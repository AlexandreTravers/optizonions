from PyQt5.QtCore import *
import sys
from widgets import *
from windows import *
import sys
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