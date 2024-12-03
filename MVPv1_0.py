#code fait sans chatgpt (pour ça qu'il y a pas mal de faute) il faut juste améliorer les boucles et conditions pour que ca "fonctionn"

import random

class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack = attack_power

    def deal_attack(self, target):
        damage = random.randint(1, 5)
        target.health -= damage
        print(f"{self.name} attaque ! point de vie perdu : {damage}")

    def isAlive(self):
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
        return f"{self.name} - Points de vie : {self.health}"


class Player(Character):
    def __init__(self, name, health, attack_power):
        self.inventory = []
        self.character_budget = 10 #argent du perso
        super().__init__(name, health, attack_power)

    def add_to_inventory(self, item):
        self.inventory.append(item)

    def remove_from_inventory(self, item):
        self.inventory.remove(item)

    def get_inventory(self):
        if len(self.inventory) == 0:
            print("votre inventaire est vide")
        else:
            print(f"objet dans votre inventaire :")
            for objet in self.inventory:
                print(f"- {objet}")

    def save(self):
        pass #fonction pour sauvegarder la partie a completer


class NPC(Character):
    def __init__(self, name):
        self.name = name
        self.dialogue = []

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

class quest:
    def __init__(self, rewards, objectif):
        self.rewards = rewards
        self.objectif = objectif
        self.completed = False

class Locations:
    def __init__(self, name):
        self.name = name
        self.all_locations = []
        self.id = 0

    def interact(self, int):
        pass

class TextLibrary:
    def __init__(self):
        self.dico_text = []

    def display_text(self):
        pass



player = Player("Héros", 20, 5)
enemy = Character("Ennemi", 15, 4)


while player.isAlive():
    print("\nQue voulez-vous faire ?")
    print("1. explorer")
    print("2. attaquer")
    print("3. consulter votre inventaire")

    reponse = input("Entrer le numéro de votre choix")
    if reponse == "1":
        print("Vers ou voulez-vous aller ? \n Nord, Sud, Est, Ouest")
        direction = input("Entrer la direction du choix")
        if direction == "Nord" and "Sud" and "Est" and "Ouest":
            print("Vous rencontrer un gobelin sur votre chemin, il à l'air de vouloir vous attaquer ! Que faire?")
            

    if reponse == "2":
        player.deal_attack(enemy)
        if enemy.isAlive() :
            enemy.deal_attack(player)
    elif reponse == "3":
        player.get_inventory()
        
    else :
        print("choix invalide")

if player.is_alive():
    print("\nFélicitations ! Vous avez vaincu l'ennemi.")
else:
    print("\nVous avez été vaincu par l'ennemi. Fin de la partie.")
