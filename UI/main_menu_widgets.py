from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from enum import Enum
import stylesheets

from indices_widgets import *
from problem_creation_buttons_widgets import *

class MainMenu(QWidget):
    def __init__(self, parent):
        super(MainMenu, self).__init__()
        self.parent = parent
        self.layout = QVBoxLayout()

        window_label = QLabel()
        window_label.setText("OPTIZONIONS")
        window_label.setStyleSheet("QLabel{font-size:72px}")
        self.layout.addWidget(window_label)

        self.layout.addWidget(SplitMenu(self))

        self.layout.setAlignment(Qt.AlignLeft)
        self.setLayout(self.layout)


class SplitMenu(QWidget):
    def __init__(self, parent):
        super(SplitMenu, self).__init__()
        self.parent = parent
        self.layout = QHBoxLayout()
        self.layout.addWidget(PremadeProblemsMenu(self))
        self.layout.addStretch()
        self.layout.addWidget(CustomProblemsMenu(self))

        self.setLayout(self.layout)


class PremadeProblemsMenu(QWidget):
    def __init__(self, parent):
        super(PremadeProblemsMenu, self).__init__()
        self.parent = parent
        self.layout = QVBoxLayout()
        menu_label = QLabel()
        menu_label.setText("Problèmes préfaits")
        menu_label.setStyleSheet("QLabel{font-size:48px}")
        self.layout.addWidget(menu_label)

        
        self.setLayout(self.layout)


class CustomProblemsMenu(QWidget):
    def __init__(self, parent):
        super(CustomProblemsMenu, self).__init__()
        self.parent = parent
        self.layout = QVBoxLayout()
        menu_label = QLabel()
        menu_label.setText("Problèmes personnalisés")
        menu_label.setStyleSheet("QLabel{font-size:48px}")
        self.layout.addWidget(menu_label)

        self.setLayout(self.layout)

