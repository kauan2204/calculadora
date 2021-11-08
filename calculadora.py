import sys
import PyQt5.QtWidgets as pyqt5
from time import sleep


class Calculadora(pyqt5.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.central_widget = pyqt5.QWidget()
        self.grid = pyqt5.QGridLayout(self.central_widget)
        
        self.setCentralWidget(self.central_widget)
        self.setWindowTitle('Calculadora')

        self.display = pyqt5.QLineEdit()
        self.grid.addWidget(self.display, 0, 0, 1, 5)
        self.display.setDisabled(True)
        self.display.setStyleSheet('* {background: #fff; color: #000; font-size: 30px}')
        self.display.setSizePolicy(pyqt5.QSizePolicy.Preferred, pyqt5.QSizePolicy.Expanding)
        
        self.botton(pyqt5.QPushButton('7'), 1, 0, 1, 1)
        self.botton(pyqt5.QPushButton('8'), 1, 1, 1, 1)
        self.botton(pyqt5.QPushButton('9'), 1, 2, 1, 1)
        self.botton(pyqt5.QPushButton('<-'), 1, 3, 1, 2,
        lambda: self.display.setText(self.display.text()[:-1]))
        
        self.botton(pyqt5.QPushButton('4'), 2, 0, 1, 1)
        self.botton(pyqt5.QPushButton('5'), 2, 1, 1, 1)
        self.botton(pyqt5.QPushButton('6'), 2, 2, 1, 1)
        self.botton(pyqt5.QPushButton('C'), 2, 3, 1, 2, lambda: self.display.setText(''))
        self.botton(pyqt5.QPushButton('6'), 2, 2, 1, 1)

        
        self.botton(pyqt5.QPushButton('1'), 3, 0, 1, 1)
        self.botton(pyqt5.QPushButton('2'), 3, 1, 1, 1)
        self.botton(pyqt5.QPushButton('3'), 3, 2, 1, 1)
        self.botton(pyqt5.QPushButton('+'), 3, 3, 2, 1, style='background: #70e000')
        self.botton(pyqt5.QPushButton('/'), 3, 4, 1, 1)
        
        self.botton(pyqt5.QPushButton('.'), 4, 0, 1, 1)
        self.botton(pyqt5.QPushButton('0'), 4, 1, 1, 1)
        self.botton(pyqt5.QPushButton('='), 4, 2, 1, 1, self.igual, 'background: black; color: white')
        self.botton(pyqt5.QPushButton('*'), 4, 4, 1, 1)
        
        self.setFixedSize(400, 400)

    def botton(self, bttn, raw, colum, rawspan, columspan, funcao=None, style=None):
        self.grid.addWidget(bttn, raw, colum, rawspan, columspan)
        if funcao is None:
            bttn.clicked.connect(lambda: self.display.setText(self.display.text() + bttn.text()))
        else:
            bttn.clicked.connect(funcao)
        if not style is None:
            bttn.setStyleSheet(style)

        bttn.setSizePolicy(pyqt5.QSizePolicy.Preferred, pyqt5.QSizePolicy.Expanding)



    def igual(self):
        try:
            self.display.setText(str(eval(self.display.text())))
        except Exception as e:
            print(e)

if __name__ == '__main__':
    qt = pyqt5.QApplication(sys.argv)
    calculadora = Calculadora()
    calculadora.show()
    qt.exec_()
