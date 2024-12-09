import random


class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.status_effects = []  # List to store any status effects

    def deal_attack(self, target):
        damage = random.randint(1, self.attack_power)  # Random damage based on attack power
        target.take_damage(damage)
        print(f"| {self.name} attaque {target.name} ! Point de vie perdu : {damage}")

    def is_alive(self):
        return self.health > 0

    def heal(self, amount):
        if self.is_alive():
            self.health += amount
            print(f"| {self.name} se soigne et regagne {amount} points de vie.")
        else:
            print(f"| {self.name} ne peut pas se soigner car il/elle est déjà mort(e).")

    def take_damage(self, damage_amount):
        self.health -= damage_amount
        print(f"| {self.name} subit {damage_amount} points de dégâts. Points de vie restants : {self.health}")
        if self.health <= 0:
            print(f"| {self.name} est mort(e).")

    def apply_status_effects(self, effect):
        self.status_effects.append(effect)
        print(f"| {self.name} est maintenant affecté(e) par : {effect}.")

    def remove_status_effects(self, effect):
        if effect in self.status_effects:
            self.status_effects.remove(effect)
            print(f"| L'effet {effect} a été retiré de {self.name}.")
        else:
            print(f"| {self.name} n'est pas affecté(e) par {effect}.")

    def __str__(self):
        return f"| {self.name} - Points de vie : {self.health} - Effets de statut : {', '.join(self.status_effects) if self.status_effects else 'Aucun'}"
