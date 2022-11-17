import sys

from PyQt5.QtWidgets import QApplication

from src.controllers.InstaHelper import InstaHelper


class MainApp(QApplication):
    def __init__(self, argv):
        super(MainApp, self).__init__(argv)
        # self.setStyleSheet(Settings.MAIN_APP_STYLE_SHEET)

    def quit(self):
        print('bye bye')
        exit(0)


def main():
    app = MainApp(sys.argv)
    InstaHelper()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
