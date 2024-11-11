from classes.Character import Character

class Player(Character):
    def __init__(self, name, health, attack_power):
        self.inventory = []
        self.character_budget = 10 #argent du perso
        super().__init__(name, health, attack_power)

    def add_to_inventory(self, item):
        self.inventory.append(item)

    def remove_from_inventory(self, item):
        self.inventory.remove(item)

    def get_inventory(self):
        if len(self.inventory) == 0:
            print("| Votre inventaire est vide.")
        else:
            print(f"| Objet(s) dans votre inventaire :")
            for objet in self.inventory:
                print(f"| - {objet}")

    def save(self):
        pass #fonction pour sauvegarder la partie a completer