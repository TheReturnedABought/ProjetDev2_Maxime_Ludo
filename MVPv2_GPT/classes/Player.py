from classes.Character import Character

class Player(Character):
    def __init__(self, name, health, attack_power):
        super().__init__(name, health, attack_power)
        self.inventory = []
        self.character_budget = 10  # argent du personnage

    def add_to_inventory(self, item):
        self.inventory.append(item)
        print(f"Vous avez ajouté {item.name} à votre inventaire.")

    def remove_from_inventory(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            print(f"Vous avez retiré {item.name} de votre inventaire.")
        else:
            print(f"{item.name} n'est pas dans l'inventaire.")

    def get_inventory(self):
        if not self.inventory:
            print("Votre inventaire est vide.")
        else:
            print("Objets dans votre inventaire :")
            for item in self.inventory:
                print(f"- {item.name}")

    def save(self):
        pass  # Méthode pour sauvegarder la progression du joueur
