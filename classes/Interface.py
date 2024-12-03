from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button

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

        # Output display
        self.output_label = Label(text="Output:", size_hint=(1, 0.1))
        self.add_widget(self.output_label)

        self.output_display = TextInput(
            text="", size_hint=(1, 0.3), readonly=True, multiline=True
        )
        self.add_widget(self.output_display)

        # Input field
        self.input_label = Label(text="Input:", size_hint=(1, 0.1))
        self.add_widget(self.input_label)

        self.input_field = TextInput(hint_text="Enter command...", size_hint=(1, 0.1))
        self.add_widget(self.input_field)

        # Submit button
        self.submit_button = Button(text="Submit", size_hint=(1, 0.1))
        self.submit_button.bind(on_press=self.submit_input)
        self.add_widget(self.submit_button)

    def submit_input(self, instance):
        """Handle input submission."""
        input_text = self.input_field.text
        self.interface.set_stdin(input_text)

        # Simulate processing (example: echo back the input)
        output_text = f"You entered: {input_text}"
        self.interface.set_stdout(output_text)

        # Display the output
        self.update_output(output_text)

        # Clear input field
        self.input_field.text = ""

    def update_output(self, text):
        """Update the output display."""
        self.output_display.text += text + "\n"

class TextAdventureApp(App):
    def build(self):
        interface = Interface()
        return InterfaceGUI(interface)

# Run the app
if __name__ == "__main__":
    TextAdventureApp().run()
