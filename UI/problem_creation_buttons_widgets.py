from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import stylesheets


class GenerateProblemButton(QPushButton):
    def __init__(self, parent):
        super(GenerateProblemButton, self).__init__()
        self.parent = parent
        self.setMinimumSize(192, 48)
        self.setMaximumSize(192, 48)
        self.setText("Générer problème")
        self.setStyleSheet(stylesheets.MainSpritesheets().getProblemManagerButton())

        self.mousePressEvent = self.generateProblem

    def generateProblem(self, event):
        self.parent.generateProblem()

class AddEntiteButton(QPushButton):
    def __init__(self, parent):
        super(AddEntiteButton, self).__init__()
        self.parent = parent
        self.setMinimumSize(192, 48)
        self.setMaximumSize(192, 48)
        self.setText("Ajouter entite")
        self.setStyleSheet(stylesheets.MainSpritesheets().getProblemManagerButton())

        self.mousePressEvent = self.addEntite

    def addEntite(self, event):
        self.parent.addEntite()

class AddvaleurButton(QPushButton):
    def __init__(self, parent):
        super(AddvaleurButton, self).__init__()
        self.parent = parent        
        self.setMinimumSize(192, 48)
        self.setMaximumSize(192, 48)
        self.setText("Ajouter valeur")
        self.setStyleSheet(stylesheets.MainSpritesheets().getProblemManagerButton())

        self.mousePressEvent = self.addValeur

    def addValeur(self, event):
        self.parent.addValeur()

class CheckSolvabiliteButton(QPushButton):
    def __init__(self, parent):
        super(CheckSolvabiliteButton, self).__init__()
        self.parent = parent
        self.setMinimumSize(192, 48)
        self.setMaximumSize(192, 48)
        self.setText("Check solvabilité")
        self.setStyleSheet(stylesheets.MainSpritesheets().getProblemManagerButton())

        self.mousePressEvent = self.addValeur

    def checkSolvabilite(self, event):
        self.parent.checkSolvabilite


