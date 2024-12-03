class Item:
    def __init__(self, name, damage_power, health_add, slot, equiped = False):
        self.name = name
        self.damage_power = damage_power
        self.health_add = health_add
        self.slot = slot #la place qu'il prend dans l'inventaire
        self.equiped = equiped
    def equip(self):
        """
       "équipe" l'item, le marque comme "dans la main" du joueur.

        PRE: L'objet que le joueur veux équiper.
        POST: L'objet est marqué comme équipé.
        Raise: renvoie une erreur si l'objet est déjà équipé ou si il n'y a aucun objet dans l'inventaire.

        """
        pass

    def unequip(self):
        """
        "Déséquipe" l'item de la main du joueur.
        PRE: 
        POST:L'objet n'est plus marqué comme équipé.
        RAISE: RunTimeError si l'objet n'est pas équipé.

        """
        pass

    def examine(self):
        pass

    def use(self):
        pass
