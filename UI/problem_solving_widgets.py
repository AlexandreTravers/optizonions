from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import stylesheets
import state
import fonts

class GridSolvingWidget(QWidget):
    def __init__(self, parent, contraintes, indices):
        super(GridSolvingWidget, self).__init__()

        self.parent = parent
        self.layout = QHBoxLayout()


        self.grid = Grid(self, contraintes, indices)
        self.layout.addWidget(self.grid)
    
        self.utils = UtilsWidget(self, indices)
        self.layout.addWidget(self.utils)
    
        self.setLayout(self.layout)

    def updatePosLabel(self, row, col):
        self.utils.updatePosLabel(row, col)

    def allGridsToMatrix(self):
        self.grid.allGridsToMatrix()

class UtilsWidget(QWidget):
    def __init__(self, parent, indices):
        super(UtilsWidget, self).__init__()
        self.parent = parent
        layout = QVBoxLayout()

        self.pos_label = QLabel()
        self.pos_label.setStyleSheet("QLabel{font-size:16px;}")
        self.pos_label.setFont(fonts.Fonts().mainFontBold())
        self.indices_widget = IndicesWidget(self, indices)
        self.check_button = CheckButton(self)

        layout.addStretch()
        layout.addWidget(self.pos_label)
        layout.addWidget(self.indices_widget)
        layout.addWidget(self.check_button)
        self.setLayout(layout)

    def updatePosLabel(self, row, col):
        self.pos_label.setText(f"({row},{col})")

    def allGridsToMatrix(self):
        self.parent.allGridsToMatrix()

    def changeIndicesColors(self):
        self.indices_widget.changeIndicesColors()    


