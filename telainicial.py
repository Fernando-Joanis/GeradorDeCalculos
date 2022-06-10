import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import menu


class MenuInicial(QMainWindow, menu.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

    def ir_para_soma(self):
        pass




if __name__ == '__main__':
    qt = QApplication(sys.argv)
    menu_inicial = MenuInicial()
    menu_inicial.show()
    qt.exec_()
