import sys
from PyQt5.QtWidgets import QApplication
from style import style
from widgets.MainWindow import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(style)
    MainWin = MainWindow()
    MainWin.show()
    sys.exit(app.exec_())