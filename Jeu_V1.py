"""A faire : 
- séparer la logique de programmation et l'affichage 
- faire un affichage avec Kivy
- nettoyer un peu les fonctions et méthodes
- développer les méthodes pour qu'elles fonctionnes (enlever certaine si trop chiant à mettre en place)
"""
from classes.Character import Character
from classes.Player import Player
from classes.NPC import NPC
from classes.Item import Item
import classes.Location
import classes.TextLibrary
from classes.narrator import NaratorFunc

visited_places = {
    "salle_buffet": False,
    "cuisine": False,
    "bibli": False,
    "couloir": False,
    "cave": False,
    "couloirCaverne": False
}


# Partie logique

def equip_item(player):
    print("Quel objet voulez-vous équiper ?")
    # Display available items and let the player equip one
    for i, item in enumerate(player.inventory):
        print(f"{i + 1}. {item.name}")
    choice = int(input("> ")) - 1
    if 0 <= choice < len(player.inventory):
        item = player.inventory[choice]
        player.equip(item)  # Assuming an equip method in Player class
        print(f"{item.name} est maintenant équipé !")


# fonction à appeler quand il y a un combat
def combat(player, enemy):
    print(f"\nUne tension palpable emplit l'air. {enemy.name} se dresse devant vous, prêt à en découdre.")
    print(f"\n{enemy.name}: {enemy.health} PV | Vous: {player.health} PV")
    print("\nQue le combat commence !")

    while player.is_alive() and enemy.is_alive():
        # Attaque du joueur
        print("\nVous préparez votre attaque...")
        attack_result = player.deal_attack(enemy)
        print(attack_result)

        # Vérifier si l'ennemi est mort
        if not enemy.is_alive():
            print(f"\nVous avez vaincu {enemy.name} ! Son corps s'effondre dans un bruit sourd.")
            return True

        # Contre-attaque de l'ennemi
        print(f"\n{enemy.name} riposte avec rage !")
        enemy_attack = enemy.deal_attack(player)
        print(enemy_attack)

        # Afficher l'état des personnages
        print(f"\nVotre état : {player}\n{enemy}")

        # Demander une action au joueur
        action = input("\nQue voulez-vous faire ? (continuer/fuir) ").strip().lower()
        if action == "fuir":
            print("\nVous tournez les talons et fuyez, le cœur battant.")
            return False


# fonction pour montrer l'inventaire
def show_inventory(inventory):
    if not inventory:

        return

    for item in inventory:
        print(f"- {item}")
    actions = ["équiper", "déséquiper", "utiliser", "quitter"]
    user_action = ""
    while user_action not in actions:
        print("\nQue voulez-vous faire ? (équiper, déséquiper, utiliser, quitter)")
        user_action = input("> ").strip().lower()

    if user_action == "équiper":
        equip_item(player)
    elif user_action == "déséquiper":
        print("Vous réfléchissez à déséquiper un objet, mais rien ne semble pertinent pour l'instant.")
    elif user_action == "utiliser":
        print("Vous vous demandez quel objet pourrait être utile...")
    elif user_action == "quitter":
        print("Vous refermez votre sac et vous préparez à continuer l'aventure.")


# début du jeu
def introScene(player):
    directions = ["forward"]
    print("L'entrée d'ou vous venez est bloqué, il faut trouver un autre moyen de sortir ! Par ou aller vous ?")
    userInput = ""
    while userInput not in directions:
        print("Options: forward")
        userInput = input()
        if userInput == "forward":
            salleBuffet(player)
        elif userInput == "backward":
            print("L'entrée du chateau est bloqué")
        else:
            print("Please enter a valid option for the adventure game.")


# fonction à appeler quand on va dans la salle de buffet
def salleBuffet(player):
    potion = Item("Potion de vie", 0, 5)
    player.add_to_inventory(potion)

    directions = ["left", "right", "forward", "backward"]
    while True:
        userInput = input("> ").strip().lower()
        if userInput == "left":
            cuisine(player)
        elif userInput == "right":
            couloir1(player)
        elif userInput == "forward":
            bibli(player)
        elif userInput == "backward":
            introScene(player)
        elif userInput == "inventaire":
            player.get_inventory()
        else:



