import os

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi

fileDirName = os.path.dirname(__file__)


class MainWindow(QMainWindow):
    """
    Главное окно
    """
    def __init__(self, *args):
        """

        :param args:
        """
        super(MainWindow, self).__init__(*args)
        print(__name__)
        loadUi(os.path.join(fileDirName, 'UI_' + __class__.__name__ + '.ui'), self)

    @pyqtSlot()
    def on_actionAboutQt_triggered(self):
        QApplication.instance().aboutQt()