class Grid(QWidget):
    def __init__(self, parent, contraintes, indices):
        super(Grid, self).__init__() 
        self.parent = parent
        
        grid_layout = QGridLayout()
        self.grids = []
        x = 0
        y = 0

        if len(contraintes) == 2:
            pb1 = ProblemGrid(self, contraintes[0], contraintes[1])
            self.grids.append(pb1)
            grid_layout.addWidget(self.grids[0], 0, 0)

        elif len(contraintes) == 3:
            pb1 = ProblemGrid(self, contraintes[0], contraintes[1])
            self.grids.append(pb1)
            grid_layout.addWidget(self.grids[0], 0, 0)

            pb2 = ProblemGrid(self, contraintes[0], contraintes[2], has_left_grid=True)
            self.grids.append(pb2)
            grid_layout.addWidget(self.grids[1], 0, 1)

            pb3 = ProblemGrid(self, contraintes[1], contraintes[2], has_top_grid=True)
            self.grids.append(pb3)
            grid_layout.addWidget(self.grids[2], 1, 1)

        elif len(contraintes) == 4:
            pb1 = ProblemGrid(self, contraintes[0], contraintes[1])
            self.grids.append(pb1)
            grid_layout.addWidget(self.grids[0], 0, 0)

            pb2 = ProblemGrid(self, contraintes[0], contraintes[2], has_left_grid=True)
            self.grids.append(pb2)
            grid_layout.addWidget(self.grids[1], 0, 1)

            pb3 = ProblemGrid(self, contraintes[0], contraintes[3], has_left_grid=True)
            self.grids.append(pb3)
            grid_layout.addWidget(self.grids[2], 0, 2)

            pb4 = ProblemGrid(self, contraintes[3], contraintes[1], has_top_grid=True)
            self.grids.append(pb4)
            grid_layout.addWidget(self.grids[3], 1, 0)

            pb5 = ProblemGrid(self, contraintes[3], contraintes[2], has_left_grid=True, has_top_grid=True)
            self.grids.append(pb5)
            grid_layout.addWidget(self.grids[4], 1, 1)

            pb6 = ProblemGrid(self, contraintes[2], contraintes[1], has_top_grid=True)
            self.grids.append(pb6)
            grid_layout.addWidget(self.grids[5], 2, 0)

            #Servent à centrer la grille, et occuper la place que la grille 
            #s'amuserait à occuper sinon
            grid_layout.addWidget(QLabel(), 0, 3)
            grid_layout.addWidget(QLabel(), 3, 0)

        self.setLayout(grid_layout)

    def updatePosLabel(self, row, col):
        self.parent.updatePosLabel(row, col)

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
        self.contrainte1 = contrainte1[1]
        self.contrainte2 = contrainte2[1]
        self.rows = len(self.contrainte1)
        self.cols = len(self.contrainte2)
        print(f"ROWS : {self.rows} / COLS : {self.cols}")
        
        self.authorize_simulation = True

        grid_layout = QGridLayout()
        for j in range(0, len(self.contrainte1)):
            if not has_left_grid:
                label_contrainte_1 = QLabel()
                label_contrainte_1.setFont(fonts.Fonts().mainFontBold())
                label_contrainte_1.setText(contrainte1[1][j])
                label_contrainte_1.setStyleSheet("""QLabel{font-size:14px;}""")
                grid_layout.addWidget(label_contrainte_1, j + 1, 0)
            for k in range(0, len(self.contrainte2)):
                if not has_top_grid:
                    label_contrainte_2 = QLabel()
                    label_contrainte_2.setFont(fonts.Fonts().mainFontBold())
                    label_contrainte_2.setText(self.tiltText(contrainte2[1][k]))
                    label_contrainte_2.setAlignment(Qt.AlignBottom)
                    label_contrainte_2.setStyleSheet("""QLabel{font-size:14px;}""")
                    grid_layout.addWidget(label_contrainte_2, 0, k + 1)

                button = GridButton(self, k + 1, j + 1)
                self.buttons.append(button)
                grid_layout.addWidget(button, k + 1, j + 1)

        print(f"{len(self.buttons)}")
        self.setLayout(grid_layout)

    def tiltText(self, text):
        str = text[0]
        for char in text[1:]:
            str += "\n" + char
        return str

    def setButtonState(self, button, button_state, old_true=False):
        if button_state == state.State.FALSE or button_state == state.State.NONE:
            for b in self.buttons:
                if old_true:
                    if (b.row == button.row and not b.col == button.col) or (not b.row == button.row and b.col == button.col):
                        if self.canBeErased(b):
                            b.clear()
                            b.manualSwitchState(state.State.NONE)
                b.clear()
                b.resetLabel()
        elif button_state == state.State.TRUE:
            self.checkRow(button)
            self.checkCol(button)
            for b in self.buttons:
                if (b.row == button.row and not b.col == button.col) or (not b.row == button.row and b.col == button.col):
                    b.manualSwitchState(state.State.FALSE)

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
                if b.state == state.State.TRUE:
                    for b_ in self.buttons:
                        if b_.row != b.row and b_.col == b.col:
                            b_.clear(clear_state=True)
                else:
                    b.clear(clear_state=True)

    def checkCol(self, button):
        for b in self.buttons:
            if b.col == button.col and b.row != button.row:
                if b.state == state.State.TRUE:
                    for b_ in self.buttons:
                        if b_.row == b.row and b_.col != b.col:
                            b_.clear(clear_state=True)
                else:
                    b.clear(clear_state=True)

    def canBeErased(self, button):
        for b in self.buttons:
            if ((b.col != button.col and b.row == button.row) or (b.col == button.col and b.row != button.row)) and b.state == state.State.TRUE:
                return False
        return True

    def updatePosLabel(self, row, col):
        self.parent.updatePosLabel(row, col)    

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
        

class CenteredQLabel(QWidget):
    def __init__(self):
        super(CenteredQLabel, self).__init__()
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter)
        layout = QHBoxLayout()
        layout.addStretch()
        layout.addWidget(self.label)
        layout.addStretch()
        layout.setAlignment(Qt.AlignBottom)
        self.setLayout(layout)

class CheckButton(QPushButton):
    def __init__(self, parent):
        super(CheckButton, self).__init__()
        self.parent = parent

        self.setMinimumSize(QSize(256, 60))
        self.setMaximumSize(QSize(256, 60))
        
        self.mousePressEvent = self.checkSolution
        self.setText("Check solution")
        self.setFont(fonts.Fonts().mainFontBold())
        self.setStyleSheet(stylesheets.MainStylesheets().getProblemButtonStylesheet())

    def checkSolution(self, event):
        print("CHECK SOLUTION\n\n")
        grids = self.parent.allGridsToMatrix()
        self.parent.changeIndicesColors()
        print("CHECK SOLUTION\n\n")
        

