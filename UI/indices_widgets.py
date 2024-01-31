from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import stylesheets

class IndiceCreator(QWidget):
    def __init__(self, parent):
        super(IndiceCreator, self).__init__()
        self.parent = parent
        self.layout = QHBoxLayout()
        label = QLabel()
        label.setText("Indice :")
        label.setStyleSheet("QLabel{font:20px;}")
        self.indice = QTextEdit()
        self.indice.setMinimumHeight(40)
        self.indice.setMaximumHeight(40)
        self.indice.setMinimumWidth(500)
        self.indice.setMaximumWidth(500)
        self.indice.setAlignment(Qt.AlignVCenter)
        self.indice.setStyleSheet(stylesheets.MainSpritesheets().getTextEditStylesheet())

        self.add_bouton = QPushButton()

        self.add_bouton.setMinimumSize(256, 40)
        self.add_bouton.setMaximumSize(256, 40)
        self.add_bouton.setText("Ajouter indice")
        self.add_bouton.setStyleSheet(stylesheets.MainSpritesheets().getProblemManagerButton())

        self.add_bouton.mousePressEvent = self.addIndice

        self.label_valide = QLabel()
        self.label_valide.setText("")
        self.label_valide.setStyleSheet("QLabel{font:20px;}")


        self.layout.addWidget(label)
        self.layout.addWidget(self.indice)
        self.layout.addWidget(self.add_bouton)
        self.layout.addWidget(self.label_valide)
        self.layout.addStretch(1)
        self.setLayout(self.layout)
    
    def addIndice(self, event):
        self.parent.addIndice(self.indice.toPlainText())

    def setIndiceValide(self, valide):
        if valide:
            self.label_valide.setText("")
        else:
            self.label_valide.setText("Indice déjà existant !")

class IndicesDisplay(QWidget):
    def __init__(self, parent):
        super(IndicesDisplay, self).__init__()
        self.layout = QVBoxLayout()
        self.parent = parent

        self.scroll = QScrollArea(self)
        self.layout.addWidget(self.scroll)
        self.scroll.setWidgetResizable(True)
        self.scroll_content = QWidget(self.scroll)

        self.scroll_layout = QVBoxLayout(self.scroll_content)
        self.scroll_layout.setAlignment(Qt.AlignTop)
        self.scroll_content.setLayout(self.scroll_layout)
        self.scroll.setWidget(self.scroll_content)
        self.scroll.setStyleSheet(stylesheets.MainSpritesheets().getScrollerStylesheet())
        
        self.setLayout(self.layout)

    def addIndice(self, indice):
        self.scroll_layout.addWidget(indice)


    def generateIndices(self):
        indices = []
        for i in reversed(range(self.scroll_layout.count())): 
            indices.append(self.scroll_layout.itemAt(i).widget().getIndice())
        return indices

    def reset(self, indices):
        for i in reversed(range(self.scroll_layout.count())):
            self.scroll_layout.itemAt(i).widget().setParent(None)

        for i in indices:
            self.addIndice(i)

class Indice(QWidget):
    def __init__(self, parent, indice_text, valeurs):
        super(Indice, self).__init__()
        self.parent = parent
        self.layout = QHBoxLayout()
        self.indice_text = indice_text
        label = QLabel()
        label.setText(self.indice_text)
        label.setStyleSheet("QLabel{font:15px;}")

        self.contraintes_manager = ContraintesManager(self, valeurs)
        
        self.remove_bouton = QPushButton()
        self.remove_bouton.setMinimumSize(30, 30)
        self.remove_bouton.setMaximumSize(30, 30)
        self.remove_bouton.setText("-")
        self.remove_bouton.setStyleSheet(stylesheets.MainSpritesheets().getProblemManagerButton())
        self.remove_bouton.mousePressEvent = self.removeIndice

        self.layout.addWidget(self.remove_bouton)
        self.layout.addWidget(label)
        self.layout.addWidget(self.contraintes_manager)
        self.layout.addStretch(1)
        self.setLayout(self.layout)

    def removeIndice(self, event):
        self.parent.removeIndice(self)

    def getIndice(self):
        return self.indice_text
    
    def updateValeurs(self, valeurs):
        self.contraintes_manager.updateContraintes(valeurs)
        
class ContraintesManager(QWidget):
    def __init__(self, parent, valeurs):
        super(ContraintesManager, self).__init__()
        self.parent = parent
        self.layout = QHBoxLayout()
        self.valeurs = valeurs

        self.contraintes = []
        self.contraintes.append(Contrainte(self, self.valeurs))
        self.layout.addWidget(self.contraintes[0])

        self.setLayout(self.layout)

    def addContrainte(self):
        self.contraintes.append(Contrainte(self, self.valeurs))
        self.layout.addWidget(self.contraintes[len(self.contraintes) - 1])

    def removeContrainte(self, contrainte):
        for i in range (0, len(self.contraintes) - 1):
            if contrainte == self.contraintes[i]:
                del self.contraintes[i + 1]
                self.layout.itemAt(i + 1).widget().setParent(None)

    def isLastContrainte(self, contrainte):
        for i in range (0, len(self.contraintes)):
            if contrainte == self.contraintes[i]:
                return i == len(self.contraintes) - 1

    def updateContraintes(self, valeurs):
        self.valeurs = valeurs
        for c in self.contraintes:
            c.updateValeurs(valeurs)

