from PyQt5.QtWidgets import QLabel


class ImageViewer(QLabel):
    def __init__(self):
        super().__init__()
        self._qimage = None

        self.resize(800, 600)

    def load_image(self, qimage):
        self._qimage = qimage