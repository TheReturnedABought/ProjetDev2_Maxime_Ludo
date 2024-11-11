from classes.Character import Character
from classes.Player import Player
import classes.NPC
import classes.Item
import classes.Quest
import classes.Location
import classes.TextLibrary

player = Player("Héros", 20, 5)
enemy = Character("Ennemi", 15, 4)
print("\n|-----------------------------|\n|   Bienvenue dans le jeu !   "
      "|\n|-----------------------------|")

first_choice = " 1. Explorer"
second_choice = " 2. Attaquer"
third_choice = " 3. Consulter votre inventaire"

def display_choice(nb):
    match nb:
        case '1':
            print(f"\n|{first_choice}")
        case '2':
            print(f"\n|{second_choice}")
        case '3':
            print(f"\n|{third_choice}")
        case _:
            return
    print("|--------------------------------")


while player.is_alive():
    print("\nQue voulez-vous faire ?")
    print(first_choice)
    print(second_choice)
    print(third_choice)

    reponse = input("Entrez le numéro de votre choix : ")

    display_choice(reponse)
    if reponse == "1":
        print("| Vers où voulez-vous aller ? [nord | sud | est | ouest]")
        direction = input("| Entrez la direction du choix en minuscule : ")
        if direction in ["nord", "sud", "est", "ouest"]:
            print(f"|<>| Vous vous dirigez vers le {direction}. \n"
                  "|<>| Vous rencontrez un gobelin sur votre chemin. \n|<>| Il a l'air de vouloir vous attaquer ! Réagissez !")
        else:
            print("|<>| Le choix est invalide ou la casse n'est pas respectée.")

    elif reponse == "2":
        player.deal_attack(enemy)
        if enemy.is_alive() :
            enemy.deal_attack(player)
            print(f"{player}\n{enemy}")
        else:
            print(f"Vous avez vaincu {enemy.name}. Félicitations !")
            input("\nAppuyez sur ENTER pour fermer le jeu.")
            break


    elif reponse == "3":
        player.get_inventory()

    else:
        print("|<>| Le choix est invalide.")

else:
    print("\nVous avez été vaincu par l'ennemi. Fin de la partie.")
    input("\nAppuyez sur ENTER pour fermer le jeu.")
