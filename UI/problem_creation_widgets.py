from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from enum import Enum
import stylesheets

from indices_widgets import *
from problem_creation_buttons_widgets import *

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
        self.layout.addWidget(self.entites, 4)



        self.indices_manuel_creator = IndiceManuelCreator(self)
        self.layout.addWidget(self.indices_manuel_creator)
        self.indices_manuels = []
        self.indices_display = IndicesDisplay(self)
        self.layout.addWidget(self.indices_display, 3)



        self.quantity_widget = QuantityWidget(self)
        self.layout.addWidget(self.quantity_widget)
        self.layout.setSpacing(0)
        self.layout.setAlignment(Qt.AlignLeft)
        self.setLayout(self.layout)

    def addEntite(self):
        self.entites.addEntite()

    def addValeur(self):
        self.entites.addValeur()

    def addIndiceManuel(self, indice):
        indiceManuel = IndiceManuel(self, indice)
        for i in self.indices_manuels:
            if i.indice_text == indiceManuel.indice_text:
                self.indices_manuel_creator.setIndiceValide(False)
                return
        
        self.indices_manuel_creator.setIndiceValide(True)
        self.indices_manuels.append(indiceManuel)
        self.indices_display.addIndice(self.indices_manuels[len(self.indices_manuels) - 1])
    
    def removeIndiceManuel(self, indice):
        for i in self.indices_manuels:
            if i.indice_text == indice.indice_text:
                self.indices_manuels.remove(i)
                self.indices_display.reset(self.indices_manuels)
                return
    
    def generateProblem(self):
        contraintes = self.entites.generateProblem()
        indices = self.indices_display.generateIndices()
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


    def addEntite(self):
        self.parent.addEntite()
    
    def addValeur(self):
        self.parent.addValeur()

    def generateProblem(self):
        self.parent.generateProblem()


class EntiteWidgets(QWidget):
    def __init__(self, parent):
        super(EntiteWidgets, self).__init__()
        self.parent = parent

        self.valeur_qty = 1
        

        self.entites = []
        #entite = CreationEntite(self, self.valeur_qty)
        #self.entites.append(entite)

        self.entite_mere = CreationEntiteMere(self, self.valeur_qty)

        self.layout = QHBoxLayout(self)
        self.layout.setAlignment(Qt.AlignTop)
        self.setLayout(self.layout)
        self.scroll = QScrollArea(self)
        self.layout.addWidget(self.scroll)
        self.scroll.setWidgetResizable(True)
        self.scroll_content = QWidget(self.scroll)

        self.scroll_layout = QHBoxLayout(self.scroll_content)
        self.scroll_layout.setAlignment(Qt.AlignTop)
        self.scroll_content.setLayout(self.scroll_layout)
        self.scroll_layout.addWidget(self.entite_mere)
        for entite in self.entites:
            self.scroll_layout.addWidget(entite)
        self.scroll.setWidget(self.scroll_content)
        self.scroll.setStyleSheet(stylesheets.ProblemCreationSpriteSheets().getScrollerStylesheet())
        self.setLayout(self.layout)


    """##########################"""
    """### ENTITES ET VALEURS ###"""
    """##########################"""
    def addEntite(self):
        #entite = CreationEntite(self, self.valeur_qty)
        entite = LayoutedEntiteWidget(self, self.valeur_qty)
        self.entites.append(entite)
        self.scroll_layout.addWidget(self.entites[len(self.entites) - 1])
        index = len(self.entites) - 1
        #for e in self.entites:
        #    e.addIndice(entite, index)
        self.entite_mere.addIndice(entite, index)

    def addValeur(self):
        self.valeur_qty += 1
        self.entite_mere.addValeurChamp()
        for e in self.entites:
            e.addValeurChamp()

    def updateValeur(self, entite):
        index = 0
        for e in self.entites:
            if e.entiteNom().toPlainText() == entite.entiteNom().toPlainText():
                break
            index += 1
        
        self.entite_mere.updateValeurs(entite.getValeursText(), index)



    """##########################"""
    """###### VERBE INDICE ######"""
    """##########################"""    
    def modifVerbe(self, entite, verbe):
        index = 0


        for e in self.entites:
            if e.entiteNom().toPlainText() == entite.entiteNom().toPlainText():
                break
            index += 1

        #for e in self.entites:
        #    if e.entite_nom.toPlainText() != entite.entite_nom.toPlainText():
        self.entite_mere.updateVerbe(verbe, index)


    """##########################"""
    """######### INDICES ########"""
    """##########################"""
    def generateIndices(self):
        indices = []
        indices.append(self.entite_mere.generateIndices())
        for im in self.indices_manuels:
            indices.append(im)
        return indices
    

    """##########################"""
    """######## PROBLEME ########"""
    """##########################"""
    def generateProblem(self):
        problem = []
        problem.append(self.entite_mere.generateContrainte())
        for e in self.entites:
            problem.append(e.generateContrainte())
        return problem

        


#############################################
############# ENTITES & VALEURS #############
#############################################

