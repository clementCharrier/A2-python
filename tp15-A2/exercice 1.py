from PySide2.QtWidgets import *

class windows(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        QWidget.setWindowTitle(self,'Le titre est changé')
        QWidget.setMinimumSize(self,600,400)
        self.layout=QVBoxLayout()
        self.bp=ButtonPanel()
        self.layout.addWidget(self.bp)
        self.notificationPanel=QTextEdit()
        self.layout.addWidget(self.notificationPanel)
        self.resultTable=QTableWidget(4,3)
        self.resultTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.layout.addWidget(self.resultTable)
        self.setLayout(self.layout)

class LabledTextField(QWidget):
    def __init__(self,text):
        QWidget.__init__(self)
        self.layout=QHBoxLayout()
        self.label1=QLabel(text)
        self.texteEdit=QTextEdit()
        self.layout.addWidget(self.label1)
        self.layout.addWidget(self.texteEdit)
        self.texteEdit.setMaximumHeight(100)
        self.setLayout(self.layout)

class ButtonPanel(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.layout=QHBoxLayout()
        self.button1=QPushButton("bouton 1")
        self.button2=QPushButton("bouton 2")
        self.button3=QPushButton("bouton 3")
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)
        self.layout.addWidget(self.button3)
        self.setLayout(self.layout)


class ConfigurationDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.layout=QVBoxLayout()
        self.labled1=LabledTextField("Ip Address")
        self.labled2=LabledTextField("User")
        self.labled3=LabledTextField("Password")
        self.layout.addWidget(self.labled1)
        self.layout.addWidget(self.labled2)
        self.layout.addWidget(self.labled3)
        self.setLayout(self.layout)
        self.win=windows()
        self.win.show()




if __name__ == "__main__":
   app = QApplication([])
   conf=ConfigurationDialog()
   conf.show()
   app.exec_()

