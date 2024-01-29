from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import stylesheets

class IndiceManuelCreator(QWidget):
    def __init__(self, parent):
        super(IndiceManuelCreator, self).__init__()
        self.parent = parent
        self.layout = QHBoxLayout()
        label = QLabel()
        label.setText("Indice Manuel :")
        label.setStyleSheet("QLabel{font:20px;}")
        self.indice = QTextEdit()
        self.indice.setMinimumHeight(40)
        self.indice.setMaximumHeight(40)
        self.indice.setMinimumWidth(500)
        self.indice.setMaximumWidth(500)
        self.indice.setAlignment(Qt.AlignVCenter)
        self.indice.setStyleSheet(stylesheets.ProblemCreationSpriteSheets().getTextEditStylesheet())

        self.add_bouton = QPushButton()

        self.add_bouton.setMinimumSize(256, 40)
        self.add_bouton.setMaximumSize(256, 40)
        self.add_bouton.setText("Ajouter indice")
        self.add_bouton.setStyleSheet(stylesheets.ProblemCreationSpriteSheets().getProblemManagerButton())

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
        self.parent.addIndiceManuel(self.indice.toPlainText())

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
        self.scroll.setStyleSheet(stylesheets.ProblemCreationSpriteSheets().getScrollerStylesheet())
        
        self.setLayout(self.layout)

    def addIndice(self, indice):
        self.scroll_layout.addWidget(indice)

    def generateIndices(self):
        indices = []
        for i in reversed(range(self.scroll_layout.count())): 
            indices.append(self.scroll_layout.itemAt(i).widget().getIndice())
        return indices

    def reset(self, indices):
        for i in reversed(range(self.layout.count())): 
            self.layout.itemAt(i).widget().setParent(None)
        for i in indices:
            self.addIndice(i)

class IndiceManuel(QWidget):
    def __init__(self, parent, indice_text):
        super(IndiceManuel, self).__init__()
        self.parent = parent
        self.layout = QHBoxLayout()
        self.indice_text = indice_text
        label = QLabel()
        label.setText(self.indice_text)
        label.setStyleSheet("QLabel{font:15px;}")

        self.remove_bouton = QPushButton()
        self.remove_bouton.setMinimumSize(25, 25)
        self.remove_bouton.setMaximumSize(25, 25)
        self.remove_bouton.setText("-")
        self.remove_bouton.setStyleSheet(stylesheets.ProblemCreationSpriteSheets().getProblemManagerButton())
        self.remove_bouton.mousePressEvent = self.removeIndiceManuel

        self.layout.addWidget(label)
        self.layout.addWidget(self.remove_bouton)
        self.layout.addStretch(1)
        self.setLayout(self.layout)

    def removeIndiceManuel(self, event):
        self.parent.removeIndiceManuel(self)

    def getIndice(self):
        return self.indice_text
        

class VerbeIndice(QWidget):
    def __init__(self, parent):
        super(VerbeIndice, self).__init__()
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
        self.entite_indice.setStyleSheet(stylesheets.ProblemCreationSpriteSheets().getTextEditStylesheet())
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



class CreationIndice(QWidget):
    def __init__(self, parent, index_entite, verbe, valeurs_indices):
        super(CreationIndice, self).__init__()
        self.parent = parent        
        self.index_reference = index_entite
        self.layout_indice = QHBoxLayout()
        self.label_indice = QLabel()
        self.label_indice.setText(verbe)
        self.label_indice.setStyleSheet("QLabel{font:16px;}")
        self.entite_indice = QComboBox()
        self.entite_indice.setStyleSheet(stylesheets.ProblemCreationSpriteSheets().getComboboxStylesheet())
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

    def indice(self):
        indice = Indice(self.parent.getValeur(), self.label_indice.text(), self.entite_indice.currentText())
        return indice
    
    def updateVerbe(self, verbe):
        self.label_indice.setText(verbe)

    def updateValeurs(self, valeurs):
        self.entite_indice.clear()
        self.entite_indice.addItem("?")
        for val_i in valeurs:
            self.entite_indice.addItem(val_i)

class Indice():
    def __init__(self, valeur, indice, valeur_indice):
        self.valeur = valeur
        self.indice = indice
        self.valeur_indice = valeur_indice

    def showIndice(self):
        return self.valeur + " " + self.indice + " " + self.valeur_indice