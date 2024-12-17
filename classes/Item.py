class Item:
    def __init__(self, name, _damage_power, _health_add, slot, equiped = False):
        self.name = name
        self._damage_power = _damage_power
        self._health_add = _health_add
        self.slot = slot #la place qu'il prend dans l'inventaire
        self.equiped = equiped
    def equip(self):
        """
        "équipe" l'item, le marque comme "dans la main" du joueur.

        PRE:
        POST:Si "equiped = False" on le change en vrai. 
            Si il a un slot (le paramètre slot a une valeur tel que main, tête) : L'objet est marqué comme équipé.
        Raise: renvoie une erreur si l'objet est déjà équipé ou si il n'y a aucun objet dans l'inventaire.

        """
        pass

    def unequip(self):
        """
        "Déséquipe" l'item de la main du joueur.
    
    PRE: 
    POST:L'objet n'est plus marqué comme équipé et le paramètre slot prend la valeur None.
    RAISE: RunTimeError si l'objet n'est pas équipé.

        """
        pass

    def examine(self):
        pass

    def use(self):
        pass
