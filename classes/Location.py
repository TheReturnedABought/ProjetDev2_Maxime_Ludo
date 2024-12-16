class Location:
    def __init__(self, name, description, visited=False):
        self.name = name
        self.description = description
        self.visited = visited

    def visit(self):
        if not self.visited:
            print(self.description)
            self.visited = True
        else:
            print(f"Vous êtes déjà passé(e) par {self.name}.")
