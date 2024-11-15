import random

class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack = attack_power

def deal_attack(self, target):
    """
    Method: deal_attack
    -------------------
    Pre-condition: The target must be a valid object with a health attribute.
    Post-condition: Inflicts damage on the target, reducing its health points.

    This method randomly determines the damage (between 1 and 5) and decreases 
    the target's health by that amount. It then prints the result of the attack.
    """
    damage = random.randint(1, 5)  # Random damage between 1 and 5
    target.health -= damage  # Reduce target's health by damage amount
    print(f"| {self.name} attaque ! point de vie perdu : {damage}")


def is_alive(self):
    """
    Method: is_alive
    ----------------
    Pre-condition: The object must have a health attribute.
    Post-condition: Returns True if health is greater than 0, otherwise False.

    Checks whether the character is still alive (i.e., has positive health).
    """
    return self.health > 0


def heal(self):
    """
    Method: heal
    ------------
    Pre-condition: The character must not be at full health.
    Post-condition: Increases the character's health by a certain amount (if implemented).

    This method is currently a placeholder for adding healing logic.
    """
    pass  # Placeholder for healing logic


def take_damage(self):
    """
    Method: take_damage
    -------------------
    Pre-condition: The object must have a health attribute.
    Post-condition: Reduces the health of the character (if implemented).

    This method is currently a placeholder for adding damage-taking logic.
    """
    pass  # Placeholder for damage handling logic


def apply_status_effects(self):
    """
    Method: apply_status_effects
    ----------------------------
    Pre-condition: Status effects should be defined for the character.
    Post-condition: Applies effects that modify the character's attributes (if implemented).

    This method is currently a placeholder for adding logic to apply status effects.
    """
    pass  # Placeholder for status effects logic


def remove_status_effects(self):
    """
    Method: remove_status_effects
    -----------------------------
    Pre-condition: Status effects should have been previously applied.
    Post-condition: Removes status effects from the character (if implemented).

    This method is currently a placeholder for adding logic to remove status effects.
    """
    pass  # Placeholder for removing status effects logic


def __str__(self):
    """
    Method: __str__
    ---------------
    Pre-condition: The character must have name and health attributes.
    Post-condition: Returns a formatted string displaying the character's name and health.

    Provides a string representation of the character for printing purposes.
    """
    return f"| {self.name} - Points de vie : {self.health}"