class CreationEntiteMere(QWidget):
    def __init__(self, parent, valeurs):
        super(CreationEntiteMere, self).__init__()
        self.parent = parent
        self.layout = QVBoxLayout()
        self.valeurs = []
        #self.layout.addStretch(1)

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
        #self.layout.addWidget(self.indice)

        for i in range (0, valeurs):
            valeur = CreationValeurEntiteMere(self, self.parent.entites, i)
            self.valeurs.append(valeur)
            self.layout.addWidget(self.valeurs[i]) 
        
        self.setLayout(self.layout)        

    def entiteNom(self):
        return self.entite_nom

    """##########################"""
    """######### VALEURS ########"""
    """##########################"""
    def addValeur(self):
        self.parent.addValeur()

    def addValeurChamp(self):
        index = len(self.valeurs)
        valeur = CreationValeurEntiteMere(self, self.parent.entites, index)
        self.valeurs.append(valeur)
        self.layout.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.valeurs[index])

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

    """##########################"""
    """###### VERBE INDICE ######"""
    """##########################"""
    """def verbe(self):
        return self.indice.verbe()
    
    def modifSelfVerbe(self, verbe):
        self.parent.modifVerbe(self, verbe)"""
        
    def updateVerbe(self, verbe, index):
        for v in self.valeurs:
            v.updateVerbes(verbe, index)
    
    """##########################"""
    """######### INDICES ########"""
    """##########################"""
    def addIndice(self, entite, index):
        if self != entite:
            for v in self.valeurs:
                v.addIndice(entite, index)

    """def generateIndices(self):
        indices = []
        for v in self.valeurs:
            indices.append(v.generateIndices())
        return indices"""

    """##########################"""
    """###### CONTRAINTES #######"""
    """##########################"""
    def generateContrainte(self):
        contrainte = []
        for v in self.valeurs:
            contrainte.append(v.getValeur())
        return contrainte

class LayoutedEntiteWidget(QWidget):
    def __init__(self, parent, valeurs):
        super(LayoutedEntiteWidget, self).__init__()
        self.parent = parent
        self.entite = CreationEntite(parent, valeurs)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.entite)
        self.layout.addStretch(1)
        self.setLayout(self.layout)

    def verbe(self):
        return self.entite.verbe()

    def getValeursText(self):
        return self.entite.getValeursText()

    def addValeurChamp(self):
        self.entite.addValeurChamp()

    def entiteNom(self):
        return self.entite.entiteNom()

    def generateContrainte(self):
        return self.entite.generateContrainte()

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
            valeur = CreationValeur(self, i)
            self.valeurs.append(valeur)
            self.layout.addWidget(self.valeurs[i]) 
        
        self.layout.addStretch(1)
        self.setLayout(self.layout)        

    def entiteNom(self):
        return self.entite_nom

    """##########################"""
    """######### VALEURS ########"""
    """##########################"""
    def addValeur(self):
        self.parent.addValeur()

    def addValeurChamp(self):
        index = len(self.valeurs)
        valeur = CreationValeur(self, index)
        self.valeurs.append(valeur)
        self.layout.setAlignment(Qt.AlignCenter)
        self.layout.insertWidget(self.layout.count() - 1, self.valeurs[index])

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

    """##########################"""
    """###### VERBE INDICE ######"""
    """##########################"""
    def verbe(self):
        return self.indice.verbe()
    
    def modifSelfVerbe(self, verbe):
        self.parent.modifVerbe(self, verbe)
        
    def updateVerbe(self, verbe, index):
        for v in self.valeurs:
            v.updateVerbes(verbe, index)

    """##########################"""
    """###### CONTRAINTES #######"""
    """##########################"""
    def generateContrainte(self):
        contrainte = []
        for v in self.valeurs:
            contrainte.append(v.getValeur())
        return contrainte
    

class CreationValeurEntiteMere(QWidget):
    def __init__(self, parent, entites, index):
        super(CreationValeurEntiteMere, self).__init__()
        self.parent = parent
        self.layout = QVBoxLayout()

        default_text = "Champ" + str(index)
        self.champ = ChampValeur(self, default_text)
        self.creations_indices = []
        

        index_indice = 0
        for e in entites:
            if e.entiteNom() != self.parent.entiteNom():
                valeurs = []
                valeurs.extend(e.getValeursText())
                creation_indice = CreationIndice(self, index_indice, e.verbe(), valeurs)
                index_indice += 1
                self.creations_indices.append(creation_indice)

        self.layout.addWidget(self.champ)
        for ci in self.creations_indices:
            self.layout.addWidget(ci)

        self.setLayout(self.layout)

    """##########################"""
    """######### VALEUR #########"""
    """##########################"""
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

    """##########################"""
    """##### VERBES INDICES #####"""
    """##########################"""
    def updateVerbes(self, verbe, index):
        for ci in self.creations_indices:
            if ci.index_reference == index:
                ci.updateVerbe(verbe)


    """##########################"""
    """######### INDICES ########"""
    """##########################"""
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

        

class CreationValeur(QWidget):
    def __init__(self, parent, index):
        super(CreationValeur, self).__init__()
        self.parent = parent
        self.layout = QVBoxLayout()

        default_text = "Champ" + str(index)
        self.champ = ChampValeur(self, default_text)
        self.creations_indices = []

        self.layout.addWidget(self.champ)
        self.setLayout(self.layout)

    """##########################"""
    """######### VALEUR #########"""
    """##########################"""
    def addValeur(self):
        self.parent.addValeur()

    def getValeur(self):
        return self.champ.valeur_nom.toPlainText()
    
    def updateSelfValeur(self):
        self.parent.updateSelfValeur()
    

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