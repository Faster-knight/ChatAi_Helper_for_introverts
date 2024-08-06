import logging
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget, QApplication, QMainWindow
from PyQt6.QtCore import QRect, QSize
import os as __os

qtApp = QApplication([])
logger_module = logging.getLogger(__name__)
module_path = __os.path.dirname(__file__)


def resetQtApplication(args: list[str]):
    global qtApp
    qtApp = QApplication(args)


class WindowDivHeaderNav(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setGeometry(QRect(0, 0, 80, 600))


class WindowDivApiIntegrationsNav(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setGeometry(QRect(820, 0, 80, 600))


class WindowDivContent(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setGeometry(QRect(80, 0, 740, 600))
        self.contentComponent = None

    def setContentComponent(self, component: QWidget):
        self.contentComponent = component
        self.contentComponent.show()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(QRect(0, 0, 900, 600))
        self.setMaximumSize(QSize(900, 600))
        self.setMinimumSize(QSize(900, 600))
        self.setWindowTitle("ChatAI timepatch")

    def setIcon(self, icon: QIcon):
        self.setWindowIcon(icon)
