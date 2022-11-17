from PyQt5.QtGui import QImage


class Image:
    def __init__(self):
        self._qimage = None
        pass

    def load_from_file(self, input_filepath):
        self._qimage = QImage(input_filepath)
        pass

    def get_qimage(self):
        return self._qimage

