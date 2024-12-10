from classes.Character import Character
from classes.Player import Player
from classes.NPC import NPC
from classes.Item import Item
import classes.Location
import classes.TextLibrary

visited_places = {
    "salle_buffet": False,
    "cuisine": False,
    "bibli": False,
    "couloir": False,
    "cave": False,
    "couloirCaverne": False
}


def NaratorFunc(input_text, **kwargs):
    """
    Process input text and return the corresponding narrative or action response.

    Args:
        input_text (str): The input command or text from the user.
        kwargs: Additional parameters for dynamic text generation.

    Returns:
        str: The narrative text or error message based on input_text.
    """
    narratives = {
        "hello": "Hello There",
        "intro": (
            "Bienvenue dans le Jeu d'Aventure !\n"
            "Vous êtes un aventurier audacieux, qui s'est aventuré dans un vieux château abandonné en pleine forêt.\n"
            "Le château a été laissé à l'abandon depuis des siècles, et des rumeurs parlent de trésors cachés et de secrets oubliés.\n"
            "Alors que vous explorez le château, vous vous retrouvez perdu dans ses couloirs sombres et labyrinthiques."
        ),
        "name_prompt": "Entrez votre nom : ",
        "good_luck": "Bonne chance, {name}. Vous allez en avoir besoin.",
        "blocked_entrance": "L'entrée du château est bloquée, il faut trouver un autre moyen de sortir !",
        "salle_buffet": (
            "Vous entrez dans une salle opulente, ornée de lustres étincelants et de longues tables chargées de vaisselle dorée.\n"
            "Chaque coin de la pièce semble suinter la richesse, mais un étrange silence règne, presque oppressant."
        ),
        "found_potion": (
            "Votre regard est attiré par une fiole posée négligemment sur une table.\n"
            "Un liquide rouge y tourbillonne mystérieusement. Vous avez trouvé une potion de vie !"
        ),
        "action_options": "Que voulez-vous faire ? Options: {options}",
        "invalid_input": "Veuillez entrer une option valide.",
        "combat_start": (
            "Une tension palpable emplit l'air. {enemy_name} se dresse devant vous, prêt à en découdre.\n"
            "{enemy_name}: {enemy_health} PV | Vous: {player_health} PV\n"
            "Que le combat commence !"
        ),
        "combat_victory": "Vous avez vaincu {enemy_name} ! Son corps s'effondre dans un bruit sourd.",
        "combat_defeat": "Vous avez été vaincu par {enemy_name}. L'obscurité vous enveloppe...",
        "inventory_empty": "Votre inventaire est vide. Peut-être devriez-vous explorer davantage...",
        "inventory_items": "Vous ouvrez votre sac et inspectez vos possessions :\n{items}"
    }

    # Handle dynamic input
    input_text = input_text.strip().lower()

    if input_text in narratives:
        # Retrieve predefined narrative
        text = narratives[input_text]
    else:
        # Handle unknown inputs
        text = "Commande inconnue. Veuillez essayer une autre commande."

    # Format the text if there are additional keyword arguments
    if kwargs:
        text = text.format(**kwargs)

    return text


# Example utility function to handle inventory formatting
def format_inventory(items):
    if not items:
        return NaratorFunc("inventory_empty")
    formatted_items = "\n".join(f"- {item}" for item in items)
    return NaratorFunc("inventory_items", items=formatted_items)
