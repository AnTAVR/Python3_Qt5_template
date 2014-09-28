#!/usr/bin/env python3
import sys
import os

from PyQt5.QtCore import QLibraryInfo, QProcess, QProcessEnvironment
from PyQt5.QtWidgets import QApplication

app = QApplication(sys.argv)

base = os.path.dirname(__file__)
env = QProcessEnvironment.systemEnvironment()
print(os.path.join(base, 'widget', 'designer'))
env.insert('PYQTDESIGNERPATH', os.path.join(base, 'widget', 'designer'))
env.insert('PYTHONPATH', os.path.join(base, 'widget'))

# Запускаю Designer
designer = QProcess()
designer.setProcessEnvironment(env)

designer_bin = os.path.join(QLibraryInfo.location(QLibraryInfo.BinariesPath), 'designer')

designer.start(designer_bin)
designer.waitForFinished(-1)

sys.exit(designer.exitCode())
