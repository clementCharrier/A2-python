from PySide2.QtWidgets import *

class windows(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        QWidget.setWindowTitle(self,"IMH")
        QWidget.setFixedSize(self,500,300)
        self.layout=QVBoxLayout()
        self.button1=QPushButton("Quitte la fenetre")
        self.n=0
        self.n2=0
        self.button4=QPushButton("choisir")
        self.menu=QMenu()
        self.menu.addAction("Bouton 1",self.ferme)
        self.menu.addAction("Bouton 2",self.changeTitre)
        self.menu.addAction("Bouton 3",self.ChangeTexte)
        self.button4.setMenu(self.menu)
        self.button2=QPushButton("clic "+str(self.n))
        self.button3=QPushButton("modifie le texte")
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)
        self.layout.addWidget(self.button3)
        self.button1.clicked.connect(self.ferme)
        self.button2.clicked.connect(self.changeTitre)
        self.button3.clicked.connect(self.ChangeTexte)
        self.layout.addWidget(self.button4)
        self.texte=QTextEdit("Le nombre de clic va être affiché ici")
        self.layout.addWidget(self.texte)
        self.setLayout(self.layout)

    def ferme(self):
        QWidget.close(self)

    def changeTitre(self):
        self.n+=1
        self.button2.setText("clic "+str(self.n))

    def ChangeTexte(self):
        self.n2+=1
        self.texte.setText("clic "+str(self.n2))


if __name__ == "__main__":
   app = QApplication([])
   conf=windows()
   conf.show()
   app.exec_()

