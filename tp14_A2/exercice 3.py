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
        self.progression.setValue((1))
        self.lineEdit=QLineEdit()
        self.button=QPushButton("augment le téléchargement")
        self.button.setToolTip("Tu passes le curseur sur le boutton")
        self.button2=QPushButton("réinitialise le téléchargement")
        self.layout.addWidget(self.button2)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.progression)
        self.layout.addWidget(self.lineEdit)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)



    def MousePressedEvent(self):
        self.progression.setValue(self.progression.value()+1)
        if self.progression.value()==100 :
            self.label.setText("Téléchargement terminé")
    def MousPressedEvent2(self):
        self.progression.setValue(0)
        self.label.setText("le téléchargement à été réinitialisé")


if __name__ == "__main__":
   app = QApplication([])
   win = imh()
   win.show()
   win.button.clicked.connect(win.MousePressedEvent)
   win.button2.clicked.connect(win.MousPressedEvent2)
   app.exec_()


