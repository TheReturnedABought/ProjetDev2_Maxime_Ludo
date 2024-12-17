from classes.Character import Character

class Player(Character):
    def __init__(self, name, health, attack_power):
        self.inventory = []
        self.character_budget = 10 #argent du perso
        super().__init__(name, health, attack_power)


    def add_to_inventory(self, item):
        self.inventory.append(item)

        """
        Ajoute dans l'inventaire (liste) "item" qui est une string
        
        PRE : item est une string représentant un objet physique.
        POST: l'item est dans l'inventaire après l'ajout.
        

        """


    def remove_from_inventory(self, item):
        self.inventory.remove(item)

        """
        Enlève de l'inventaire (liste) "item" qui est un string
        
        PRE : L'item que le joueur veut retirer.
        POST: Renvoie que l'item n'est plus dans l'inventaire.
        RAISE : renvoie une erreur si item n'est pas dans l'inventaire 
        """


    def get_inventory(self):
        """
        prend la liste "inventory" et la transmet à une fonction "show_inventory"

        PRE : l'inventaire initialisé.
        POST: retourne l'appel à la fonction show_inventory(self.inventory).
        """
        if not isinstance(self.inventory, list):
            raise ValueError("L'inventaire n'est pas initialisé correctement.")
        return self.show_inventory(self.inventory)

    def show_inventory(self, inventory):
        """
        Cette fonction affiche le contenu de l'inventaire.
        PRE : 'inventory' est une liste.
        POST: Retourne une représentation textuelle de l'inventaire.
        """
        if not inventory:
            return "L'inventaire est vide."
        return f"Inventaire : {', '.join(map(str, inventory))}"
        
    def save(self):
        pass #fonction pour sauvegarder la partie a completer