# fonction à appeler quand on va dans la cuisine
def cuisine(player):
    """
    Scène immersive dans la cuisine avec un combat
    """
    if visited_places["cuisine"]:
        salleBuffet(player)

    visited_places["cuisine"] = True

    #ancien print

    # Création de l'ennemi
    enemy = Character("Gobelin", health=15, attack_power=3)

    # Lancer le combat
    if combat(player, enemy):  # Si le combat est gagné

        couteau = Item("Couteau de cuisine", 5, 0)
        provisions = Item("Provisions", 0, 5)
        player.add_to_inventory(provisions)
        player.add_to_inventory(couteau)

        directions = ["backward"]
        while True:

            userInput = input("> ").strip().lower()
            if userInput == "backward":
                print("\nVous quittez la cuisine et retournez dans la salle du buffet.")
                salleBuffet(player)
            elif userInput == "inventaire":
                player.get_inventory()
            else:
                print("Cela ne semble pas être une option valide.")
    else:  # Si le joueur fuit ou perd
        print("\nVous battez en retraite, laissant la cuisine derrière vous.")
        salleBuffet(player)


def couloir1(player):
    if visited_places["couloir"] == True:
        pass;

    else:


        # Demander si le joueur veut résoudre l'énigme ou non
        choix_énigme = input(NaratorFunc("demande_engime")).strip().lower()

        if choix_énigme != "oui":

            # ancien print

            # ancien print
            choix_direction(player)
            return

        tableaux = ["Tableau 1", "Tableau 2", "Tableau 3", "Tableau 4"]
        solution = [3, 1, 4, 2]  # Ordre correct pour réaligner les tableaux
        essais = []
        tentatives = 0



        while essais != solution:
            print("\nVoici les tableaux dans leur état actuel :")
            print(", ".join([f"{t} (désaligné)" for t in tableaux]))

            print(
                "\nDans quel ordre voulez-vous réaligner les tableaux ? (Entrez les numéros séparés par des espaces, ex: '3 1 4 2')")
            try:
                choix = input("> ")
                essais = list(map(int, choix.split()))
            except ValueError:
                print("Veuillez entrer uniquement des chiffres.")
                continue

            tentatives += 1

            if essais == solution:
                print(
                    "\nVous réalignez les tableaux dans le bon ordre. Un clic mécanique résonne, et une partie du mur coulisse lentement pour révéler un coffre secret.")
                print(f"Vous avez résolu l'énigme en {tentatives} tentatives !")
                print("Vous ouvrez le coffre et découvrez une épée!")
                epee = Item("épée", 8, 0)
                player.add_to_inventory(epee)
                visited_places["couloir"] = True
                break

            elif len(essais) != len(solution):
                print("\nVous n'avez pas aligné tous les tableaux.")
            else:
                print("\nL'ordre semble incorrect. Les tableaux restent désalignés.")

        if tentatives > 5:
            print("\nVous commencez à vous demander si vous n'avez pas manqué un indice quelque part.")

        # À la fin de l'énigme, ou si l'énigme n'est pas résolue, demander où aller
        choix_direction(player)


def choix_direction(player):
    """
    Permet de choisir où aller après l'énigme.
    """
    directions = ["forward", "backward", "right"]
    userInput = ""
    while userInput not in directions:
        print("\nOù voulez-vous aller maintenant ? (forward, backward, right)")
        userInput = input("> ").strip().lower()
        if userInput == "forward":
            print("\nVous avancez prudemment dans le couloir...")
            salleMort(player)
        elif userInput == "backward":
            salleBuffet(player)

        elif userInput == "right":
            print("\nVous tournez à droite...")
            cave(player)


