from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from enum import Enum
import stylesheets

class ProblemSolvingWidget(QWidget):
    def __init__(self, parent):
        super(ProblemSolvingWidget, self).__init__()

        self.parent = parent
        self.layout = QVBoxLayout()

        contraintes = [["Anglais", "Francais", "Allemand", "Espagnol"], ["A", "B", "C", "D"], 
                       ["1", "2", "3", "4"], ["Rouge", "Bleu", "Vert", "Jaune"]]
        grid = Grid(self, contraintes)
        self.layout.addWidget(grid)

        self.setLayout(self.layout)

    

class Grid(QWidget):
    def __init__(self, parent, contraintes):
        super(Grid, self).__init__() 
        self.parent = parent
        
        gridLayout = QGridLayout()

        pb1 = ProblemGrid(self, contraintes[0], contraintes[1])
        pb2 = ProblemGrid(self, contraintes[0], contraintes[2], hasLeftGrid = True)
        pb3 = ProblemGrid(self, contraintes[3], contraintes[1], hasTopGrid = True)
        
        gridLayout.addWidget(pb1, 0, 0)
        gridLayout.addWidget(pb2, 0, 1)
        gridLayout.addWidget(pb3, 1, 0)
        
        self.posLabel = QLabel()
        gridLayout.addWidget(self.posLabel, 2,2)


        self.setLayout(gridLayout)

    def updatePosLabel(self, row, col):
        self.posLabel.setText(f"({row},{col})")
        

class ProblemGrid(QWidget):
    def __init__(self, parent, contrainte1, contrainte2, hasLeftGrid = False, hasTopGrid = False):
        super(ProblemGrid, self).__init__()
        self.parent = parent
        self.buttons = []
        self.rows = len(contrainte1)
        self.cols = len(contrainte2)

        gridLayout = QGridLayout()
        for j in range(0, len(contrainte1)):
            if not hasLeftGrid:
                labelContrainte1 = QLabel()
                labelContrainte1.setText(contrainte1[j])
                gridLayout.addWidget(labelContrainte1, j + 1, 0)
            for k in range(0, len(contrainte2)):
                if not hasTopGrid:
                    labelContrainte2 = QLabel()
                    labelContrainte2.setText(contrainte2[k])
                    gridLayout.addWidget(labelContrainte2, 0, k + 1)

                button = GridButton(self, k + 1, j + 1)
                self.buttons.append(button)
                gridLayout.addWidget(button, k + 1, j + 1)

        print(f"{len(self.buttons)}")
        self.setLayout(gridLayout)

    
    def setButtonState(self, button, state):
        if state == State.FALSE or state == State.NONE:
            for b in self.buttons:
                if (b.row == button.row and not b.col == button.col) or (not b.row == button.row and b.col == button.col) :
                    b.clear()
                    b.manualSwitchState(State.NONE)

        elif state == State.TRUE:
            self.checkRow(button)
            self.checkCol(button)
            for b in self.buttons:
                if (b.row == button.row and not b.col == button.col) or (not b.row == button.row and b.col == button.col):
                    b.manualSwitchState(State.FALSE)

        self.toMatrix()
                    
    def simulateAll(self, button, state):
        for b in self.buttons:
            if (b.row == button.row and not b.col == button.col) or (not b.row == button.row and b.col == button.col) :
                if state:
                    b.simulateState(False)
                else:
                    b.clear()
                    b.resetLabel()

    def checkRow(self, button):
        for b in self.buttons:
            if b.col != button.col and b.row == button.row:
                if b.state == State.TRUE:
                    for b_ in self.buttons:
                        if b_.row != b.row and b_.col == b.col:
                            b_.clear(clearState=True)
                else:
                    b.clear(clearState=True)

    def checkCol(self, button):
        for b in self.buttons:
            if b.col == button.col and b.row != button.row:
                if b.state == State.TRUE:
                    for b_ in self.buttons:
                        if b_.row == b.row and b_.col != b.col:
                            b_.clear(clearState=True)
                else:
                    b.clear(clearState=True)


    def updatePosLabel(self, row, col):
        self.parent.updatePosLabel(row, col)    

    def toMatrix(self):
        matrix = []
        for i in range(0, self.rows):
            matrixRow = []
            for j in range(0, self.cols):
                matrixRow.append(self.buttons[i * self.cols + j].stateToString())
            matrix.append(matrixRow)
        
        for m in matrix: 
            print(f"\n{m}")
        
        


