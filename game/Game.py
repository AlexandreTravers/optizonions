class Game():
    def __init__(self, entities, name):
        self.name = name
        self.entities = entities
        self.solution = None

    def set_solution(self, solution):
        self.solution = solution

    def solve(self):
        print("Solve todo")
        # Mettez ici votre code de résolution du jeu