class Item:
    def __init__(self, name, damage_power=0, health_add=0, slot=1):
        self.name = name
        self.damage_power = damage_power
        self.health_add = health_add
        self.slot = slot  # Taille de l'item dans l'inventaire

    def use(self, target=None):
        if self.damage_power > 0 and target:
            print(f"Vous utilisez {self.name} pour attaquer {target.name} !")
            target.health -= self.damage_power
        elif self.health_add > 0:
            print(f"Vous utilisez {self.name} et gagnez {self.health_add} points de vie.")
        else:
            print(f"{self.name} ne peut pas être utilisé comme ça.")

    def equip(self):
        print(f"{self.name} est équipé.")

    def unequip(self):
        print(f"{self.name} est déséquipé.")

    def examine(self):
        print(f"{self.name}: dégâts = {self.damage_power}, soin = {self.health_add}")