class GridButton(QPushButton):
    def __init__(self, parent, row, col, round_type = stylesheets.GridButtonType.NORMAL):
        super(GridButton, self).__init__()
        self.parent = parent
        self.row = row
        self.col = col

        self.setMinimumSize(QSize(50, 50))
        self.setMaximumSize(QSize(50, 50))
    
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        self.state = State.NONE
        self.setLayout(layout)
        self.installEventFilter(self)
        self.setStyleSheet(stylesheets.GridButtonStylesheets().getStylesheetForType(round_type))

        self.mousePressEvent = self.switchState
        

    def eventFilter(self, obj, event):
        if obj == self and self.state == State.NONE:
            if event.type() == QtCore.QEvent.HoverEnter:
                self.simulateState(True)
                self.parent.simulateAll(self, True)
                self.updatePosLabel(self.row, self.col)

            elif event.type() == QtCore.QEvent.HoverLeave:
                self.clear()
                self.parent.simulateAll(self, False)
                self.updatePosLabel(0, 0)

        return super(QPushButton, self).eventFilter(obj, event)


    def switchState(self, event): 
        self.clear()
        text = ""
        if event.button() == Qt.LeftButton:
                self.state = State.TRUE
                text = "V"
                self.parent.setButtonState(self, self.state)
        elif event.button() == Qt.RightButton:
                self.state = State.FALSE
                text = "X"
                self.parent.setButtonState(self, self.state)       
        elif event.button() == Qt.MiddleButton:
            self.state = State.NONE
            text = ""

        self.createLabel(text, False)


    def manualSwitchState(self, state):
        self.clear()
        self.state = state
        if self.state == State.NONE:
            return

        text = ""
        if state == State.TRUE:
                text = "V"
        else:
                text = "X"
        self.createLabel(text, False)


    def simulateState(self, tick):
        self.clear()
        if tick: 
            text = "V"
        else:
            text = "X"
        self.createLabel(text, True)

    def clear(self, clearState = False):
        if clearState:
            self.state = State.NONE

        for i in reversed(range(self.layout().count())): 
            self.layout().itemAt(i).widget().setParent(None)

    def resetLabel(self):
        if self.state == State.TRUE:
            self.createLabel("V", False)
        if self.state == State.FALSE:
            self.createLabel("X", False)

    def createLabel(self, text, simulated):
        self.label = HoverableQLabel(self)
        self.simLabel = HoverableQLabel(self)
        if(simulated):
            self.simLabel.setStyleSheet(stylesheets.GridButtonStylesheets().getSimulatedLabelStylesheet())        
            self.simLabel.setText(text)
            self.simLabel.setAlignment(Qt.AlignCenter)
            self.layout().removeWidget(self.label)
            self.layout().removeWidget(self.simLabel)
            self.layout().addWidget(self.simLabel, alignment=Qt.AlignCenter)
        else:    
            self.label.setStyleSheet(stylesheets.GridButtonStylesheets().getLabelStylesheet())        
            self.label.setText(text)
            self.label.setAlignment(Qt.AlignCenter)
            self.layout().removeWidget(self.label)
            self.layout().removeWidget(self.simLabel)
            self.layout().addWidget(self.label, alignment=Qt.AlignCenter)
        

    def updatePosLabel(self, row, col):
        self.parent.updatePosLabel(row, col)

    def stateToString(self):
        if self.state == State.NONE:
            return "NONE"
        elif self.state == State.TRUE:
            return "TRUE"
        elif self.state == State.FALSE:
            return "FALSE"


class HoverableQLabel(QLabel):
    def __init__(self, parent):
        super(HoverableQLabel, self).__init__()
        self.parent = parent
        self.installEventFilter(self)
    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.Enter:
            self.parent.updatePosLabel(self.parent.row, self.parent.col)

        elif event.type() == QtCore.QEvent.Leave:
            self.parent.updatePosLabel(0, 0)

        return super(QLabel, self).eventFilter(obj, event)


class State(Enum):
    NONE = 0
    TRUE = 1
    FALSE = 2



class VerticalLabel(QWidget):
    def __init__(self):
        super(VerticalLabel, self).__init__()
    
    def setText(self, text):
        self.text = text

    def paintEvent(self):
        painter = QtGui.QPainter(self)
        painter.setPen(QtCore.Qt.black)
        painter.translate(20, 100)
        painter.rotate(-90)
        painter.drawText(0, 0, self.text)
        painter.end()




class ProblemCreationWidget(QWidget):
    def __init__(self, parent):
        super(ProblemCreationWidget, self).__init__()
        self.parent = parent
        self.layout = QVBoxLayout()

        windowLabel = QLabel()
        windowLabel.setText("TU VEUX UN PROBLEME ?")
        windowLabel.setStyleSheet("QLabel{font-size:72px}")
        self.layout.addWidget(windowLabel)
        self.entites = EntiteWidgets(self)
        self.layout.addWidget(self.entites)
        self.quantityWidget = QuantityWidget(self)
        self.layout.addWidget(self.quantityWidget)
        self.layout.setAlignment(Qt.AlignLeft)
        self.setLayout(self.layout)

    def addValeur(self):
        self.entites.addValeur()

    def addEntite(self):
        self.entites.addEntite()

