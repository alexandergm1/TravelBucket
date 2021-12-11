class Country:
    def __init__(self, name, continent, visited = False, id = None):
        self.name = name
        self.continent = continent
        self.visited = visited
        self.id = id


    def mark_visited(self):
        self.visited = True