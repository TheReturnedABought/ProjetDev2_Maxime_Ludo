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

visited_places = {
    "salle_buffet": False,
    "cuisine": False
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
        print("\nVotre inventaire est vide. Peut-être devriez-vous explorer davantage...")
        return

    print("\nVous ouvrez votre sac et inspectez vos possessions :")
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
    print(
        "\nVous entrez dans une salle opulente, ornée de lustres étincelants et de longues tables chargées de vaisselle dorée.")
    print("Chaque coin de la pièce semble suinter la richesse, mais un étrange silence règne, presque oppressant.")
    print(
        "\nVotre regard est attiré par une fiole posée négligemment sur une table. Un liquide rouge y tourbillonne mystérieusement.")
    potion = Item("Potion de vie", 0, 5)
    player.add_to_inventory(potion)
    print("\nVous avez trouvé une potion de vie ! Elle pourrait vous être utile plus tard.")

    directions = ["left", "right", "forward", "backward"]
    print("\nPar où voulez-vous aller ? Que voulez-vous faire ?")

    while True:
        print("Options : left/right/backward/forward ou inventaire")
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
            print("Veuillez entrer une option valide.")


# fonction à appeler quand on va dans la cuisine
def cuisine(player):
    """
    Scène immersive dans la cuisine avec un combat
    """
    if visited_places["cuisine"]:
        print("\nVous retournez dans la cuisine. Elle est désormais silencieuse et vide.")
        print("Le sol est encore marqué par les traces du combat précédent.")
        salleBuffet(player)

    visited_places["cuisine"] = True

    print("\nVous poussez une porte grinçante et entrez dans ce qui semble être une cuisine.")
    print("L'odeur de nourriture rance flotte dans l'air, mélangée à celle de bois brûlé.")
    print("Des étagères croulent sous des ustensiles rouillés, et un chaudron abandonné repose au centre.")
    print("\nAlors que vous vous avancez prudemment, une ombre furtive surgit !")
    print("Un gobelin malingre, armé d'un couteau de cuisine rouillé, vous bloque le passage.")
    print(f"Le gobelin montre les crocs et crie : 'Personne ne vole MES provisions !'")

    # Création de l'ennemi
    enemy = Character("Gobelin", health=15, attack_power=3)

    # Lancer le combat
    if combat(player, enemy):  # Si le combat est gagné
        print("\nAprès un combat acharné, le gobelin s'effondre en grognant. Le calme revient dans la pièce.")
        print("Vous explorez rapidement la cuisine et trouvez des provisions et un couteau de cuisine.")
        couteau = Item("Couteau de cuisine", 5, 0)
        provisions = Item("Provisions", 0, 5)
        player.add_to_inventory(provisions)
        player.add_to_inventory(couteau)
        print("\nVous ajoutez les provisions et le couteau à votre inventaire.")

        directions = ["backward"]
        while True:
            print("\nQue voulez-vous faire maintenant ?")
            print("Options : backward / inventaire")
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
    print(
        "Vous entrez dans un couloir sombre et lugubre. Les murs sont ornés de portraits anciens, mais quelque chose cloche.")
    print("Les tableaux sont mal alignés et un étrange frisson parcourt votre échine.")
    print(
        "\nAlors que vous avancez prudemment, vous remarquez un vieux livre posé à terre. La couverture semble usée, mais le titre est encore lisible : *'L'Ordre des Âges'.*")
    print("\nVous ramassez le livre et l'ouvrez. Une phrase attire votre attention :")
    print(
        "\"Dans le grand cycle, l'enfant vient avant le guerrier, mais après le vieillard. Le roi se tient toujours entre eux.\"")
    print("\nEn levant les yeux, vous remarquez que les tableaux représentent :")
    print("1. Un enfant avec un jouet")
    print("2. Un roi en pleine gloire")
    print("3. Un vieillard tenant une canne")
    print("4. Un guerrier avec une épée")

    # Demander si le joueur veut résoudre l'énigme ou non
    choix_énigme = input("\nVoulez-vous regarder de plus près les tableaux? (oui/non) > ").strip().lower()

    if choix_énigme != "oui":
        print("\nVous décidez de ne pas résoudre l'énigme pour le moment.")
        print("Vous continuez à avancer dans le couloir, en ignorant les tableaux mal alignés.")
        # Ajouter un autre élément de l'histoire ici pour continuer sans résoudre l'énigme
        print("\nVous sentez une légère brise venant d'un autre passage. Vous décidez de vous y diriger.")
        # Choisir où aller après avoir ignoré l'énigme
        choix_direction(player)
        return

    tableaux = ["Tableau 1", "Tableau 2", "Tableau 3", "Tableau 4"]
    solution = [3, 1, 4, 2]  # Ordre correct pour réaligner les tableaux
    essais = []
    tentatives = 0

    print("\nVous sentez que réaligner les tableaux dans le bon ordre pourrait révéler quelque chose de caché.")

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
    print("Vous entrez dans une cave sombre et mystérieuse. Devant vous se dresse une statue imposante d'un sphinx.")
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
            return  # Fin de la scène en cas d'échec.

    print("\nVotre réponse semble déclencher quelque chose d'irréversible. Les murs tremblent, puis s’effondrent brusquement. \nUne masse d’eau vive jaillit des décombres et vous emporte avec une force inouïe. Incapable de lutter, vous êtes propulsé dans une grotte sombre et profonde. \nLes remous violents vous poussent contre les parois rocheuses, et vous vous retrouvez haletant sur une plage de sable noir, à l'intérieur de cette mystérieuse caverne.")

    print("\nUn seul chemins s'offrent à vous :")
    print("Un passage éclairé par une faible lumière.")

    directions = ["left", "right", "forward", "backward"]
    userInput = ""
    while userInput not in directions:
        print("Options: forward ou inventaire")
        userInput = input()
        if userInput == "forward":
            cuisine(player)


def chambre(player):
    pass;


def salleMort(player):
    pass


# fonction qui lance le jeu
def main():
    """
    Fonction principale du jeu
    """
    print("Bienvenue dans le Jeu d'Aventure !")
    print("Vous êtes un aventurier audacieux, qui s'est aventuré dans un vieux château abandonné en pleine forêt.")
    print(
        "Le château a été laissé à l'abandon depuis des siècles, et des rumeurs parlent de trésors cachés et de secrets oubliés.")
    print("Alors que vous explorez le château, vous vous retrouvez perdu dans ses couloirs sombres et labyrinthiques.")
    print("Vous pouvez choisir de vous déplacer dans différentes directions pour découvrir ce que cache le château.")

    # Demander le nom du joueur
    name = input("Entrez votre nom : ")
    print(f"Bonne chance, {name}. Vous allez en avoir besoin.")

    # Créer le joueur
    player = Player(name, health=20, attack_power=5)

    # Commencer le jeu
    introScene(player)


if __name__ == "__main__":
    main()
