from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from problem_creation_widgets import *
from problem_solving_widgets import *
from zebra_solving_widgets import *
from main_menu_widgets import *
from json_handler import *
import problem_generator
import json
import os
import re



class ProblemWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setStyleSheet("background-color: rgba(250,220,155,255); ") 
        self.setWindowTitle("OPTIZONIONS - Des problemes et des solutions")

        
        
        ##contraintes = [("Prenom", ["Martin", "Alexandre", "Marc", "Louis"]), ("Lettre", ["A", "B", "C", "D"]), 
        ##               ("Chiffre", ["1", "2", "3", "4"]), ("Couleur", ["Rouge", "Bleu", "Vert", "Jaune"]),
        ##               ("Vetement", ["Pull", "Polo", "Jean", "Cargo"]), ("Nationalite", ["EN", "FR", "AL", "ES"])
        ##              ]
        #contraintes = [("Prenom", ["Martin", "Alexandre", "Marc", "Louis"]), ("Lettre", ["A", "B", "C", "D"]), 
        #               ("Chiffre", ["1", "2", "3", "4"]), ("Couleur", ["Rouge", "Bleu", "Vert", "Jaune"]),
        #               ("Vetement", ["Pull", "Polo", "Jean", "Cargo"])]
        contraintes = [("Nationalite", ["Anglais", "Francais", "Allemand", "Espagnol"]), ("Lettre", ["A", "B", "C", "D"]), 
                       ("Chiffre", ["1", "2", "3", "4"]), ("Couleur", ["Rouge", "Bleu", "Vert", "Jaune"])]
        
        #contraintes = [("Nationalite", ["Anglais", "Francais", "Allemand", "Espagnol"]), ("Lettre", ["A", "B", "C", "D"]), 
        #               ("Chiffre", ["1", "2", "3", "4"])]
        #indices = ["Anglais - A", "1 - Rouge", "B - 2", "A - Jaune",
        #           "Anglais - A", "1 - Rouge", "B - 2", "A - Jaune",
        #           "Anglais - A", "1 - Rouge", "B - 2", "A - Jaune",
        #           "Anglais - A", "1 - Rouge", "B - 2", "A - Jaune",
        #           "Anglais - A", "1 - Rouge", "B - 2", "A - Jaune",
        #           "Anglais - A", "1 - Rouge", "B - 2", "A - Jaune"]
        #jsonFile = "../jsonFiles/MonJison.json"
        #jsonH = JsonHandler()  
        #contraintes = jsonH.loadConstraintsFromFile(jsonFile)
        #indices = jsonH.loadCluesFromFiles(jsonFile)

        #mainWidget = problem_generator.ProblemGenerator().CreateProblem(self, contraintes, indices)
        #GridSolvingWidget(self, contraintes, indices)
        #mainWidget = ZebraSolvingWidget(self, contraintes, indices)
        #mainWidget = ProblemCreationWidget(self)
        mainWidget = MainMenu(self)
        self.mainWidget = mainWidget
        self.container_layout = QHBoxLayout()
        #self.mainWidget = None

        #self.initProblemCreation()
        container = QWidget()
        self.container_layout.addWidget(self.mainWidget)
        self.container_layout.setAlignment(Qt.AlignTop)
        container.setLayout(self.container_layout)

        self.setCentralWidget(container)

        self.show()

    def startPremadeProblem(self, num_probleme):
        print(num_probleme)
        jsonFile = "";
        if(num_probleme ==1):
            jsonFile = self.importerNormal("New_Pc.json")
        if(num_probleme ==2):
            jsonFile = self.importerNormal("Al_Pacino.json")
        if(num_probleme ==3):
            jsonFile = self.importerNormal("Pasta.json")
        else:
            print("Problème normal non existant")

        if jsonFile != "":
            jsonH = JsonHandler()
            contraintes = jsonH.loadConstraintsFromFile(jsonFile)
            indices = jsonH.loadCluesFromFiles(jsonFile)
            mainWidget = problem_generator.ProblemGenerator().CreateProblem(self, contraintes, indices, num_probleme)
            self.mainWidget = mainWidget
            self.container_layout = QHBoxLayout()
            #self.mainWidget = None

            #self.initProblemCreation()
            container = QWidget()
            self.container_layout.addWidget(self.mainWidget)
            self.container_layout.setAlignment(Qt.AlignTop)
            container.setLayout(self.container_layout)

            self.setCentralWidget(container)

            self.show()


    def initProblemCreation(self):
        for i in range(self.container_layout.count()): 
            self.container_layout.itemAt(i).widget().setParent(None) 
        if self.mainWidget != None:
            self.mainWidget.destroy()
        mainWidget = ProblemCreationWidget(self)
        self.mainWidget = mainWidget

        # Créer un menu bar
        self.menubar = self.menuBar()
        self.menubar.setStyleSheet("QMenuBar { background-color: #F3F3F3; } QAction:hover { color: black; background-color:blue; }")
        # Créer un menu "Fichier"
        self.file_menu = self.menubar.addMenu('Fichier')
        self.file_menu.setStyleSheet("QMenu { background-color:#F3F3F3; } QAction:hover { color: black; background-color:blue; }")

        # Créer une action "Importer"
        import_action = HoverableQWidgetAction(self, "Importer un probleme en JSON", self.importer)
        self.file_menu.addAction(import_action)

        # Créer une action "Exporter"
        export_action = HoverableQWidgetAction(self, "Exporter un probleme en JSON", self.exporter)
        self.file_menu.addAction(export_action)

        self.container_layout.addWidget(self.mainWidget)
    
    def initSolving(self):
        print("Go initSOlving")
        jsonH = JsonHandler()  
        jsonFile = self.importer()
        if jsonFile != "":
            contraintes = jsonH.loadConstraintsFromFile(jsonFile)
            indices = jsonH.loadCluesFromFiles(jsonFile)
            indexContraintes = []
            print(contraintes)
            for i in indices:
                for c in i.contraintes:
                    element1, element2 = self.extraire_elements(c)
                    print(c)
                    print(self.trouver_indices(element1,element2,contraintes))
                    indexContraintes.append(self.trouver_indices(element1,element2,contraintes))
            
                i.indexContraintes = indexContraintes
                print(i.text)
                print(i.indexContraintes)
                
            mainWidget = problem_generator.ProblemGenerator().CreateProblem(self, contraintes, indices, -1)
            self.mainWidget = mainWidget
            self.container_layout = QHBoxLayout()
            #self.mainWidget = None

            #self.initProblemCreation()
            container = QWidget()
            self.container_layout.addWidget(self.mainWidget)
            self.container_layout.setAlignment(Qt.AlignTop)
            container.setLayout(self.container_layout)

            self.setCentralWidget(container)

            self.show()
        else :
            print("Pas de fichier trouvé")


    def extraire_elements(self,phrase):
        
        elements = re.split(r' = | != ', phrase)
        return elements[0], elements[1] if len(elements) == 2 else (None, None)
        
    def trouver_indices(self, element1, element2, contraintes):

        index_entite1 = index_element1 = index_entite2 = index_element2 = None
        

        for index_entite, (entite, elements) in enumerate(contraintes):
            if element1 in elements:
                index_entite1, index_element1 = index_entite, elements.index(element1)
            if element2 in elements:
                index_entite2, index_element2 = index_entite, elements.index(element2)
        
        if None not in [index_entite1, index_element1, index_entite2, index_element2]:
            return [index_entite1, index_element1], [index_entite2, index_element2]
        else:
            return None
        
    def importer(self):
        print("Action Importer triggered")
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly

        current_dir = os.path.dirname(__file__)
        parent_dir = os.path.dirname(current_dir)
        file_name, _ = QFileDialog.getOpenFileName(self, "Sélectionnez un fichier JSON", parent_dir, "JSON Files (*.json);;Tous les fichiers (*)", options=options)

        if file_name:
            print(f"Chemin du fichier JSON sélectionné : {file_name}")
            return file_name
        else:
            return ""
        
    import os

    def importerNormal(self, jsonName):
        print("Action ImporterNormal triggered")
        
        current_dir = os.path.dirname(__file__)
        parent_dir = os.path.dirname(current_dir)
        json_files_dir = os.path.join(parent_dir, "jsonFiles")
        
        json_file_path = os.path.join(json_files_dir, jsonName)
        
        if os.path.isfile(json_file_path):
            print(f"Chemin du fichier JSON sélectionné : {json_file_path}")
            return json_file_path
        else:
            print(f"Le fichier JSON spécifié n'existe pas : {json_file_path}")
            return ""


    def exporter(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Enregistrer le fichier", "", "Tous les fichiers (*);;Text Files (*.txt)", options=options)
        problem = self.mainWidget.exportProblemToJSON()
        if file_name:
            with open(file_name, 'w') as f:
                json.dump(problem, f, indent=4)



    def switchToSolving(self, contraintes, indices):
        self.menubar.destroy()
        print(contraintes)
        mainWidget = GridSolvingWidget(self, contraintes, indices, 4)
        self.mainWidget = mainWidget

        container = QWidget()
        container_layout = QHBoxLayout()
        container_layout.addWidget(self.mainWidget)
        container_layout.setAlignment(Qt.AlignTop)
        container.setLayout(container_layout)

        self.setCentralWidget(container)

        self.show()

class HoverableQWidgetAction(QWidgetAction):
    def __init__(self, parent, text, func):
        super(HoverableQWidgetAction, self).__init__(parent)
        #self.parent = parent
        self.action_text = QLabel(text)
        self.action_text.setStyleSheet("QLabel { background-color : #F3F3F3; color : black; padding : 2px 20px 2px 20px; font-size:14px }")
        self.setDefaultWidget(self.action_text)
        self.triggered.connect(func)


        self.action_text.installEventFilter(self)
        
    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.Enter:
            self.action_text.setStyleSheet("QLabel { background-color : #0366D6; color : white; padding : 2px 20px 2px 20px; font-size:14px}")

        elif event.type() == QtCore.QEvent.Leave:
            self.action_text.setStyleSheet("QLabel { background-color : #F3F3F3; color : black; padding : 2px 20px 2px 20px; font-size:14px}")

        return super(HoverableQWidgetAction, self).eventFilter(obj, event)