def bibli(player):
    """
    Scène de la bibliothèque avec rencontre d'un fantôme et un avertissement pour éviter de mourir ici.
    """
    if visited_places["bibli"] == True:
        print("La bibliothèque semble si calme sans le fantôme")
    else:
        print(
            "\nVous poussez lentement la porte en bois massive de la bibliothèque. L'air à l'intérieur est lourd et poussiéreux.")
        print(
            "Des rayonnages immenses s'étendent à perte de vue, remplis de livres anciens, certains à peine lisibles à cause de l'usure du temps.")
        print(
            "L'odeur du vieux papier et du bois vieilli emplit vos narines. La pièce semble abandonnée depuis des siècles.")
        print(
            "\nSoudain, un frisson vous parcourt l'échine. Vous apercevez une silhouette translucide, presque éthérée, flottant devant une étagère.")
        print("C'est un fantôme, un esprit qui semble perdu dans le temps. Il vous regarde, comme s'il vous attendait.")
        print("\nLe fantôme se tourne vers vous et, d'une voix grave mais douce, il commence à parler :")
        print(
            "\"Je suis l'âme du dernier propriétaire de ce château, un érudit obsédé par la connaissance. Jadis, je suis mort ici, seul et oublié, pris au piège des ombres de ce lieu maudit.\"")
        print(
            "Le fantôme s'approche lentement, ses traits se précisant, et vous pouvez presque voir des larmes briller dans ses yeux.")
        print(
            "\"Je suis resté prisonnier de ces murs, piégé par mes erreurs. Ne fais pas la même chose, aventurier. Ne meurs pas ici comme moi. Ce château te réclame, mais il est aussi une prison.\"")
        print("Il semble profondément triste, mais continue :")
        print(
            "\"Il y a une issue, mais elle est bien cachée. Prends le chemin à droite, et lorsque tu arriveras au portrait du roi, tourne à droite. Suis ce chemin avec prudence, car des pièges se cachent dans l'ombre.\"")
        print("\"Va, vite, et échappe à ce destin funeste. Le temps est compté.\"")
        print("\nLe fantôme disparaît lentement dans un éclat de lumière pâle, laissant derrière lui un silence lourd.")
        print("Vous sentez que l'atmosphère de la bibliothèque a changé, mais un lourd pressentiment demeure.")
        print("\nQue voulez-vous faire ?")

        # Offrir des options pour continuer l'aventure
        directions = ["left", "right", "forward", "backward"]
        userInput = ""
        while userInput not in directions:
            print("Options: left, right, backward ou inventaire")
            userInput = input()
            if userInput == "left":
                cuisine(player)
            elif userInput == "right":
                couloir1(player)
            elif userInput == "backward":
                salleBuffet(player)
            elif userInput == "inventaire":
                player.get_inventory()  # Voir l'inventaire


def cave(player):
    if visited_places["cave"] == True:
        print("vous pouvez voir le trou géant qui vous a emmené dans la grotte")
        print("voulez-vous aller dans la grotte")
        userInput = input()
        if userInput == "oui":
            couloirCaverne(player)
        else:
            print("vous retourner dans le couloir")
            couloir1(player)
    else:
        print(
            "Vous entrez dans une cave sombre et mystérieuse. Devant vous se dresse une statue imposante d'un sphinx.")
        print("Son regard perçant semble suivre chacun de vos mouvements.")
        print("\nSoudain, une voix grave résonne dans l'air :")
        print('"Où allez-vous en cette heure si tardive ?"\n')
        print("Vous ne voyez pas d'où provient la voix, mais elle dégage une telle autorité que vous en tremblez.")
        print('"Si vous souhaitez avancer, vous devez répondre à mes trois énigmes."\n')

        enigmes = [
            {
                "question": "Je colle éternellement et rien n'empêchera mon arrivée. Tout me fuit, mais tout passe en moi. Qui suis-je ?",
                "reponse": ["le temps", "temps"],
                "effet": "Les murs autour de vous semblent vieillir et se fissurer, comme si des siècles s'étaient écoulés en un instant."
            },
            {
                "question": "Petit, je donne du plaisir, mais grand, je détruis des villes. Mon amour est la lune, et mon désir est la mer. Qui suis-je ?",
                "reponse": ["les vagues", "vague", "une vague"],
                "effet": "Une goutte froide tombe sur votre épaule depuis le plafond, et un bruit d'eau se fait entendre au loin."
            },
            {
                "question": "Je brûle comme le feu ou je mijote sous la peau. Je vise la justice, mais souvent, je suis trompeuse. Qui suis-je ?",
                "reponse": ["la colère", "colère"],
                "effet": "Les murs s'effondrent soudainement, et une masse d'eau vous emporte avec violence vers une grotte sombre."
            }
        ]

        for i, enigme in enumerate(enigmes, start=1):
            print(f"\nÉnigme {i} :")
            print(f'"{enigme["question"]}"\n')

            tentative = input("> ").strip().lower()
            if tentative in enigme["reponse"]:
                print("\nBonne réponse !")
                print(enigme["effet"])
            else:
                print("\nMauvaise réponse...")
                print("La statue reste immobile, mais vous sentez la tension monter dans l'air.")
                print("Vous devez retenter votre chance pour continuer.")
                return

        print(
            "\nVotre réponse semble déclencher quelque chose d'irréversible. Les murs tremblent, puis s’effondrent brusquement. \nUne masse d’eau vive jaillit des décombres et vous emporte avec une force inouïe. Incapable de lutter, vous êtes propulsé dans une grotte sombre et profonde. \nLes remous violents vous poussent contre les parois rocheuses, et vous vous retrouvez haletant sur une plage de sable noir, à l'intérieur de cette mystérieuse caverne.")

        print("\nUn seul chemins s'offrent à vous :")
        print("Un passage éclairé par une faible lumière.")
        visited_places["cave"] = True

        directions = ["left", "right", "forward", "backward"]
        userInput = ""
        while userInput not in directions:
            print("Options: forward ou inventaire")
            userInput = input()
            if userInput == "forward":
                couloirCaverne(player)
            if userInput == "inventaire":
                player.get_inventory()  # Voir l'inventaire


