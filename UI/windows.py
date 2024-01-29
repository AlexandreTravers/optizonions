from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from problem_creation_widgets import *
from problem_solving_widgets import *

class ProblemWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setStyleSheet("background-color: rgba(240,230,205,255);") 
        self.setWindowTitle("OPTIZONIONS - Des problemes et des solutions")

        contraintes = [["Anglais", "Francais", "Allemand", "Espagnol"], ["A", "B", "C", "D"], 
                       ["1", "2", "3", "4"], ["Rouge", "Bleu", "Vert", "Jaune"]]
        indices = ["Anglais - A", "1 - Rouge", "B - 2", "A - Jaune",
                   "Anglais - A", "1 - Rouge", "B - 2", "A - Jaune",
                   "Anglais - A", "1 - Rouge", "B - 2", "A - Jaune",
                   "Anglais - A", "1 - Rouge", "B - 2", "A - Jaune",
                   "Anglais - A", "1 - Rouge", "B - 2", "A - Jaune",
                   "Anglais - A", "1 - Rouge", "B - 2", "A - Jaune"]
        mainWidget = ProblemSolvingWidget(self, contraintes, indices)
        #mainWidget = ProblemCreationWidget(self)
        self.mainWidget = mainWidget

        container = QWidget()
        container_layout = QHBoxLayout()
        container_layout.addWidget(self.mainWidget)
        container_layout.setAlignment(Qt.AlignTop)
        container.setLayout(container_layout)

        self.setCentralWidget(container)

        self.show()
    
    def switchToSolving(self, contraintes, indices):
        mainWidget = ProblemSolvingWidget(self, contraintes, indices)
        self.mainWidget = mainWidget

        container = QWidget()
        container_layout = QHBoxLayout()
        #container_layout.addStretch(1)
        container_layout.addWidget(self.mainWidget)
        #container_layout.addStretch(1)
        container_layout.setAlignment(Qt.AlignTop)
        container.setLayout(container_layout)

        self.setCentralWidget(container)

        self.show()
