import json


class JsonHandler():
    def __init__(self):
        self.name = "JsonHandler"
        '''
        self.parent = parent
        self.setText("Save/Load JSON")
        self.clicked.connect(self.onClicked)
        '''

    def createJson(self, entities, secondaryEntities):
        problem = {
            "problem": {}
        }

        # Créer un dictionnaire pour les entités secondaires
        secondary_data = {}
        for entite in secondaryEntities:
            champs_dict = {f"champ{i+1}": valeur.getValeur() for i, valeur in enumerate(entite.valeurs)}
            secondary_data[entite.entite_nom.toPlainText()] = {
                "verbe": entite.indice.entite_indice.toPlainText(),
                "champs": champs_dict
            }

        # Ajouter les entités secondaires au problème
        problem["problem"].update(secondary_data)

        # Contraintes pour l'entité principale
        if entities:
            principale = entities[0]
            champs_principale = {}
            for i, champ in enumerate(principale.valeurs):
                # Dictionnaire de contraintes pour chaque champ
                contraintes = {"nom": champ.getValeur()} 
                for key, value in secondary_data.items():
                    contraintes[key] = value["champs"][f"champ{i+1}"]
                champs_principale[f"champ{i+1}"] = contraintes

            problem["problem"][principale.entite_nom.toPlainText()] = {
                "intitule": "principale",
                "champs": champs_principale
            }
        
        return problem
        """filename = 'problem_logique.json'
        with open(filename, 'w') as file:
            json.dump(problem, file, indent=4)"""


    def loadJson(self):

        with open('problem.json', 'r') as file:
            data = json.load(file)

        for entite_nom, entite_data in data["problem"].items():
            pass
        