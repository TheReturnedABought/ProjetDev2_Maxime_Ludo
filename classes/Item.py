class Item:
    def __init__(self, name, damage_power, health_add, slot):
        self.name = name
        self.damage_power = damage_power
        self.health_add = health_add
        self.slot = slot #la place qu'il prend dans l'inventaire

    def equip(self):
        pass

    def unequip(self):
        pass

    def examine(self):
        pass

    def use(self):
        pass