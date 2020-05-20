from PySide2.QtWidgets import *


class windows(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        QWidget.setWindowTitle(self,"IHM")
        self.layout=QHBoxLayout()
        self.progression=QProgressBar()
        self.progression.setValue((0))
        self.silde=QSlider()
        self.layout.addWidget(self.progression)
        self.layout.addWidget(self.silde)
        self.silde.valueChanged.connect(self.augmenteProg)
        self.setLayout(self.layout)


    def augmenteProg(self):
        self.progression.setValue(self.silde.value()+1)

if __name__ == "__main__":
   app = QApplication([])
   conf=windows()
   conf.show()
   app.exec_()