class GridButton(QPushButton):
    def __init__(self, parent, row, col, round_type = stylesheets.GridButtonType.NORMAL):
        super(GridButton, self).__init__()
        self.parent = parent
        self.row = row
        self.col = col

        self.setMinimumSize(QSize(40, 40))
        self.setMaximumSize(QSize(40, 40))

        self.updateTimer = QTimer(self)
        self.updateTimer.setSingleShot(True)
        self.updateTimer.timeout.connect(self.handleUpdate)
        self.pendingState = None

    
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        self.state = state.State.NONE
        self.setLayout(layout)
        self.installEventFilter(self)
        self.setStyleSheet(stylesheets.GridButtonStylesheets().getStylesheetForType(round_type))

        self.mousePressEvent = self.switchState
        

    def eventFilter(self, obj, event):
        if obj == self and self.state == state.State.NONE:
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
                self.state = state.State.TRUE
                text = "V"
                self.parent.setButtonState(self, self.state)
        elif event.button() == Qt.RightButton:
                old_true = False
                if self.state == state.State.TRUE:
                    old_true = True
                self.state = state.State.FALSE
                text = "X"
                self.parent.setButtonState(self, self.state, old_true=old_true)
        elif event.button() == Qt.MiddleButton:
            self.state = state.State.NONE
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


    def manualSwitchState(self, button_state):
        self.clear()
        self.state = button_state
        if self.state == state.State.NONE:
            return

        text = ""
        if button_state == state.State.TRUE:
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
            self.state = state.State.NONE

        for i in reversed(range(self.layout().count())): 
            self.layout().itemAt(i).widget().setParent(None)

    def resetLabel(self):
        if self.state == state.State.TRUE:
            self.createLabel("V", False)
        if self.state == state.State.FALSE:
            self.createLabel("X", False)

    def createLabel(self, text, simulated):
        self.label = HoverableQLabel(self)
        self.sim_Label = HoverableQLabel(self)
        if self.layout().itemAt(0) != None:
            self.layout().itemAt(0).widget().setParent(None)
        if(simulated):
            self.sim_Label.setStyleSheet(stylesheets.GridButtonStylesheets().getSimulatedLabelStylesheet())        
            self.sim_Label.setText(text)
            self.sim_Label.setAlignment(Qt.AlignCenter)            
            self.layout().addWidget(self.sim_Label, alignment=Qt.AlignCenter)
        else:    
            self.label.setStyleSheet(stylesheets.GridButtonStylesheets().getLabelStylesheet())        
            self.label.setText(text)
            self.label.setAlignment(Qt.AlignCenter)
            self.layout().addWidget(self.label, alignment=Qt.AlignCenter)
        

    def updatePosLabel(self, row, col):
        self.parent.updatePosLabel(row, col)

    def stateToString(self):
        if self.state == state.State.NONE:
            return "NONE"
        elif self.state == state.State.TRUE:
            return "TRUE"
        elif self.state == state.State.FALSE:
            return "FALSE"


class HoverableQLabel(QLabel):
    def __init__(self, parent):
        super(HoverableQLabel, self).__init__()
        self.parent = parent
        self.setFont(fonts.Fonts().mainFontBold())
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
        self.indices = indices
        self.layout = QVBoxLayout(self)
        self.setLayout(self.layout)

        self.scroll = QScrollArea(self)
        self.layout.addWidget(self.scroll)
        self.scroll.setWidgetResizable(True)
        self.scroll_content = QWidget(self.scroll)

        self.scroll_layout = QVBoxLayout(self.scroll_content)
        self.scroll_layout.setAlignment(Qt.AlignTop)
        self.scroll_content.setLayout(self.scroll_layout)
        for i in self.indices:
            indice = QLabel()
            indice.setStyleSheet(stylesheets.MainStylesheets().getIndiceNeutralStylesheet())
            indice.setFont(fonts.Fonts().mainFontBold())
            indice.setText(i.text)
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

    def changeIndicesColors(self):
        for i in range(0, self.scroll_layout.count()):
            if i % 2 == 0:
                print("PAIR")
                self.scroll_layout.itemAt(i).widget().setStyleSheet(stylesheets.MainStylesheets().getIndiceOkayStylesheet())
            else:
                print("IMPAIR")
                self.scroll_layout.itemAt(i).widget().setStyleSheet(stylesheets.MainStylesheets().getIndiceNotOkayStylesheet())





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