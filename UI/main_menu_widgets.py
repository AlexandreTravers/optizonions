from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from enum import Enum
import stylesheets
import fonts

from indices_widgets import *
from problem_creation_buttons_widgets import *


class MainMenu(QWidget):
    def __init__(self, parent):
        super(MainMenu, self).__init__()
        self.parent = parent
        layout = QVBoxLayout()

        window_label = QLabel()
        window_label.setText("Optizonions")
        window_label.setAlignment(Qt.AlignCenter)
        window_label.setFont(fonts.Fonts().titleFont())
        window_label.setStyleSheet("QLabel{font-size:256px;color:#422206;}")

        layout.addStretch(1)
        layout.addWidget(window_label)
        layout.addStretch(1)
        layout.addWidget(SplitMenu(self))
        layout.addStretch(1)

        self.setLayout(layout)

    def initProblemCreation(self):
        self.parent.initProblemCreation()

    def initSolving(self):
        self.parent.initSolving()

class SplitMenu(QWidget):
    def __init__(self, parent):
        super(SplitMenu, self).__init__()
        self.parent = parent
        self.layout = QHBoxLayout()
        self.layout.addStretch(1)
        self.layout.addWidget(PremadeProblemsMenu(self))
        self.layout.addStretch(1)
        self.layout.addWidget(CustomProblemsMenu(self))
        self.layout.addStretch(1)
        self.setLayout(self.layout)

    def initProblemCreation(self):
        self.parent.initProblemCreation()

    def initSolving(self):
        self.parent.initSolving()

class PremadeProblemsMenu(QWidget):
    def __init__(self, parent):
        super(PremadeProblemsMenu, self).__init__()
        self.parent = parent
        self.layout = QVBoxLayout()
        menu_label = QLabel()
        menu_label.setText("Problèmes préfaits")
        menu_label.setStyleSheet("QLabel{font-size:72px;color:#422206;}")
        menu_label.setFont(fonts.Fonts().subtitleFont())

        self.layout.addWidget(menu_label)

        pc = PremadeProblemButton(self, "A New PC", 1)
        movies = PremadeProblemButton(self, "Movie Buffs", 2)
        zebre = PremadeProblemButton(self, "Pasta & Wine", 3)

        self.layout.addWidget(pc)
        self.layout.addWidget(movies)
        self.layout.addWidget(zebre)
        self.layout.addStretch(1)
        self.setLayout(self.layout)

class PremadeProblemButton(QWidget):
    def __init__(self, parent, nom_probleme, num_probleme):
        super(PremadeProblemButton, self).__init__()
        self.parent = parent
        self.layout = QHBoxLayout()

        self.label = QLabel()
        self.label.setText(nom_probleme)
        self.label.setStyleSheet("QLabel{font-size:48px;color:#422206;}")
        self.label.setFont(fonts.Fonts().mainFont())
        
        self.num_probleme = num_probleme
        
        self.startButton = QPushButton()
        self.startButton.setText("Démarrer")
        self.startButton.setMinimumSize(QSize(256, 60))
        self.startButton.setMaximumSize(QSize(256, 60))
        self.startButton.setStyleSheet(stylesheets.MainStylesheets().getProblemButtonStylesheet())
        self.startButton.setFont(fonts.Fonts().mainFontBold())
        self.startButton.mousePressEvent = self.startProblem

        self.layout.addStretch(1)
        self.layout.addWidget(self.label)
        self.layout.addStretch(1)
        self.layout.addWidget(self.startButton)
        self.setLayout(self.layout)
    
    def startProblem(self, event):
        self.parent.startPremadeProblem(self.num_probleme)

class CustomProblemsMenu(QWidget):
    def __init__(self, parent):
        super(CustomProblemsMenu, self).__init__()
        self.parent = parent
        self.layout = QVBoxLayout()
        menu_label = QLabel()
        menu_label.setText("Problèmes personnalisés")
        menu_label.setStyleSheet("QLabel{font-size:72px;color:#422206;}")
        menu_label.setFont(fonts.Fonts().subtitleFont())

        self.layout.addWidget(menu_label)

        custom_problem_creation = CustomProblemButton(self, "Créer problème", self.initProblemCreation)
        custom_problem_solving = CustomProblemButton(self, "Résoudre problème", self.initSolving)
        
        self.layout.addWidget(custom_problem_creation)
        self.layout.addWidget(custom_problem_solving)
        self.layout.addStretch(1)
        self.setLayout(self.layout)

    def initProblemCreation(self, event):
        self.parent.initProblemCreation()

    def initSolving(self, event):
        self.parent.initSolving()

class CustomProblemButton(QWidget):
    def __init__(self, parent, nom_option, func):
        super(CustomProblemButton, self).__init__()
        self.parent = parent
        self.layout = QHBoxLayout()

        self.label = QLabel()
        self.label.setText(nom_option)
        self.label.setStyleSheet("QLabel{font-size:48px;color:#422206;}")
        self.label.setFont(fonts.Fonts().mainFont())

        self.button = QPushButton()
        self.button.setText("Démarrer")
        self.button.setMinimumSize(QSize(256, 60))
        self.button.setMaximumSize(QSize(256, 60))
        self.button.setStyleSheet(stylesheets.MainStylesheets().getProblemButtonStylesheet())
        self.button.setFont(fonts.Fonts().mainFontBold())

        self.button.mousePressEvent = func

        self.layout.addStretch(1)
        self.layout.addWidget(self.label)
        self.layout.addStretch(2)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)