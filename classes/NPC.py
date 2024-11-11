from classes.Character import Character

class NPC(Character):
    def __init__(self, name):
        self.name = name
        self.dialogue = []