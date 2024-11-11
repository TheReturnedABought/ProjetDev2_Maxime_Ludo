import random

class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack = attack_power

    def deal_attack(self, target):
        damage = random.randint(1, 5)
        target.health -= damage
        print(f"| {self.name} attaque ! point de vie perdu : {damage}")

    def is_alive(self):
        return self.health > 0

    def heal(self):
        pass

    def take_damage(self):
        pass

    def apply_status_effects(self):
        pass

    def remove_status_effects(self):
        pass

    def __str__(self):
        return f"| {self.name} - Points de vie : {self.health}"