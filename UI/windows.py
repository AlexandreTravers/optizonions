from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from problem_creation_widgets import *
from problem_solving_widgets import *
from zebra_solving_widgets import *
from main_menu_widgets import *
import json

class ProblemWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setStyleSheet("background-color: rgba(240,230,215,255); ") 
        self.setWindowTitle("OPTIZONIONS - Des problemes et des solutions")

        
        
        contraintes = [("Prenom", ["Martin", "Alexandre", "Marc", "Louis"]), ("Lettre", ["A", "B", "C", "D"]), 
                       ("Chiffre", ["1", "2", "3", "4"]), ("Couleur", ["Rouge", "Bleu", "Vert", "Jaune"]),
                       ("Vetement", ["Pull", "Polo", "Jean", "Cargo"]), ("Nationalite", ["EN", "FR", "AL", "ES"])
                       ]
        #contraintes = [("Prenom", ["Martin", "Alexandre", "Marc", "Louis"]), ("Lettre", ["A", "B", "C", "D"]), 
        #               ("Chiffre", ["1", "2", "3", "4"]), ("Couleur", ["Rouge", "Bleu", "Vert", "Jaune"]),
        #               ("Vetement", ["Pull", "Polo", "Jean", "Cargo"])]
        #contraintes = [("Nationalite", ["Anglais", "Francais", "Allemand", "Espagnol"]), ("Lettre", ["A", "B", "C", "D"]), 
        #               ("Chiffre", ["1", "2", "3", "4"]), ("Couleur", ["Rouge", "Bleu", "Vert", "Jaune"])]
        
        #contraintes = [("Nationalite", ["Anglais", "Francais", "Allemand", "Espagnol"]), ("Lettre", ["A", "B", "C", "D"]), 
        #               ("Chiffre", ["1", "2", "3", "4"])]
        indices = ["Anglais - A", "1 - Rouge", "B - 2", "A - Jaune",
                   "Anglais - A", "1 - Rouge", "B - 2", "A - Jaune",
                   "Anglais - A", "1 - Rouge", "B - 2", "A - Jaune",
                   "Anglais - A", "1 - Rouge", "B - 2", "A - Jaune",
                   "Anglais - A", "1 - Rouge", "B - 2", "A - Jaune",
                   "Anglais - A", "1 - Rouge", "B - 2", "A - Jaune"]
        mainWidget = ProblemSolvingWidget(self, contraintes, indices)
        #mainWidget = ZebraSolvingWidget(self, contraintes, indices)
        #mainWidget = ProblemCreationWidget(self)
        #mainWidget = MainMenu(self)
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

    def importer(self):
        print("Action Importer triggered")

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
        mainWidget = ProblemSolvingWidget(self, contraintes, indices)
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