def couloirCaverne(player):
    if visited_places["cuisine"] == True:
        print("vous arpenter les couloirs sombres de la caverne, celle-ci à l'air bien calme sans l'immense araignée ")

    print(
        "\nVous avancez dans les couloirs sombres de la grotte. L'air est lourd, et une odeur nauséabonde vous prend à la gorge.")
    print(
        "Soudain, un bruit inquiétant résonne. Vous levez les yeux et apercevez une énorme araignée suspendue au plafond.")
    print("Elle descend lentement sur sa toile, ses yeux multiples brillant dans l'obscurité.")
    print("\nC'est un combat à mort ! Préparez-vous !\n")

    enemy = Character("Araignée", 15, 4)
    if combat(player, enemy):
        print(
            "Après un combat long et éprouvant, vous parvenez finalement à terrasser la bête monstrueuse. L'araignée géante s'effondre dans un dernier spasme, ses immenses pattes se repliant sur elles-mêmes.")
        print(
            "Vous respirez profondément, le cœur battant à tout rompre, et une pensée ironique traverse votre esprit :")
        print("\"Elle ne semble plus si redoutable maintenant qu'elle est morte.\"")
        print("\nMais alors que vous vous détendez un instant, une vision terrifiante vous glace le sang.")
        print(
            "Le corps de l'araignée commence à se décomposer à une vitesse anormale. Sa carapace se fissure, et soudain, elle explose en une myriade de petites araignées grouillantes.")
        print(
            "Les créatures minuscules se déversent en une vague noire et chaotique, envahissant le sol autour de vous. Elles se dispersent dans toutes les directions, disparaissant dans les ombres.")
        print("\nAu centre de ce chaos grouillant, quelque chose brille faiblement dans l'obscurité.")
        print(
            "En vous approchant avec précaution, vous découvrez une clé étrange posée sur le sol, là où la bête avait rendu son dernier souffle.")
        print(
            "La clé est froide au toucher, ornée de motifs arachnéens gravés dans le métal noirci. Elle semble presque vivante, pulsant légèrement comme si elle portait encore un fragment de l'araignée.")
        print(
            "\nVous savez que cet objet a une importance cruciale, mais une part de vous ne peut s’empêcher de frissonner en la tenant dans vos mains.")

        clé = Item("Clé de l'araignée", 0, 0)
        player.add_to_inventory(clé)


def chambre(player):
    pass;


def salleMort(player):
    pass


# fonction qui lance le jeu
def main():
    """
    Fonction principale du jeu
    """
    
    # Demander le nom du joueur
    name = input("Entrez votre nom : ")
    print(f"Bonne chance, {name}. Vous allez en avoir besoin.")

    # Créer le joueur
    player = Player(name, health=20, attack_power=5)

    # Commencer le jeu
    introScene(player)


if __name__ == "__main__":
    main()
