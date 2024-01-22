from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from enum import Enum
import stylesheets

class ProblemCreationWidget(QWidget):
    def __init__(self, parent):
        super(ProblemCreationWidget, self).__init__()
        self.parent = parent
        self.layout = QVBoxLayout()

        window_label = QLabel()
        window_label.setText("TU VEUX UN PROBLEME ?")
        window_label.setStyleSheet("QLabel{font-size:72px}")
        self.layout.addWidget(window_label)
        self.entites = EntiteWidgets(self)
        self.layout.addWidget(self.entites)
        self.quantity_widget = QuantityWidget(self)
        self.layout.addWidget(self.quantity_widget)
        self.layout.setAlignment(Qt.AlignLeft)
        self.setLayout(self.layout)

    def addValeur(self):
        self.entites.addValeur()

    def addEntite(self):
        self.entites.addEntite()

    def generateProblem(self):
        contraintes = self.entites.generateProblem()
        indices = self.entites.generateIndices()
        for i in indices:
            print(i)
        self.parent.switchToSolving(contraintes, indices)


class QuantityWidget(QWidget):
    def __init__(self, parent):
        super(QuantityWidget, self).__init__()
        self.parent = parent

        self.layout = QHBoxLayout()

        self.layout.addStretch(1)
        self.valeur_button = AddvaleurButton(self)
        self.layout.addWidget(self.valeur_button)
        self.entite_button = AddEntiteButton(self)
        self.layout.addWidget(self.entite_button)
        self.problem_generation_button = GenerateProblemButton(self)
        self.layout.addWidget(self.problem_generation_button)
        
        self.setLayout(self.layout)

    def addValeur(self):
        self.parent.addValeur()

    def addEntite(self):
        self.parent.addEntite()

    def generateProblem(self):
        self.parent.generateProblem()


class EntiteWidgets(QWidget):
    def __init__(self, parent):
        super(EntiteWidgets, self).__init__()
        self.parent = parent

        self.valeur_qty = 1

        self.entites = []
        entite = CreationEntite(self, self.valeur_qty)
        self.entites.append(entite)

        self.layout = QHBoxLayout(self)
        self.setLayout(self.layout)

        self.scroll = QScrollArea(self)
        self.layout.addWidget(self.scroll)
        self.scroll.setWidgetResizable(True)
        self.scroll_content = QWidget(self.scroll)

        self.scroll_layout = QHBoxLayout(self.scroll_content)
        self.scroll_layout.setAlignment(Qt.AlignTop)
        self.scroll_content.setLayout(self.scroll_layout)
        for entite in self.entites:
            self.scroll_layout.addWidget(entite)
        self.scroll.setWidget(self.scroll_content)
        self.scroll.setStyleSheet(stylesheets.ProblemCreationSpriteSheets().getScrollerStylesheet())
        self.setLayout(self.layout)

    def addEntite(self):
        entite = CreationEntite(self, self.valeur_qty)
        self.entites.append(entite)
        self.scroll_layout.addWidget(self.entites[len(self.entites) - 1])
        index = len(self.entites) - 1
        for e in self.entites:
            e.addIndice(entite, index)


    def addValeur(self):
        self.valeur_qty += 1
        for e in self.entites:
            e.addValeurChamp()

    def updateValeur(self, entite):
        index = 0
        for e in self.entites:
            if e.entite_nom.toPlainText() == entite.entite_nom.toPlainText():
                break
            index += 1

        for e in self.entites:
            if e.entite_nom.toPlainText() != entite.entite_nom.toPlainText():
                e.updateValeurs(entite.getValeursText(), index)

    def generateIndices(self):
        indices = []
        for e in self.entites:
            indices.append(e.generateIndices())
        return indices
    

    def generateProblem(self):
        problem = []
        for e in self.entites:
            problem.append(e.generateContrainte())
        return problem
    
    
    def modifVerbe(self, entite, verbe):
        index = 0
        for e in self.entites:
            if e.entite_nom.toPlainText() == entite.entite_nom.toPlainText():
                break
            index += 1
        for e in self.entites:
            if e.entite_nom.toPlainText() != entite.entite_nom.toPlainText():
                e.updateVerbe(verbe, index)

        


#############################################
############# ENTITES & VALEURS #############
#############################################

class CreationEntite(QWidget):
    def __init__(self, parent, valeurs):
        super(CreationEntite, self).__init__()
        self.parent = parent
        self.layout = QVBoxLayout()
        
        self.valeurs = []
        self.layout.addStretch(1)

        label = QLabel()
        label.setText("Entite")
        label.setStyleSheet("QLabel{font:16px;}")
        self.entite_nom = QTextEdit()
        self.entite_nom.setMinimumHeight(40)
        self.entite_nom.setMaximumHeight(40)
        self.entite_nom.setMinimumWidth(150)
        self.entite_nom.setMaximumWidth(150)
        self.entite_nom.setAlignment(Qt.AlignVCenter)
        self.entite_nom.setStyleSheet(stylesheets.ProblemCreationSpriteSheets().getTextEditStylesheet())
        
        self.indice = VerbeIndice(self)

        self.layout.addWidget(label)
        self.layout.addWidget(self.entite_nom)
        self.layout.addWidget(self.indice)

        for i in range (0, valeurs):
            valeur = CreationValeur(self, self.parent.entites, i)
            self.valeurs.append(valeur)
            self.layout.addWidget(self.valeurs[i]) 
        
        self.setLayout(self.layout)        


    def addValeur(self):
        self.parent.addValeur()

    def addValeurChamp(self):
        index = len(self.valeurs)
        valeur = CreationValeur(self, self.parent.entites, index)
        self.valeurs.append(valeur)
        self.layout.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.valeurs[index])

    def generateIndices(self):
        indices = []
        for v in self.valeurs:
            indices.append(v.generateIndices())
        return indices

    def generateContrainte(self):
        contrainte = []
        for v in self.valeurs:
            contrainte.append(v.getValeur())
        return contrainte
    
    def getValeursText(self):
        vals = []
        for v in self.valeurs:
            vals.append(v.getValeur())

        return vals
    
    def updateSelfValeur(self):
        self.parent.updateValeur(self)

    def updateValeurs(self, valeurs, index):
        for v in self.valeurs:
            v.updateValeurs(valeurs, index)

    def verbe(self):
        return self.indice.verbe()
    
    def modifSelfVerbe(self, verbe):
        self.parent.modifVerbe(self, verbe)
        
    def updateVerbe(self, verbe, index):
        for v in self.valeurs:
            v.updateVerbes(verbe, index)

    def addIndice(self, entite, index):
        if self != entite:
            for v in self.valeurs:
                v.addIndice(entite, index)
        

