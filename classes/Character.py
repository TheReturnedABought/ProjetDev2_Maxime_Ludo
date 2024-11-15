import random

class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack = attack_power

def deal_attack(self, target):
    damage = random.randint(1, 5)  # Random damage between 1 and 5
    target.health -= damage  # Reduce target's health by damage amount
    print(f"| {self.name} attaque ! point de vie perdu : {damage}")


def is_alive(self):
    return self.health > 0


def heal(self):
    pass  # Placeholder for healing logic


def take_damage(self, damage_amount):
    pass  # Placeholder for damage handling logic


def apply_status_effects(self, effect):
    pass  # Placeholder for status effects logic


def remove_status_effects(self , effect):
    pass  # Placeholder for removing status effects logic


def __str__(self):
    return f"| {self.name} - Points de vie : {self.health}"
