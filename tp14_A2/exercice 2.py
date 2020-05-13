from PySide2.QtWidgets import *

class imh(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        QWidget.setWindowTitle(self,"je change le titre")
        self.layout=QGridLayout()
        self.label=QLabel("je suis une étiquette")
        self.button1=QPushButton("je suis boutton1")
        self.button2=QPushButton("je suis boutton2")
        self.text=QTextEdit()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)
        self.setLayout(self.layout)

if __name__ == "__main__":
   app = QApplication([])
   win = imh()
   win.show()
   app.exec_()