class CreationValeur(QWidget):
    def __init__(self, parent, entites, index):
        super(CreationValeur, self).__init__()
        self.parent = parent
        self.layout = QVBoxLayout()

        default_text = "Champ" + str(index)
        self.champ = ChampValeur(self, default_text)
        self.creations_indices = []
        
        index_indice = 0
        for e in entites:
            if e.entite_nom != self.parent.entite_nom:
                valeurs = []
                valeurs.extend(e.getValeursText())
                creation_indice = CreationIndice(self, index_indice, e.verbe(), valeurs)
                index_indice += 1
                self.creations_indices.append(creation_indice)

        self.layout.addWidget(self.champ)
        for ci in self.creations_indices:
            self.layout.addWidget(ci)

        self.setLayout(self.layout)

    def addValeur(self):
        self.parent.addValeur()

    def getValeur(self):
        return self.champ.valeur_nom.toPlainText()
    
    def updateSelfValeur(self):
        self.parent.updateSelfValeur()

    def updateValeurs(self, valeurs, index):
        for ci in self.creations_indices:
            if ci.index_reference == index:
                ci.updateValeurs(valeurs)


    def updateVerbes(self, verbe, index):
        for ci in self.creations_indices:
            if ci.index_reference == index:
                ci.updateVerbe(verbe)

    def addIndice(self, entite, index):
        valeurs = []
        valeurs.extend(entite.getValeursText())
        creation_indice = CreationIndice(self, index, entite.verbe(), valeurs)
        self.creations_indices.append(creation_indice)
        self.layout.addWidget(self.creations_indices[len(self.creations_indices) - 1])


    def updateIndice(self, verbe_indice, index_indice):
        for ci in self.creations_indices:
            if ci.index_reference == index_indice:
                ci.updateVerbe(verbe_indice)

    def generateIndices(self):
        indices = []
        for ci in self.creations_indices:
            if ci.currentValeur() != "?":
                indices.append(ci.indice().showIndice())
        return indices
    
class ChampValeur(QWidget):
    def __init__(self, parent, default_text):
        super(ChampValeur, self).__init__()
        self.parent = parent
        self.layout = QHBoxLayout()
        label = QLabel()
        label.setText("Champ")
        label.setStyleSheet("QLabel{font:16px;}")
        self.valeur_nom = QTextEdit()
        self.valeur_nom.setText(default_text)
        self.valeur_nom.setMinimumHeight(40)
        self.valeur_nom.setMaximumHeight(40)
        self.valeur_nom.setMinimumWidth(200)
        self.valeur_nom.setMaximumWidth(200)
        self.valeur_nom.setAlignment(Qt.AlignVCenter)
        self.valeur_nom.setStyleSheet(stylesheets.ProblemCreationSpriteSheets().getTextEditStylesheet())
        self.valeur_nom.textChanged.connect(self.updateSelfValeur)        

        self.layout.addWidget(label)
        self.layout.addWidget(self.valeur_nom)
        self.layout.addStretch(1)
        self.setLayout(self.layout)
        
    def updateSelfValeur(self):
        self.parent.updateSelfValeur()



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



#############################################
################## BOUTONS ##################
#############################################
    

class GenerateProblemButton(QPushButton):
    def __init__(self, parent):
        super(GenerateProblemButton, self).__init__()
        self.parent = parent        
        self.setMinimumSize(256, 64)
        self.setMaximumSize(256, 64)
        self.setText("Générer problème")
        self.setStyleSheet(stylesheets.ProblemCreationSpriteSheets().getProblemManagerButton())

        self.mousePressEvent = self.generateProblem

    def generateProblem(self, event):
        self.parent.generateProblem()

class AddEntiteButton(QPushButton):
    def __init__(self, parent):
        super(AddEntiteButton, self).__init__()
        self.parent = parent        
        self.setMinimumSize(256, 64)
        self.setMaximumSize(256, 64)
        self.setText("Ajouter entite")
        self.setStyleSheet(stylesheets.ProblemCreationSpriteSheets().getProblemManagerButton())

        self.mousePressEvent = self.addEntite

    def addEntite(self, event):
        self.parent.addEntite()

class AddvaleurButton(QPushButton):
    def __init__(self, parent):
        super(AddvaleurButton, self).__init__()
        self.parent = parent        
        self.setMinimumSize(256, 64)
        self.setMaximumSize(256, 64)
        self.setText("Ajouter valeur")
        self.setStyleSheet(stylesheets.ProblemCreationSpriteSheets().getProblemManagerButton())

        self.mousePressEvent = self.addValeur

    def addValeur(self, event):
        self.parent.addValeur()
