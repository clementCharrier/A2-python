from PySide2.QtWidgets import *
from PySide2.QtCore import *



class windows(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        QWidget.setWindowTitle(self,"Calculatrice")
        self.layout=QVBoxLayout()
        self.label=QLabel("0")
        self.label.setAlignment(Qt.AlignLeft)
        self.button1=ButtonPanel("C","CE")
        self.button2=ButtonPanel2(7,8,9,"/")
        self.button3=ButtonPanel2(4,5,6,"*")
        self.button4=ButtonPanel2(1,2,3,"-")
        self.button5=ButtonPanel2(0,".","=","+")
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)
        self.layout.addWidget(self.button3)
        self.layout.addWidget(self.button4)
        self.layout.addWidget(self.button5)
        self.setLayout(self.layout)


class ButtonPanel(QWidget):
    def __init__(self,text1,text2):
        QWidget.__init__(self)
        self.layout=QHBoxLayout()
        self.button1=QPushButton(str(text1))
        self.button2=QPushButton(str(text2))
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)
        self.button1.clicked.connect(self.changeV1)
        self.button2.clicked.connect(self.changeV2)
        self.setLayout(self.layout)

    def changeV1(self):
        conf.label.setAlignment(Qt.AlignLeft)
        conf.label.setText("0")
    def changeV2(self):
        conf.label.setText(conf.label.text()[:len(conf.label.text())-1])

class ButtonPanel2(QWidget):
    def __init__(self,text1,text2,text3,text4):
        QWidget.__init__(self)
        self.layout=QHBoxLayout()
        self.button1=QPushButton(str(text1))
        self.button2=QPushButton(str(text2))
        self.button3=QPushButton(str(text3))
        self.button4=QPushButton(str(text4))
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)
        self.layout.addWidget(self.button3)
        self.layout.addWidget(self.button4)
        self.button1.clicked.connect(self.ChangeValeur1)
        self.button2.clicked.connect(self.ChangeValeur2)
        self.button3.clicked.connect(self.ChangeValeur3)
        self.button4.clicked.connect(self.ChangeValeur4)
        self.setLayout(self.layout)

    def ChangeValeur1(self):
        if conf.label.text()=='0':
            conf.label.setAlignment(Qt.AlignRight)
            conf.label.setText(self.button1.text())
        elif self.button1.text()=="=":
            conf.label.setAlignment(Qt.AlignLeft)
            conf.label.setText(str(eval(conf.label.text())))
        else:
            conf.label.setAlignment(Qt.AlignRight)
            conf.label.setText(conf.label.text()+self.button1.text())

    def ChangeValeur2(self):
        if conf.label.text()=='0':
            conf.label.setAlignment(Qt.AlignRight)
            conf.label.setText(self.button2.text())
        elif self.button2.text()=="=":
            conf.label.setAlignment(Qt.AlignLeft)
            conf.label.setTextstr((eval(conf.label.text())))
        else:
            conf.label.setAlignment(Qt.AlignRight)
            conf.label.setText(conf.label.text()+self.button2.text())
    def ChangeValeur3(self):
        if conf.label.text()=='0':
            conf.label.setAlignment(Qt.AlignRight)
            conf.label.setText(self.button3.text())
        elif self.button3.text()=="=":
            conf.label.setAlignment(Qt.AlignLeft)
            conf.label.setText(str(eval(conf.label.text())))
        else:
            conf.label.setAlignment(Qt.AlignRight)
            conf.label.setText(conf.label.text()+self.button3.text())

    def ChangeValeur4(self):
        if conf.label.text()=='0':
            conf.label.setAlignment(Qt.AlignRight)
            conf.label.setText(self.button4.text())
        elif self.button4.text()=="=":
            conf.label.setAlignment(Qt.AlignLeft)
            conf.label.setText(str(eval(conf.label.text())))
        else:
            conf.label.setAlignment(Qt.AlignRight)
            conf.label.setText(conf.label.text()+self.button4.text())


if __name__ == "__main__":
   app = QApplication([])
   conf=windows()
   conf.show()
   app.exec_()
