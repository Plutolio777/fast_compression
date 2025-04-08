from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QLabel, \
    QComboBox, QSlider, QFileDialog, QCheckBox, QFrame, QStackedWidget, QScrollArea, QDesktopWidget
from PyQt5.QtCore import Qt
from siui.core import SiGlobal
from siui.templates.application.application import SiliconApplication

from app.components.page_homepage import ExampleHomepage


class MyApplication(SiliconApplication):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        screen_geo = QDesktopWidget().screenGeometry()
        self.setMinimumSize(1024, 380)
        self.resize(1366, 916)
        self.move((screen_geo.width() - self.width()) // 2, (screen_geo.height() - self.height()) // 2)
        self.layerMain().setTitle("Silicon UI Gallery")
        self.setWindowTitle("Silicon UI Gallery")
        self.setWindowIcon(QIcon("../img/empty_icon.png"))

        self.layerMain().addPage(ExampleHomepage(self),
                                 icon=SiGlobal.siui.iconpack.get("ic_fluent_home_filled"),
                                 hint="主页", side="top")

        self.layerMain().setPage(0)
        SiGlobal.siui.reloadAllWindowsStyleSheet()

