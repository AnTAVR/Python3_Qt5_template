#!/usr/bin/env python3

import sys, os

# добавляем пути для поиска компонентов.
# pathLib = '/usr/lib/main'
pathLib = sys.path[0]
pathLibWindow = os.path.join(pathLib, 'window')
pathLibWidget = os.path.join(pathLib, 'widget')
sys.path.append(pathLibWindow)
sys.path.append(pathLibWidget)
sys.path.append(os.path.join(pathLib, 'class'))

# генерация ресурсов. (только вовремя разработки!!!)
pathGenRc = "'" + os.path.join(sys.path[0], 'gen_rc.sh') + "'"
os.system(pathGenRc + ' "' + pathLibWindow + '"')
os.system(pathGenRc + ' "' + pathLibWidget + '"')

from PyQt5.QtWidgets import QApplication
from MainWindow import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)

    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec_())
