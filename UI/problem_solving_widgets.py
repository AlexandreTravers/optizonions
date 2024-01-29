from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from enum import Enum
import stylesheets

class ProblemSolvingWidget(QWidget):
    def __init__(self, parent, contraintes, indices):
        super(ProblemSolvingWidget, self).__init__()

        self.parent = parent
        self.layout = QVBoxLayout()


        grid = Grid(self, contraintes, indices)
        self.layout.addWidget(grid)
        self.setLayout(self.layout)
    

class Grid(QWidget):
    def __init__(self, parent, contraintes, indices):
        super(Grid, self).__init__() 
        self.parent = parent
        
        grid_layout = QGridLayout()
        self.grids = []
        pb1 = ProblemGrid(self, contraintes[0], contraintes[1])
        pb2 = ProblemGrid(self, contraintes[0], contraintes[2], has_left_grid = True)
        pb3 = ProblemGrid(self, contraintes[3], contraintes[1], has_top_grid = True)
        self.grids.append(pb1)
        self.grids.append(pb2)
        self.grids.append(pb3)
        grid_layout.addWidget(pb1, 0, 0)
        grid_layout.addWidget(pb2, 0, 1)
        grid_layout.addWidget(pb3, 1, 0)
        

        self.pos_label = QLabel()
        grid_layout.addWidget(self.pos_label, 2, 2)

        self.indices_widget = IndicesWidget(self, indices)
        grid_layout.addWidget(self.indices_widget, 3, 2)

        self.check_button = CheckButton(self)
        grid_layout.addWidget(self.check_button, 4, 2)

        self.setLayout(grid_layout)

    def updatePosLabel(self, row, col):
        self.pos_label.setText(f"({row},{col})")

    def allGridsToMatrix(self):
        grids = []
        for g in self.grids:
            grids.append(g.toMatrix())

        return grids
        


class ProblemGrid(QWidget):
    def __init__(self, parent, contrainte1, contrainte2, has_left_grid = False, has_top_grid = False):
        super(ProblemGrid, self).__init__()
        self.parent = parent
        self.buttons = []
        self.nom_contrainte1 = contrainte1[0]
        self.nom_contrainte2 = contrainte2[0]
        self.contrainte1 = contrainte1
        self.contrainte2 = contrainte2
        self.rows = len(contrainte1)
        self.cols = len(contrainte2)
        self.authorize_simulation = True

        grid_layout = QGridLayout()
        for j in range(0, len(contrainte1)):
            if not has_left_grid:
                label_contrainte_1 = QLabel()
                label_contrainte_1.setText(contrainte1[1][j])
                grid_layout.addWidget(label_contrainte_1, j + 1, 0)
            for k in range(0, len(contrainte2)):
                if not has_top_grid:
                    label_contrainte_2 = QLabel()
                    label_contrainte_2.setText(contrainte2[1][k])
                    grid_layout.addWidget(label_contrainte_2, 0, k + 1)

                button = GridButton(self, k + 1, j + 1)
                self.buttons.append(button)
                grid_layout.addWidget(button, k + 1, j + 1)

        print(f"{len(self.buttons)}")
        self.setLayout(grid_layout)

    
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
        self.authorize_simulation = False
        for b in self.buttons:
            if (b.row == button.row and not b.col == button.col) or (not b.row == button.row and b.col == button.col) :
                if state:
                    b.simulateState(False)
                else:
                    b.clear()
                    b.resetLabel()
        self.authorize_simulation = True

    def checkRow(self, button):
        for b in self.buttons:
            if b.col != button.col and b.row == button.row:
                if b.state == State.TRUE:
                    for b_ in self.buttons:
                        if b_.row != b.row and b_.col == b.col:
                            b_.clear(clear_state=True)
                else:
                    b.clear(clear_state=True)

    def checkCol(self, button):
        for b in self.buttons:
            if b.col == button.col and b.row != button.row:
                if b.state == State.TRUE:
                    for b_ in self.buttons:
                        if b_.row == b.row and b_.col != b.col:
                            b_.clear(clear_state=True)
                else:
                    b.clear(clear_state=True)


    def updatePosLabel(self, row, col):
        self.parent.updatePosLabel(row, col)    

    def toMatrix(self):
        contraintes = (self.nom_contrainte1, self.nom_contrainte2)
        
        matrix = []
        for i in range(0, self.rows):
            matrix_row = []
            for j in range(0, self.cols):
                matrix_row.append(self.buttons[i * self.cols + j].stateToString())
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
        self.setStyleSheet(stylesheets.ProblemCreationSpriteSheets().getProblemManagerButton())

    def checkSolution(self, event):
        print("CHECK SOLUTION\n\n")
        grids = self.parent.allGridsToMatrix()
        print("CHECK SOLUTION\n\n")
        

class GridButton(QPushButton):
    def __init__(self, parent, row, col, round_type = stylesheets.GridButtonType.NORMAL):
        super(GridButton, self).__init__()
        self.parent = parent
        self.row = row
        self.col = col

        self.setMinimumSize(QSize(50, 50))
        self.setMaximumSize(QSize(50, 50))

        self.updateTimer = QTimer(self)
        self.updateTimer.setSingleShot(True)
        self.updateTimer.timeout.connect(self.handleUpdate)
        self.pendingState = None

    
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
                if self.parent.authorize_simulation:
                    self.pendingState = True
                    self.startTimer()
                    #self.simulateState(True)
                    #self.parent.simulateAll(self, True)
                    self.updatePosLabel(self.row, self.col)

            elif event.type() == QtCore.QEvent.HoverLeave:
                self.pendingState = False
                self.startTimer()
                self.clear()
                #self.parent.simulateAll(self, False)
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


    def startTimer(self):
        if not self.updateTimer.isActive():
            self.updateTimer.start(10)  # 100 ms delay

    def handleUpdate(self):
        if self.pendingState is not None:
            if self.pendingState:
                self.simulateState(True)
                self.parent.simulateAll(self, True)
            else:
                self.clear()
                self.parent.simulateAll(self, False)
            self.updatePosLabel(self.row, self.col)
            self.pendingState = None


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

    def clear(self, clear_state = False):
        if clear_state:
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
        self.sim_Label = HoverableQLabel(self)
        if(simulated):
            self.sim_Label.setStyleSheet(stylesheets.GridButtonStylesheets().getSimulatedLabelStylesheet())        
            self.sim_Label.setText(text)
            self.sim_Label.setAlignment(Qt.AlignCenter)
            self.layout().removeWidget(self.label)
            self.layout().removeWidget(self.sim_Label)
            self.layout().addWidget(self.sim_Label, alignment=Qt.AlignCenter)
        else:    
            self.label.setStyleSheet(stylesheets.GridButtonStylesheets().getLabelStylesheet())        
            self.label.setText(text)
            self.label.setAlignment(Qt.AlignCenter)
            self.layout().removeWidget(self.label)
            self.layout().removeWidget(self.sim_Label)
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
        self.scroll.setStyleSheet(stylesheets.ProblemCreationSpriteSheets().getScrollerStylesheet())
        self.setLayout(self.layout)




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