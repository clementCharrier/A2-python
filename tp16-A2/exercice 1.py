from PySide2.QtWidgets import *
import random as rd

class windows(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        QWidget.setWindowTitle(self,"Cycle de l'ISEN yncrea Ouest")
        QWidget.setFixedSize(self, 500,300)
        self.layout=QVBoxLayout()
        self.button=QPushButton("Choisir un Cycle")
        self.label=QLabel(" ")
        self.label.setFixedSize(460,200)
        self.layout.addWidget(self.label)
        self.layout.addWidget((self.button))
        self.button.clicked.connect(self.randomCycle)
        self.setLayout(self.layout)


    def randomCycle(self):
        cycle=rd.choice(["CSI","CIR","BIOST","CENT","BIAST","EST"])
        self.label.setText(cycle)


if __name__ == "__main__":
   app = QApplication([])
   conf=windows()
   conf.show()
   app.exec_()