class Contrainte(QWidget):
    def __init__(self, parent, valeurs):
        super(Contrainte, self).__init__()
        self.parent = parent
        self.has_next = False
        self.layout = QHBoxLayout()
        self.lvalue = QComboBox()
        self.lvalue.setStyleSheet(stylesheets.MainSpritesheets().getComboboxStylesheet())
        self.lvalue.setMinimumHeight(30)
        self.lvalue.setMaximumHeight(30)
        self.lvalue.setMinimumWidth(120)
        self.lvalue.setMaximumWidth(120)
        self.lvalue.clear()
        self.lvalue.addItem("?")
        for v in valeurs:
            self.lvalue.addItem(v)

        self.operation = QComboBox()
        self.operation.setStyleSheet(stylesheets.MainSpritesheets().getComboboxStylesheet())
        self.operation.setMinimumHeight(30)
        self.operation.setMaximumHeight(30)
        self.operation.setMinimumWidth(120)
        self.operation.setMaximumWidth(120)
        self.operation.clear()
        self.operation.addItem("==")
        self.operation.addItem("!=")

        self.rvalue = QComboBox()
        self.rvalue.setStyleSheet(stylesheets.MainSpritesheets().getComboboxStylesheet())
        self.rvalue.setMinimumHeight(30)
        self.rvalue.setMaximumHeight(30)
        self.rvalue.setMinimumWidth(120)
        self.rvalue.setMaximumWidth(120)
        self.rvalue.clear()
        self.rvalue.addItem("?")
        for v in valeurs:
            self.rvalue.addItem(v)

        self.layout.addWidget(self.lvalue)
        self.layout.addWidget(self.operation)
        self.layout.addWidget(self.rvalue)

        self.add_bouton = QPushButton()
        self.add_bouton.setMinimumSize(30, 30)
        self.add_bouton.setMaximumSize(30, 30)
        self.add_bouton.setText("+")
        self.add_bouton.setStyleSheet(stylesheets.MainSpritesheets().getProblemManagerButton())
        self.add_bouton.mousePressEvent = self.addContrainte
        self.layout.addWidget(self.add_bouton)
        self.setLayout(self.layout)


    def addContrainte(self, event):
        if not self.has_next:
            if event.button() == Qt.LeftButton:
                self.add_bouton.setMinimumSize(50, 30)
                self.add_bouton.setMaximumSize(50, 30)
                self.add_bouton.setText("ET")
                self.parent.addContrainte()
                self.has_next = True
        else:
            if event.button() == Qt.MiddleButton:
                self.parent.removeContrainte(self)
                if self.parent.isLastContrainte(self):
                    self.add_bouton.setMinimumSize(30, 30)
                    self.add_bouton.setMaximumSize(30, 30)
                    self.add_bouton.setText("+")
                    self.has_next = False

    def updateValeurs(self, valeurs):
        for i in range (0, len(valeurs)):
            if(valeurs[i] != self.lvalue.itemText(i)):
                self.lvalue.setItemText(i + 1, valeurs[i])
            if(valeurs[i] != self.rvalue.itemText(i)):
                self.rvalue.setItemText(i + 1, valeurs[i])
            if i + 1 >= len(self.lvalue):
                self.lvalue.addItem(valeurs[i])
            if i + 1 >= len(self.rvalue):
                self.rvalue.addItem(valeurs[i])


class VerbeEntite(QWidget):
    def __init__(self, parent):
        super(VerbeEntite, self).__init__()
        self.parent = parent
        self.layout_indice = QHBoxLayout()
        label_indice = QLabel()
        label_indice.setText("Verbe indice")
        label_indice.setStyleSheet("QLabel{font:16px;}")
        self.entite_indice = QTextEdit()
        self.entite_indice.setMinimumHeight(40)
        self.entite_indice.setMaximumHeight(40)
        self.entite_indice.setMinimumWidth(100)
        self.entite_indice.setMaximumWidth(100)
        self.entite_indice.setAlignment(Qt.AlignVCenter)
        self.entite_indice.setStyleSheet(stylesheets.MainSpritesheets().getTextEditStylesheet())
        self.entite_indice.setText("Action")
        self.entite_indice.textChanged.connect(self.modifSelfVerbe)        
        self.layout_indice.addWidget(label_indice)
        self.layout_indice.addWidget(self.entite_indice)
        self.layout_indice.addStretch(1)
        self.setLayout(self.layout_indice)

    def verbe(self):
        return self.entite_indice.toPlainText()

    def modifSelfVerbe(self):
        self.parent.modifSelfVerbe(self.verbe())



class ValeursEntiteMere(QWidget):
    def __init__(self, parent, index_entite, verbe, valeurs_indices):
        super(ValeursEntiteMere, self).__init__()
        self.parent = parent        
        self.index_reference = index_entite
        self.layout_indice = QHBoxLayout()
        self.label_indice = QLabel()
        self.label_indice.setText(verbe)
        self.label_indice.setStyleSheet("QLabel{font:16px;}")
        self.entite_indice = QComboBox()
        self.entite_indice.setStyleSheet(stylesheets.MainSpritesheets().getComboboxStylesheet())
        self.entite_indice.setMinimumHeight(30)
        self.entite_indice.setMaximumHeight(30)
        self.entite_indice.setMinimumWidth(120)
        self.entite_indice.setMaximumWidth(120)
        self.entite_indice.clear()
        self.entite_indice.addItem("?")
        for val_i in valeurs_indices:
            self.entite_indice.addItem(val_i)
    
        self.layout_indice.setContentsMargins(50, 0, 0, 0)
        self.layout_indice.addWidget(self.label_indice)
        self.layout_indice.addWidget(self.entite_indice)
        self.layout_indice.addStretch(1)
        self.setLayout(self.layout_indice)

    def currentValeur(self):
        return self.entite_indice.currentText()
    
    def updateVerbe(self, verbe):
        self.label_indice.setText(verbe)

    def updateValeurs(self, valeurs):
        self.entite_indice.clear()
        self.entite_indice.addItem("?")
        for val_i in valeurs:
            self.entite_indice.addItem(val_i)
