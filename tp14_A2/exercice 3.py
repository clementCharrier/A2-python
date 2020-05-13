from PySide2.QtWidgets import *
from PySide2.QtGui import QIcon
from PySide2.QtCore import *
class imh(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        QWidget.setFixedSize(self,400,300)
        QWidget.setWindowTitle(self,"je change le titre")
        self.image=QIcon("d:/travail/ImgPython.png")
        QWidget.setWindowIcon(self,self.image)
        self.layout=QVBoxLayout()
        self.label=QLabel("je suis une etiquette")
        self.label.setAlignment(Qt.AlignCenter)
        self.progression=QProgressBar()
        self.progression.setValue((75))
        self.lineEdit=QLineEdit()
        self.button=QPushButton("affiche un texte")
        self.button.setToolTip("le texte affiché par le boutton")
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.progression)
        self.layout.addWidget(self.lineEdit)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

if __name__ == "__main__":
   app = QApplication([])
   win = imh()
   win.show()
   app.exec_()
