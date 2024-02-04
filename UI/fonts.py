
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Fonts():
    def __init__(self):
        font_id = QFontDatabase.addApplicationFont("UI/Ressources/Fonts/AANTARADISTANCE.TTF")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        self.title_font = QFont(font_family)

        font_id = QFontDatabase.addApplicationFont("UI/Ressources/Fonts/QUICKSAND_BOLD_OBLIQUE.OTF")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        self.subtitle_font = QFont(font_family)

        font_id = QFontDatabase.addApplicationFont("UI/Ressources/Fonts/QUICKSAND_BOOK.OTF")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        self.main_font = QFont(font_family)

        font_id = QFontDatabase.addApplicationFont("UI/Ressources/Fonts/QUICKSAND_BOLD.OTF")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        self.main_font_bold = QFont(font_family)

    def titleFont(self):
        return self.title_font

    def subtitleFont(self):
        return self.subtitle_font

    def mainFont(self):
        return self.main_font

    def mainFontBold(self):
        return self.main_font_bold

