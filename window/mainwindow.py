import os

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication

from ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Главное окно.
    """

    def __init__(self, *args):
        """
        Инициализация класса главного окна.
        :param args:
        """
        super(MainWindow, self).__init__(*args)
        self.setupUi(self)


    @pyqtSlot(name='on_actionAboutQt_triggered')
    def aboutQt(self):
        """
        Слот раздела меню AboutQt.
        Выводит окно с версийе Qt.
        """
        QApplication.instance().aboutQt()
