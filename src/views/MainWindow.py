from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

from src.views.ImageViewer import ImageViewer


class MainWindow(QMainWindow):
    def __init__(self, width=800, height=600):
        super(MainWindow, self).__init__(flags=Qt.Window)

        screen_size = qApp.desktop().availableGeometry().size()
        top_x = (screen_size.width() // 2) - (width // 2)
        top_y = (screen_size.height() // 2) - (height // 2)
        self.setGeometry(top_x, top_y, width, height)

        self.setWindowTitle("InstaHelper")

        self._ww = QWidget(flags=Qt.Widget)
        self._ww_layout = QGridLayout()
        self._ww.setLayout(self._ww_layout)
        self._ww.setMinimumWidth(800)
        self._ww.setMinimumHeight(600)

        self._viewer = ImageViewer()

        self._ww_layout.addWidget(self._viewer)

        self.setCentralWidget(self._ww)

        self.show()
