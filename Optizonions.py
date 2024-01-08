from dataObjects.Entity import Entity
from dataObjects.Field import Field
from dataObjects.Solution import Solution
from game.Game import Game
from loader.JsonConverter import JsonConverter

field1 = Field("Chien")
field2 = Field("Serpent")
field3 = Field("Souris")
field4 = Field("Chat")
field5 = Field("Elephant")

field6 = Field("Laine")
field7 = Field("Ordinateur")
field8 = Field("Lance-incendie")
field9 = Field("Bloc-note")
field10 = Field("Souris")

Animal = Entity("Animal", [field1, field2, field3, field4, field5])
Objet = Entity("Entity2", [field6, field7, field8, field9, field10])

entities = [Animal, Objet]

Animal.printFields()
solution = Solution(len(entities), len(Animal.fields))
solution.print_solution_matrix()
game = Game(entities, "Chelous")
game.set_solution(solution)
game.solve()

converter = JsonConverter(game)
game_json = converter.to_json()
converter.to_json_file()
print("Game vers JSON")

print(game_json)

game2 = converter.from_json_file("Chelous_data.json")

print("Meme Game Apres chargement")

print(converter.to_json())
