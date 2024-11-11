class TextLibrary:
    def __init__(self):
        self.texts = {}

    def add_text(self, key, text):
        self.texts[key] = text

    def display_text(self, key):
        if key in self.texts:
            print(self.texts[key])
        else:
            print("Texte non trouvé.")
