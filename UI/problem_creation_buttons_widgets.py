from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import stylesheets
import fonts


class GenerateProblemButton(QPushButton):
    def __init__(self, parent):
        super(GenerateProblemButton, self).__init__()
        self.parent = parent
        self.setMinimumSize(256, 60)
        self.setMaximumSize(256, 60)
        self.setText("Générer problème")
        self.setFont(fonts.Fonts().mainFontBold())
        self.setStyleSheet(stylesheets.MainStylesheets().getProblemButtonStylesheet())

        self.mousePressEvent = self.generateProblem

    def generateProblem(self, event):
        self.parent.generateProblem()

class AddEntiteButton(QPushButton):
    def __init__(self, parent):
        super(AddEntiteButton, self).__init__()
        self.parent = parent
        self.setMinimumSize(192, 60)
        self.setMaximumSize(192, 60)
        self.setText("Ajouter entite")
        self.setFont(fonts.Fonts().mainFontBold())
        self.setStyleSheet(stylesheets.MainStylesheets().getProblemButtonStylesheet())

        self.mousePressEvent = self.addEntite

    def addEntite(self, event):
        self.parent.addEntite()

class AddvaleurButton(QPushButton):
    def __init__(self, parent):
        super(AddvaleurButton, self).__init__()
        self.parent = parent        
        self.setMinimumSize(192, 60)
        self.setMaximumSize(192, 60)
        self.setText("Ajouter valeur")
        self.setFont(fonts.Fonts().mainFontBold())
        self.setStyleSheet(stylesheets.MainStylesheets().getProblemButtonStylesheet())

        self.mousePressEvent = self.addValeur

    def addValeur(self, event):
        self.parent.addValeur()


class ValeurManagerButton(QWidget):
    def __init__(self, parent, text, add_func, del_func):
        super(ValeurManagerButton, self).__init__()
        self.parent = parent
        layout = QHBoxLayout()
        self.delButton = QtyButton(self, "-", del_func)
        self.descButton = QPushButton()
        self.descButton.setMinimumSize(192, 60)
        self.descButton.setMaximumSize(192, 60)
        self.descButton.setText(text)
        self.descButton.setFont(fonts.Fonts().mainFontBold())
        self.descButton.setStyleSheet(stylesheets.MainStylesheets().getProblemButtonStylesheet())
        self.addButton = QtyButton(self, "+", add_func)

        layout.addWidget(self.delButton)
        layout.addWidget(self.descButton)
        layout.addWidget(self.addButton)
        self.setLayout(layout)

class QtyButton(QPushButton):
    def __init__(self, parent, text, func):
        super(QtyButton, self).__init__()
        self.parent = parent
        self.setMinimumSize(60, 60)
        self.setMaximumSize(60, 60)
        self.setText(text)
        self.setFont(fonts.Fonts().mainFontBold())
        self.setStyleSheet(stylesheets.MainStylesheets().getProblemButtonStylesheet())
        self.mousePressEvent = func



class CheckSolvabiliteButton(QPushButton):
    def __init__(self, parent):
        super(CheckSolvabiliteButton, self).__init__()
        self.parent = parent
        self.setMinimumSize(192, 60)
        self.setMaximumSize(192, 60)
        self.setText("Check solutions")
        self.setFont(fonts.Fonts().mainFontBold())
        self.setStyleSheet(stylesheets.MainStylesheets().getProblemButtonStylesheet())

        self.mousePressEvent = self.addValeur

    def checkSolvabilite(self, event):
        self.parent.checkSolvabilite


