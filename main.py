#!/usr/bin/env python3

import sys

from PyQt5.QtWidgets import QApplication
from window.MainWindow import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)

    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec_())
