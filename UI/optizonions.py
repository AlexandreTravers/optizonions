from PyQt5.QtCore import *
import sys
from widgets import *
from windows import *

def main(args):
    launch_main_gui()

def launch_main_gui():
    App = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    window.showMaximized()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main(sys.argv)