from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from Narator import NaratorFunc

class Interface:
    def __init__(self):
        self.stdin = ""
        self.stdout = ""

    def get_stdin(self):
        """Retrieve the current stdin value."""
        return self.stdin

    def set_stdin(self, input_text):
        """Set the stdin value."""
        if isinstance(input_text, str):
            self.stdin = input_text
        else:
            raise ValueError("Input must be a string.")

    def set_stdout(self, output_text):
        """Set the stdout value."""
        if isinstance(output_text, str):
            self.stdout = output_text
        else:
            raise ValueError("Output must be a string.")

    def get_stdout(self):
        """Retrieve the current stdout value."""
        return self.stdout

class InterfaceGUI(BoxLayout):
    def __init__(self, interface, **kwargs):
        super().__init__(**kwargs)
        self.interface = interface
        self.orientation = "vertical"
        self.spacing = 10
        self.padding = 10

        # Output section with a ScrollView
        self.output_label = Label(
            text="Output:",
            size_hint=(1, 0.05),
            halign="left",
            valign="middle",
            font_size=18,
        )
        self.add_widget(self.output_label)

        self.output_scroll = ScrollView(size_hint=(1, 0.4))
        self.output_display = TextInput(
            text="",
            size_hint_y=None,
            height=300,
            readonly=True,
            multiline=True,
            font_size=16,
            background_color=(0.9, 0.9, 0.9, 1),
            foreground_color=(0, 0, 0, 1),
        )
        self.output_scroll.add_widget(self.output_display)
        self.add_widget(self.output_scroll)

        # Input section
        self.input_label = Label(
            text="Input:",
            size_hint=(1, 0.05),
            halign="left",
            valign="middle",
            font_size=18,
        )
        self.add_widget(self.input_label)

        self.input_field = TextInput(
            hint_text="Enter command...",
            size_hint=(1, 0.1),
            font_size=16,
            multiline=False,
            background_color=(0.95, 0.95, 1, 1),
        )
        self.input_field.bind(on_text_validate=self.on_enter_key)  # Bind Enter key event
        self.add_widget(self.input_field)

        # Buttons section
        self.buttons_layout = BoxLayout(size_hint=(1, 0.1), spacing=10)
        self.submit_button = Button(
            text="Submit", size_hint=(0.5, 1), font_size=16, background_color=(0, 0.5, 1, 1)
        )
        self.submit_button.bind(on_press=self.submit_input)

        self.clear_button = Button(
            text="Clear Output",
            size_hint=(0.5, 1),
            font_size=16,
            background_color=(1, 0.5, 0, 1),
        )
        self.clear_button.bind(on_press=self.clear_output)

        self.buttons_layout.add_widget(self.submit_button)
        self.buttons_layout.add_widget(self.clear_button)
        self.add_widget(self.buttons_layout)

    def submit_input(self, instance):
        """Handle input submission."""
        input_text = self.input_field.text
        self.interface.set_stdin(input_text)

        # Process the input using NaratorFunc
        output_text = NaratorFunc(input_text)
        self.interface.set_stdout(output_text)

        # Display the output
        self.update_output(output_text)

        # Clear input field
        self.input_field.text = ""

    def update_output(self, text):
        """Update the output display."""
        self.output_display.text += text + "\n"

    def clear_output(self, instance):
        """Clear the output display."""
        self.output_display.text = ""

    def on_enter_key(self, instance):
        """Handle Enter key press."""
        self.submit_input(instance)

class TextAdventureApp(App):
    def build(self):
        interface = Interface()
        return InterfaceGUI(interface)

# Run the app
if __name__ == "__main__":
    TextAdventureApp().run()
