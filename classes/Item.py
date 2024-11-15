class Item:
    def __init__(self, name, damage_power, health_add, slot):
        self.name = name
        self.damage_power = damage_power
        self.health_add = health_add
        self.slot = slot #la place qu'il prend dans l'inventaire

    def equip(self):
        """
        PRE: Lobjet doit être dans l'inventaire et ne doit pas être déjà équipé.
        POST: L'objet est marqué comme équipé.
        Raise: Erreur si l'objet est déjà équipé.

        """
        pass

    def unequip(self):
        """

        PRE: L'objet doit être équipé.
        POST:L'objet n'est plus marqué comme équipé.
        RAISE: RunTimeError si l'objet n'est pas équipé.
        """
        pass

    def examine(self):
        pass

    def use(self):
        pass
