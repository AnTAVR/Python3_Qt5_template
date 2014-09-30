#!/usr/bin/env python3
import sys

from PyQt5.QtWidgets import QApplication

from classes.functions import init

init(sys.path[0])

from window.mainwindow import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec_())
