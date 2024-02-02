from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from enum import Enum
import stylesheets

class ZebraSolvingWidget(QWidget):
    def __init__(self, parent, contraintes, indices):
        super(ZebraSolvingWidget, self).__init__()

        self.parent = parent
        self.layout = QVBoxLayout()


        grid = Grid(self, contraintes)
        indices_widget = IndicesWidget(self, indices)
        self.layout.addWidget(grid)
        self.layout.addWidget(indices_widget)
        self.setLayout(self.layout)
    

class Grid(QWidget):
    def __init__(self, parent, contraintes):
        super(Grid, self).__init__() 
        self.parent = parent
        
        layout = QHBoxLayout()
        self.entites = []

        noms = []
        for c in contraintes:
            noms.append(c[0])
        cz = ContraintesZebre(self, noms)
        layout.addWidget(cz)

        print(contraintes[1])
        for e in contraintes[0][1]:
            z = EntiteZebre(self, e, contraintes[1:])
            layout.addWidget(z)
        
        self.check_button = CheckButton(self)
        layout.addWidget(self.check_button)

        self.setLayout(layout)

    def allEntitesToMatrix(self):
        matrix = []
        for e in self.entites:
            matrix.append(e.toMatrix())

        return matrix
        
class ContraintesZebre(QWidget):
    def __init__(self, parent, noms_contraintes):
        super(ContraintesZebre, self).__init__()
        self.parent = parent
        layout = QVBoxLayout()
        self.contraintes = []
        for nc in noms_contraintes:
            label = QLabel()
            label.setText(nc)
            #label.setStyleSheet()
            self.contraintes.append(label)
        for c in self.contraintes:
            layout.addWidget(c)
        self.setLayout(layout)

class EntiteZebre(QWidget):
    def __init__(self, parent, nom_entite, contraintes):
        super(EntiteZebre, self).__init__()
        self.parent = parent
        layout = QVBoxLayout()
        self.label_entite = QLabel()
        print(nom_entite)
        self.label_entite.setText(nom_entite)
        layout.addWidget(self.label_entite)

        self.boxes = []
        for c in contraintes:
            box = QComboBox()
            box.setStyleSheet(stylesheets.MainStylesheets().getComboboxStylesheet())
            for c_ in c[1]:
                box.addItem(c_)
            layout.addWidget(box)        
        self.setLayout(layout)

    def toMatrix(self):
        contraintes = (self.nom_contrainte1, self.nom_contrainte2)
        
        matrix = []
        for i in range(0, self.rows):
            matrix_row = []
            for j in range(0, self.cols):
                matrix_row.append(self.buttons[j * self.rows + i].stateToString())
            matrix.append(matrix_row)
        
        print(f"MATRICE : {self.nom_contrainte1} X {self.nom_contrainte2}")
        for m in matrix:
            print(f"\n{m}")

        return contraintes, matrix
        
        
class CheckButton(QPushButton):
    def __init__(self, parent):
        super(CheckButton, self).__init__()
        self.parent = parent

        self.setMinimumSize(QSize(192, 48))
        self.setMaximumSize(QSize(192, 48))
        
        self.mousePressEvent = self.checkSolution
        self.setText("Check solution")
        self.setStyleSheet(stylesheets.MainStylesheets().getProblemButtonStylesheet())

    def checkSolution(self, event):
        print("CHECK SOLUTION\n\n")
        grids = self.parent.allGridsToMatrix()
        print("CHECK SOLUTION\n\n")
        


class IndicesWidget(QWidget):
    def __init__(self, parent, indices):
        super(IndicesWidget, self).__init__()
        self.parent = parent
        self.layout = QVBoxLayout(self)
        self.setLayout(self.layout)

        self.scroll = QScrollArea(self)
        self.layout.addWidget(self.scroll)
        self.scroll.setWidgetResizable(True)
        self.scroll_content = QWidget(self.scroll)

        self.scroll_layout = QVBoxLayout(self.scroll_content)
        self.scroll_layout.setAlignment(Qt.AlignTop)
        self.scroll_content.setLayout(self.scroll_layout)
        print(indices)
        for i in indices:
            indice = QLabel()
            indice.setStyleSheet("QLabel{font:16px;}")
            indice.setText(i)
            self.scroll_layout.addWidget(indice)            
            """for i_ in i:
                if len(i_) > 0:
                    indice = QLabel()
                    indice.setStyleSheet("QLabel{font:16px;}")
                    indice.setText(i_[0])
                    self.scroll_layout.addWidget(indice)"""
        self.scroll.setWidget(self.scroll_content)
        self.scroll.setStyleSheet(stylesheets.MainStylesheets().getScrollerStylesheet())
        self.setLayout(self.layout)