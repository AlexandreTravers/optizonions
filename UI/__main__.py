from PyQt5.QtCore import *
import sys
import os
# Ajouter le chemin du dossier parent au chemin de recherche des modules
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)


from widgets import *
from windows import *


import traceback

def main(args):
    launch_main_gui()

def launch_main_gui():
    App = QApplication(sys.argv)
    window = ProblemWindow()
    #window.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    window.showMaximized()
    sys.exit(App.exec_())
    sys.excepthook = my_hook


def my_hook(*args):  # We don't really need arguments    
    traceback.print_exc()


if __name__ == '__main__':
    main(sys.argv)