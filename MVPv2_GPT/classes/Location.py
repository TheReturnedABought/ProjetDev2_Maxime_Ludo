class Location:
    def __init__(self, name, sub_locations=None):
        self.name = name
        self.sub_locations = sub_locations if sub_locations else {}  # sous-lieux possibles

    def interact(self):
        print(f"Vous interagissez avec {self.name}.")

    def add_sub_location(self, location_name, location):
        self.sub_locations[location_name] = location
