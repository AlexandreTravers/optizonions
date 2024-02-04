from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import stylesheets
import state
from modeles.mainSolver import ObjetMatrice
import fonts


class ZebraSolvingWidget(QWidget):
    def __init__(self, parent, contraintes, indices, numPb):
        super(ZebraSolvingWidget, self).__init__()

        self.parent = parent
        self.layout = QVBoxLayout()


        zebre = Zebre(self, contraintes, numPb)
        indices_widget = IndicesWidget(self, indices)
        self.layout.addWidget(zebre)
        self.layout.addWidget(indices_widget)
        self.setLayout(self.layout)
    

class Zebre(QWidget):
    def __init__(self, parent, contraintes, numPb):
        super(Zebre, self).__init__() 
        self.parent = parent
        
        layout = QHBoxLayout()
        self.entites = []

        noms = []
        for c in contraintes:
            noms.append(c[0])
        cz = ContraintesZebre(self, noms)
        layout.addWidget(cz)

        for e in contraintes[0][1]:
            z = EntiteZebre(self, e, contraintes[1:])
            self.entites.append(z)
            layout.addWidget(z)
        
        self.check_button = CheckButton(self, numPb)
        layout.addWidget(self.check_button)

        self.setLayout(layout)

    def allEntitesToMatrix(self):
        matrix = []
        for e in self.entites:
            matrix.append(e.toMatrix())

        grid_matrix = []
        for i in range (len(matrix[0])):
            mini_grid_matrix = []
            for m in matrix:
                mini_grid_matrix.append(m[i])
            grid_matrix.append(mini_grid_matrix)

        
        for m in grid_matrix:
            for m_ in m:
                print(f"{m_}\n")
            print("\n")
        return matrix
    
    def stateToString(self, s):
        if s == state.State.NONE:
            return "NONE"
        elif s == state.State.TRUE:
            return "TRUE"
        elif s == state.State.FALSE:
            return "FALSE"

        
class ContraintesZebre(QWidget):
    def __init__(self, parent, noms_contraintes):
        super(ContraintesZebre, self).__init__()
        self.parent = parent
        layout = QVBoxLayout()
        self.contraintes = []
        for nc in noms_contraintes:
            label = QLabel()
            label.setText(nc)
            label.setStyleSheet("QLabel{font-size:20px}")
            label.setFont(fonts.Fonts().mainFontBold())

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
        self.label_entite.setText(nom_entite)
        self.label_entite.setStyleSheet("QLabel{font-size:20px}")
        self.label_entite.setFont(fonts.Fonts().mainFontBold())
        layout.addWidget(self.label_entite)

        self.boxes = []
        for c in contraintes:
            box = QComboBox()
            box.addItem("?")
            box.setStyleSheet(stylesheets.MainStylesheets().getComboboxStylesheet())
            box.setFont(fonts.Fonts().mainFontBold())
            for c_ in c[1]:
                box.addItem(c_)
            self.boxes.append(box)
            layout.addWidget(box)        
        self.setLayout(layout)

    def toMatrix(self):
        #contraintes = (self.nom_contrainte1, self.nom_contrainte2)
        
        matrixes = []
        for box in self.boxes:
            matrix = []
            for val in [box.itemText(i) for i in range(1, box.count())]:
                if box.currentText() == "?":
                    matrix.append(state.State.NONE)
                elif val == box.currentText() and val != "?":
                    matrix.append(state.State.TRUE)
                else:
                    matrix.append(state.State.FALSE)            
            matrixes.append(matrix)
        
        #print(f"MATRICE : {self.nom_contrainte1} X {self.nom_contrainte2}")
        return matrixes
        #return contraintes, matrix
        
        
class CheckButton(QPushButton):
    def __init__(self, parent, numPb):
        super(CheckButton, self).__init__()
        self.parent = parent
        self.numPb = numPb

        self.setMinimumSize(QSize(192, 60))
        self.setMaximumSize(QSize(192, 60))
        
        self.mousePressEvent = self.checkSolution
        self.setText("Check solution")
        self.setFont(fonts.Fonts().mainFontBold())
        self.setStyleSheet(stylesheets.MainStylesheets().getProblemButtonStylesheet())

    def checkSolution(self, event):
        print("CHECK SOLUTION\n\n")
        grids = self.parent.allEntitesToMatrix()
        matrix = []
        allIsMarked = True
        print("grids : ")
        for i in grids:
            print(i)
            oneR = []
            for j in i:
                oneM = []
                for elts in j:
                    if (elts == 'NONE'):
                        oneM.append(0)
                        allIsMarked = False
                    elif (elts == 'FALSE'):
                        oneM.append(-1)
                    elif (elts == 'TRUE'):
                        oneM.append(1)
                if (len(oneM) > 0):
                    oneR.append(oneM)
            if (len(oneR) > 0):
                matrix.append(oneR)
        print(matrix)
        resultat = ObjetMatrice(matrix, self.numPb).getResult()
        resultat.append(allIsMarked)
        print(resultat)
        print("CHECK SOLUTION\n\n")
        self.parent.changeIndicesColors(resultat)
        


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
            indice.setStyleSheet("QLabel{font:20px;}")
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