import random

class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.status_effects = {}  # Pour stocker des effets de statut éventuels

    def deal_attack(self, target):
        damage = random.randint(1, self.attack_power)
        target.health -= damage
        print(f"{self.name} attaque {target.name} ! Points de vie perdus : {damage}")

    def is_alive(self):
        return self.health > 0

    def heal(self, amount):
        self.health += amount
        print(f"{self.name} récupère {amount} points de vie.")

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} subit {damage} points de dégâts.")

    def apply_status_effects(self):
        # Applique les effets de statut, par exemple : poison, paralysie, etc.
        pass

    def remove_status_effects(self):
        # Supprime tous les effets de statut
        self.status_effects.clear()

    def __str__(self):
        return f"{self.name} - Points de vie : {self.health}"
