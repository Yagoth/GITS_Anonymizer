# Created May 28, 2021 by Yagoth and Ko
import sys
from PyQt5.QtWidgets import *
from gitsAnonymizerApp import GITSAnonymizerApp

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GITSAnonymizerApp()
    sys.exit(app.exec_())
