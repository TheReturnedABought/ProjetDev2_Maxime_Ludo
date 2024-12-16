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
    print("Vous entrez dans le couloir 1.")

def bibli(player):
    print("Vous entrez dans la bibliothèque.")

def introScene(player):
    print("Vous retournez à la scène d'introduction.")


