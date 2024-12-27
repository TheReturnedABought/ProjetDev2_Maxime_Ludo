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
            "Bienvenue dans le Jeu d'Aventure !"
            "Vous êtes un aventurier audacieux, qui s'est aventuré dans un vieux château abandonné en pleine forêt."
            "Le château a été laissé à l'abandon depuis des siècles, et des rumeurs parlent de trésors cachés et de secrets oubliés."
            "Alors que vous explorez le château, vous vous retrouvez perdu dans ses couloirs sombres et labyrinthiques. "
            "Test"
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
            "Un liquide rouge y tourbillonne mystérieusement. Vous avez trouvé une potion de vie ! Elle pourrait vous être utile plus tard."
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
        "inventory_items": "Vous ouvrez votre sac et inspectez vos possessions :\n{items}",
        "regarder_inventaire_valide" : "Vous ouvrez votre sac et inspectez vos possessions :",
        "regarder_inventaire_invalide" : "Votre inventaire est vide. Peut-être devriez-vous explorer davantage...",
        "visited_cuisine" : "Vous retournez dans la cuisine. Elle est désormais silencieuse et vide. \nLe sol est encore marqué par les traces du combat précédent.",
        "scène_cuisine": (
            "Vous poussez une porte grinçante et entrez dans ce qui semble être une cuisine."
            "L'odeur de nourriture rance flotte dans l'air, mélangée à celle de bois brûlé."
            "Des étagères croulent sous des ustensiles rouillés, et un chaudron abandonné repose au centre."
            "Alors que vous vous avancez prudemment, une ombre furtive surgit !"
            "Un gobelin malingre, armé d'un couteau de cuisine rouillé, vous bloque le passage."
            "Le gobelin montre les crocs et crie : 'Personne ne vole MES provisions !'"
        ),
        "combat_victory_cuisine": "Après un combat acharné, le gobelin s'effondre en grognant. Le calme revient dans la pièce.\nVous explorez rapidement la cuisine et trouvez des provisions et un couteau de cuisine.\nVous ajoutez les provisions et le couteau à votre inventaire.",
        "scène_couloir" : (
            "Vous entrez dans un couloir sombre et lugubre. Les murs sont ornés de portraits anciens, mais quelque chose cloche."
            "Les tableaux sont mal alignés et un étrange frisson parcourt votre échine."
            "Alors que vous avancez prudemment, vous remarquez un vieux livre posé à terre. La couverture semble usée, mais le titre est encore lisible : *'L'Ordre des Âges'.*"
            "Vous ramassez le livre et l'ouvrez. Une phrase attire votre attention :"
            "\"Dans le grand cycle, l'enfant vient avant le guerrier, mais après le vieillard. Le roi se tient toujours entre eux.\""
            "En levant les yeux, vous remarquez que les tableaux représentent :"
            "1. Un enfant avec un jouet"
            "2. Un roi en pleine gloire"
            "3. Un vieillard tenant une canne"
            "4. Un guerrier avec une épée"
        ),
        "scène_couloir_visited" : "Juste le couloir vide ou vous avez résolu les énigmes",
        "question_tableau" : "Voulez-vous regarder de plus près les tableaux? (oui/non) > ",
        "tableau_sensation" : "Vous sentez que réaligner les tableaux dans le bon ordre pourrait révéler quelque chose de caché.",
        "demande_enigme" : "Voulez-vous regarder de plus près les tableaux? (oui/non) > ",
        "enigme_non" : (
            "Vous décidez de ne pas résoudre l'énigme pour le moment."
            "Vous continuez à avancer dans le couloir, en ignorant les tableaux mal alignés."
            "Vous sentez une légère brise venant d'un autre passage. Vous décidez de vous y diriger."
        )

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
