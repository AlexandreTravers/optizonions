import json
from dataObjects.Entity import Entity
from dataObjects.Field import Field
from dataObjects.Solution import Solution
from game.Game import Game


class JsonConverter:
    def __init__(self, game):
        self.game = game

    def to_json(self):
        game_dict = {
            "entities": [],
            "solution": self.game.solution.matrix if self.game.solution else None
        }

        for entity in self.game.entities:
            entity_dict = {
                "name": entity.name,
                "fields": [field.name for field in entity.fields]
            }
            game_dict["entities"].append(entity_dict)

        return json.dumps(game_dict, indent=4)

    def to_json_file(self):
        with open(self.game.name + "_data.json", "w") as json_file:
            json.dump({
                "name": self.game.name,
                "entities": [{
                    "name": entity.name,
                    "fields": [field.name for field in entity.fields]
                } for entity in self.game.entities],
                "solution": self.game.solution.matrix if self.game.solution else None
            }, json_file, indent=4, separators=(',', ':'))

    def from_json_file(self, filename):
        with open(filename, "r") as json_file:
            game_data = json.load(json_file)

        entities = []
        for entity_data in game_data["entities"]:
            name = entity_data["name"]
            fields = [Field(field_name) for field_name in entity_data["fields"]]
            entities.append(Entity(name, fields))

        game_name = game_data.get("name", "Unnamed game")
        game = Game(entities, game_name)

        # Charger la solution si elle existe dans le fichier JSON
        solution_data = game_data.get("solution")
        if solution_data:
            entity_count = len(entities)
            field_count = len(entities[0].fields) if entities else 0
            solution = Solution(entity_count, field_count)
            solution.matrix = solution_data
            game.set_solution(solution)

        self.game = game
        return game
