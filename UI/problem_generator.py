from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from problem_creation_widgets import *
from problem_solving_widgets import *
from zebra_solving_widgets import *
from main_menu_widgets import *
import json


class ProblemGenerator():
    def CreateProblem(self, parent, contraintes, indices):
        if len(contraintes) > 4: 
            return ZebraSolvingWidget(parent, contraintes, indices)
        
        else:
            return GridSolvingWidget(parent, contraintes, indices)
