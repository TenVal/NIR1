import sys
from PyQt5 import QtWidgets
from MainWindow import MainWindow
# from MainWindowMpl import MplWidget


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # main = MplWidget()
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

