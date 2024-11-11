from classes.Character import Character

class NPC(Character):
    def __init__(self, name, health, attack_power, dialogue=""):
        super().__init__(name, health, attack_power)
        self.dialogue = dialogue

    def talk(self):
        if self.dialogue:
            print(f"{self.name} dit : {self.dialogue}")
        else:
            print(f"{self.name} n'a rien à dire.")
