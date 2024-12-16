class Location:
    def __init__(self, name, description, actions, visited=False):
        """
        Initializes a new location.

        :param name: Name of the location.
        :param description: Description of the location displayed upon first visit.
        :param actions: A dictionary of actions available in this location (e.g., move directions, inventory).
        :param visited: Boolean indicating if the location has been visited before.
        """
        self.name = name
        self.description = description
        self.actions = actions
        self.visited = visited

    def visit(self, player):
        """Handles visiting the location, displaying the description if not already visited."""
        if not self.visited:
            print(self.description)
            self.visited = True
        else:
            print(f"Vous êtes déjà passé(e) par {self.name}.")

        # If there's a special item or event in the room, handle it here.
        if self.name == "Salle du Buffet":
            potion = Item("Potion de vie", 0, 5)
            player.add_to_inventory(potion)
            print("\nVous avez trouvé une potion de vie ! Elle pourrait vous être utile plus tard.")

        self.choose_action(player)

    def choose_action(self, player):
        """Handles player actions within the location."""
        while True:
            print("\nOptions : " + "/".join(self.actions.keys()) + " ou inventaire")
            userInput = input("> ").strip().lower()

            if userInput == "inventaire":
                player.get_inventory()
            elif userInput in self.actions:
                self.actions[userInput](player)
                break
            else:
                print("Veuillez entrer une option valide.")

# Example usage of the Location class

def salleBuffet(player):
    """Creates the Salle du Buffet location and initiates the visit."""
    buffet_description = (
        "\nVous entrez dans une salle opulente, ornée de lustres étincelants et de longues tables chargées de vaisselle dorée."
        "\nChaque coin de la pièce semble suinter la richesse, mais un étrange silence règne, presque oppressant."
        "\n\nVotre regard est attiré par une fiole posée négligemment sur une table. Un liquide rouge y tourbillonne mystérieusement."
    )

    buffet_actions = {
        "left": cuisine,
        "right": couloir1,
        "forward": bibli,
        "backward": introScene
    }

    salle_buffet = Location("Salle du Buffet", buffet_description, buffet_actions)
    salle_buffet.visit(player)

# Example definitions for the placeholder functions and classes
def cuisine(player):
    print("Vous entrez dans la cuisine.")

def couloir1(player):
    """
    Creates the Couloir 1 location with a puzzle and item reward.
    """
    couloir_description = (
        "Vous entrez dans un couloir sombre et lugubre. Les murs sont ornés de portraits anciens, mais quelque chose cloche. "
        "Les tableaux sont mal alignés et un étrange frisson parcourt votre échine."
        "\n\nVous remarquez un vieux livre posé à terre. La couverture semble usée, mais le titre est encore lisible : 'L'Ordre des Âges'."
        "\nEn levant les yeux, vous remarquez que les tableaux représentent :"
        "\n1. Un enfant avec un jouet"
        "\n2. Un roi en pleine gloire"
        "\n3. Un vieillard tenant une canne"
        "\n4. Un guerrier avec une épée"
        "\n\nUne phrase du livre attire votre attention : "
        "\"Dans le grand cycle, l'enfant vient avant le guerrier, mais après le vieillard. Le roi se tient toujours entre eux.\""
    )

    def solve_puzzle(player):
        """Handles the puzzle of Couloir 1."""
        tableaux = ["Tableau 1", "Tableau 2", "Tableau 3", "Tableau 4"]
        solution = [3, 1, 4, 2]  # Correct order for the portraits
        attempts = []
        tries = 0

        print("\nVous sentez que réaligner les tableaux dans le bon ordre pourrait révéler quelque chose de caché.")

        while attempts != solution:
            print("\nVoici les tableaux dans leur état actuel :")
            print(", ".join([f"{t} (désaligné)" for t in tableaux]))

            print("\nDans quel ordre voulez-vous réaligner les tableaux ? (Entrez les numéros séparés par des espaces, ex: '3 1 4 2')")
            try:
                user_input = input("> ")
                attempts = list(map(int, user_input.split()))
            except ValueError:
                print("Veuillez entrer uniquement des chiffres.")
                continue

            tries += 1

            if attempts == solution:
                print(
                    "\nVous réalignez les tableaux dans le bon ordre. Un clic mécanique résonne, et une partie du mur coulisse lentement pour révéler un coffre secret."
                )
                print(f"Vous avez résolu l'énigme en {tries} tentative(s) !")
                print("Vous ouvrez le coffre et découvrez une épée !")
                sword = Item("Épée", 8, 0)
                player.add_to_inventory(sword)
                visited_places["couloir"] = True
                break
            elif len(attempts) != len(solution):
                print("\nVous n'avez pas aligné tous les tableaux.")
            else:
                print("\nL'ordre semble incorrect. Les tableaux restent désalignés.")

        if tries > 5:
            print("\nVous commencez à vous demander si vous n'avez pas manqué un indice quelque part.")

    couloir_actions = {
        "solve_puzzle": solve_puzzle,
        "backward": salleBuffet,
        "right": cave,
        "forward": salleMort
    }

    couloir1_location = Location("Couloir 1", couloir_description, couloir_actions)
    couloir1_location.visit(player)


def bibli(player):
    print("Vous entrez dans la bibliothèque.")

def introScene(player):
    print("Vous retournez à la scène d'introduction.")


