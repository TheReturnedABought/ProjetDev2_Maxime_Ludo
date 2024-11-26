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
        if not isinstance(self.inventory, list):
        raise ValueError("L'inventaire n'est pas initialisé correctement.")

       """
        prend la liste "inventory" et la transmet à une fonction "show_inventory"

        PRE : l'inventaire initialisé.
        POST: retourne l'appel à la fonction show_inventory(self.inventory).
        Raise : si l'inventaire n'a pas été initialisé correctement : renvoie ValueError
        """


    def save(self):
        pass #fonction pour sauvegarder la partie a completer