class QuantityWidget(QWidget):
    def __init__(self, parent):
        super(QuantityWidget, self).__init__()
        self.parent = parent

        self.layout = QHBoxLayout()

        self.layout.addStretch(1)
        self.valeurButton = AddValeurButton(self)
        self.layout.addWidget(self.valeurButton)
        self.entiteButton = AddEntiteButton(self)
        self.layout.addWidget(self.entiteButton)
        
        self.setLayout(self.layout)

    def addValeur(self):
        self.parent.addValeur()

    def addEntite(self):
        self.parent.addEntite()

class EntiteWidgets(QWidget):
    def __init__(self, parent):
        super(EntiteWidgets, self).__init__()
        self.parent = parent

        self.valeurQty = 1

        self.entites = []
        entite = CreationEntite(self, self.valeurQty)
        self.entites.append(entite)

        self.layout = QHBoxLayout(self)
        self.setLayout(self.layout)

        self.scroll = QScrollArea(self)
        self.layout.addWidget(self.scroll)
        self.scroll.setWidgetResizable(True)
        self.scrollContent = QWidget(self.scroll)

        self.scrollLayout = QHBoxLayout(self.scrollContent)
        self.scrollLayout.setAlignment(Qt.AlignTop)
        self.scrollContent.setLayout(self.scrollLayout)
        for entite in self.entites:
            self.scrollLayout.addWidget(entite)
        self.scroll.setWidget(self.scrollContent)
        self.scroll.setStyleSheet(stylesheets.MainStylesheets().getScrollerStylsheet())
        self.setLayout(self.layout)

    def addEntite(self):
        newEntite = CreationEntite(self, self.valeurQty)
        self.entites.append(newEntite)
        self.scrollLayout.addWidget(self.entites[len(self.entites) - 1])


    def addValeur(self):
        self.valeurQty += 1
        for e in self.entites:
            e.addValeurChamp()

class CreationEntite(QWidget):
    def __init__(self, parent, valeurs):
        super(CreationEntite, self).__init__()
        self.parent = parent
        self.layout = QVBoxLayout()
        
        self.valeurs = []
        self.layout.addStretch(1)

        label = QLabel()
        label.setText("Entite")
        self.entiteNom = QTextEdit()
        self.entiteNom.setMinimumHeight(40)
        self.entiteNom.setMaximumHeight(40)
        self.entiteNom.setMinimumWidth(300)
        self.entiteNom.setMaximumWidth(300)
        self.entiteNom.setAlignment(Qt.AlignVCenter)
        self.entiteNom.setStyleSheet(stylesheets.MainStylesheets().getTextEditStylesheet())
        
        self.layout.addWidget(label)
        self.layout.addWidget(self.entiteNom)
        for i in range (0, valeurs):
            valeur = CreationValeur(self)
            self.valeurs.append(valeur)
            self.layout.addWidget(self.valeurs[i])
        self.layout.setAlignment(Qt.AlignCenter)
 
        
        self.setLayout(self.layout)        


    def addValeur(self):
        self.parent.addValeur()

    def addValeurChamp(self):
        valeur1 = CreationValeur(self)
        self.valeurs.append(valeur1)
        self.layout.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.valeurs[len(self.valeurs) - 1])
        


class CreationValeur(QWidget):
    def __init__(self, parent):
        super(CreationValeur, self).__init__()
        self.parent = parent
        self.layout = QHBoxLayout()
        label = QLabel()
        label.setText("Champ")
        self.textEdit = QTextEdit()
        self.textEdit.setMinimumHeight(40)
        self.textEdit.setMaximumHeight(40)
        self.textEdit.setMinimumWidth(400)
        self.textEdit.setMaximumWidth(400)
        self.textEdit.setAlignment(Qt.AlignVCenter)

        self.textEdit.setStyleSheet(stylesheets.MainStylesheets().getTextEditStylesheet())
        self.layout.addWidget(label)
        self.layout.addWidget(self.textEdit)
        self.layout.addStretch(1)
        self.setLayout(self.layout)

    def addValeur(self):
        self.parent.addValeur()


class AddEntiteButton(QPushButton):
    def __init__(self, parent):
        super(AddEntiteButton, self).__init__()
        self.parent = parent        
        self.setMinimumSize(256, 64)
        self.setMaximumSize(256, 64)
        self.setText("Ajouter entite")
        self.setStyleSheet(stylesheets.MainStylesheets().getProblemButtonStylesheet())

        self.mousePressEvent = self.addEntite

    def addEntite(self, event):
        self.parent.addEntite()

class AddValeurButton(QPushButton):
    def __init__(self, parent):
        super(AddValeurButton, self).__init__()
        self.parent = parent        
        self.setMinimumSize(256, 64)
        self.setMaximumSize(256, 64)
        self.setText("Ajouter valeur")
        self.setStyleSheet(stylesheets.MainStylesheets().getProblemButtonStylesheet())

        self.mousePressEvent = self.addValeur

    def addValeur(self, event):
        self.parent.addValeur()
