import json
from indices_widgets import *

class JsonHandler():
    def __init__(self):
        self.name = "JsonHandler"
        '''
        self.parent = parent
        self.setText("Save/Load JSON")
        self.clicked.connect(self.onClicked)
        '''

    def createJson(self, entities, secondaryEntities, indices):
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
        

        # Enregistrement des indices
        indice_list = []
        for ind in indices:
            indice_data = {
                "nomIndice": ind.getIndice(),
                "contraintes": []
            }
            for cont in ind.contraintes_manager.contraintes:
                contrainte = {
                    "lvalue": cont.lvalue.currentText(),
                    "equal": cont.operation.currentText() == "==",
                    "rvalue": cont.rvalue.currentText()
                }
                indice_data["contraintes"].append(contrainte)
            indice_list.append(indice_data)

        problem["problem"]["indices"] = indice_list
        return problem
      


    def loadFromFile(self,json_file):
        with open(json_file, 'r', encoding='utf-8') as file:
            return json.load(file)

    def loadConstraintsFromFile(self, json_file):
        data = self.loadFromFile(json_file)  # Chargement du fichier JSON
        problem = data['problem']  # Accéder au dictionnaire sous la clé 'problem'
        contraintes = []
        principale_key = None

        # Identifier la clé de l'entité principale
        for categorie, details in problem.items():
            if categorie != "indices" and "intitule" in details and details["intitule"] == "principale":
                principale_key = categorie
                break

        # Si une entité principale a été trouvée, la traiter en premier
        if principale_key:
            details = problem[principale_key]
            options = [champ["nom"] for champ in details["champs"].values()]
            contraintes.append((principale_key, options))

        # Traiter les autres catégories
        for categorie, details in problem.items():
            if categorie != "indices" and categorie != principale_key:  # Ignorer les indices et l'entité principale déjà traitée
                options = list(details.get("champs", {}).values())
                contraintes.append((categorie, options))

        return contraintes




    def loadCluesFromFiles(self, json_file):
        data = self.loadFromFile(json_file) 
        problem = data['problem'] 
        indicesSolved = []
        indices = []
        if "indices" in problem:  # Vérifier si 'indices' existe pour éviter KeyError
            for indice in problem["indices"]:
                indiceSolving = IndiceSolving()
                nomIndice = indice["nomIndice"]
                indiceSolving.text = nomIndice
                contraintes = []
                for contrainte in indice["contraintes"]:
                    lvalue = contrainte["lvalue"]
                    equal = contrainte["equal"]
                    rvalue = contrainte["rvalue"]
                    relation = "=" if equal else "!="
                    contraintes.append(f"{lvalue} {relation} {rvalue}")
                
                #indices.append(f"{nomIndice}: {' & '.join(contraintes)}")
                indices.append(f"{nomIndice}")
                
                indiceSolving.contraintes = contraintes
                indicesSolved.append(indiceSolving)

        else:
            print("Aucun indice trouvé dans le fichier JSON.")
        return indicesSolved
    

        