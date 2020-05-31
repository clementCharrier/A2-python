from PySide2.QtWidgets import *

class windows(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        QWidget.setWindowTitle(self,"ISEN Yncréa Ouest/Campus de Nantes")
        QWidget.setFixedSize(self,600,400)
        self.layout=QVBoxLayout()
        self.text=QTextEdit("les affichages des scénarios vont apparaître ici")
        self.button1=QPushButton("scénario 1")
        self.button2=QPushButton("scénario 2")
        self.button3=QPushButton("scenario 3")
        self.button1.clicked.connect(Scene1)
        self.button2.clicked.connect(Scene2)
        self.button3.clicked.connect(Scene3)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)
        self.layout.addWidget(self.button3)
        self.setLayout(self.layout)


class ecole():
    """On initialise les différents attributs privé, l'attibut self.__Salle est une liste d'objet de la classe salle"""
    def __init__(self,nom,SalleSup,SalleAct):
        self.__nom=nom
        self.__SallesSup=SalleSup
        self.__SallesAct=SalleAct
        self.__Salle=[]

    def getName(self):
        return self.__nom
    def getSallesSup(self):
        return self.__SallesSup
    def getSallesAct(self):
        return self.__SallesAct
    def getSalle(self):
        return self.__Salle
    def AjoutSalle(self,salle):
        self.__Salle.append(salle)
        self.__SallesAct+=1
    def RemoveSalle(self,salle):
        self.__Salle.remove(salle)
        self.__SallesAct-=1

    def affichage(self):
        texte1="Le nouveau bâtiment de l'école "+str(self.__nom)+ " peut supporter "+str(self.__SallesSup)+" salles."
        # print("Le nouveau bâtiment de l'école "+str(self.__nom)+" peut supporter "+str(self.__SallesSup)+" salles.")
        if self.__SallesAct==0 or self.__SallesAct is None:
            texte2=texte1+"\nIl ne contient actuellement aucune salle."
            # print("Il ne contient actuellement aucune salle.")
            return texte1
        else :
            texte2=texte1+"\nIl contient "+str(self.__SallesAct)+" salles, listés ci-après :"
            # print("Il contient "+str(self.__SallesAct)+" salles, listés ci-après :")
            textef=""
            for i in self.__Salle:
                textef+=i.affichage()
            return texte2+textef

class salle():
    def __init__(self,place,project):
        self.__place=place
        self.__proj=project

    def getPlace(self):
        return self.__place
    def getProj(self):
        return self.__proj

class salleSpe(salle):
    def __init__(self,place,project,nbEquipement):
        salle.__init__(self,place,project)
        self.__nbEquip=nbEquipement

    def getNbequip(self):
        return self.__nbEquip

class salleBan(salle):
    def __init__(self,place,project,priseElec):
        salle.__init__(self,place,project)
        self.__priseElec=priseElec #True or False

    def getPrise(self):
        return self.__priseElec

    def affichage(self):
        if self.getProj()==True and self.__priseElec==True:
            # print("Salle banalisée qui peut accueillir "+ str(self.getPlace())+" étudiants, possédant des prises et un projecteur")
            texte2="\nSalle banalisée qui peut accueillir "+ str(self.getPlace())+" étudiants, possédant des prises et un projecteur"
            return texte2
        elif self.getProj()==False and self.__priseElec==True:
            # print("Salle banalisée qui peut accueillir "+ str(self.getPlace())+" étudiants, possédant des prises mais pas de projecteur")
            texte2="\nSalle banalisée qui peut accueillir "+ str(self.getPlace())+" étudiants, possédant des prises mais pas de projecteur"
            return texte2
        elif self.getProj()==True and self.__priseElec==False:
            # print("Salle banalisée qui peut accueillir "+ str(self.getPlace())+" étudiants, ne possédant pas de prise mais un projecteur")
            texte2="\nSalle banalisée qui peut accueillir "+ str(self.getPlace())+" étudiants, ne possédant pas de prise mais un projecteur"
            return texte2
        elif self.getProj()==True and self.__priseElec==True:
            # print("Salle banalisée qui peut accueillir "+ str(self.getPlace())+" étudiants, ne possédant pas de prise ni de projecteur")
            texte2="\nSalle banalisée qui peut accueillir "+ str(self.getPlace())+" étudiants, ne possédant pas de prise ni de projecteur"

            return texte2

class salleInfo(salleSpe):
    def __init__(self,place,project,nbEquipement,sysEx):
        salleSpe.__init__(self,place,project,nbEquipement)
        self.__sysExp=sysEx

    def getSys(self):
        return self.__sysExp

    def affichage(self):
        if self.getProj()==True:
            texte2="\nSalle d'informatique possédant des ordinateurs ayant "+str(self.__sysExp) +" comme système d'exploitation ainsi qu'un projecteur"
            # print("Salle d'informatique possédant des ordinateurs ayant "+str(self.__sysExp) +" comme système d'exploitation ainsi qu'un projecteur")
            return texte2
        else:
            texte2="\nSalle d'informatique possédant des ordinateurs ayant "+str(self.__sysExp) +" comme système d'exploitation"
            # print("Salle d'informatique possédant des ordinateurs ayant "+str(self.__sysExp) +" comme système d'exploitation")
            return texte2

class sallePhy(salleSpe):
    def __init__(self,place,project,nbEquipement,nbPaillasse,nbChaisePaillasse):
        salleSpe.__init__(self,place,project,nbEquipement)
        self.__paillasse=nbPaillasse
        self.__nbChaiseP=nbChaisePaillasse

    def getNbP(self):
        return self.__paillasse
    def getChaiseP(self):
        return self.__nbChaiseP

class salleElec(sallePhy):
    def __init__(self,place,project,nbEquipement,nbPaillasse,nbChaisePaillasse,nbOscillo):
        sallePhy.__init__(self,place,project,nbEquipement,nbPaillasse,nbChaisePaillasse)
        self.__nbOscillo=nbOscillo

    def getNbOscillo(self):
        return self.__nbOscillo

    def affichage(self):
        # print (" Salle d'électricité qui peut accueillir "+str(self.getChaiseP())+"  étudiants dans "+str(self.getNbP())+" paillasses et contient "
        #        +str(self.__nbOscillo)+" oscilloscopes")
        texte2="\nSalle d'électricité qui peut accueillir "+str(self.getChaiseP())+"  étudiants dans "+str(self.getNbP())+" paillasses et contient "+str(self.__nbOscillo)+" oscilloscopes"
        return texte2


class salleMeca(sallePhy):
    def __init__(self,place,project,nbEquipement,nbPaillasse,nbChaisePaillasse,nbRessort):
        sallePhy.__init__(self,place,project,nbEquipement,nbPaillasse,nbChaisePaillasse)
        self.__nbRessort=nbRessort

    def getNbRessort(self):
        return self.__nbRessort

    def affichage(self):
        # print (" Salle d'électricité qui peut accueillir "+str(self.getChaiseP())+"  étudiants dans "+str(self.getNbP())+" paillasses et contient "
        #        +str(self.__nbRessort)+" ressorts")
        texte2="\nSalle d'électricité qui peut accueillir "+str(self.getChaiseP())+"  étudiants dans "+str(self.getNbP())+" paillasses et contient "+str(self.__nbRessort)+" ressorts"
        return texte2

def Scene1():
    bat=ecole("ISEN Yncréa Ouest/Campus de Nantes",50,0)
    texte=bat.affichage()
    conf.text.setText(texte)


def Scene2():
    bat2=ecole("ISEN Yncréa Ouest/Campus de Nantes",50,0)
    salle1=salleBan(30,True,True)
    salle2=salleInfo(30,False,1,"Windows 10")
    salle3=salleElec(30,False,1,7,28,30)
    salle4=salleMeca(30,False,1,5,20,25)
    bat2.AjoutSalle(salle1)
    bat2.AjoutSalle(salle2)
    bat2.AjoutSalle(salle3)
    bat2.AjoutSalle(salle4)
    texte=bat2.affichage()
    conf.text.setText(texte)

def Scene3():
    bat3=ecole("ISEN Yncréa Ouest/Campus de Nantes",50,0)
    salle5=salleBan(30,True,True)
    salle6=salleInfo(30,False,1,"Windows 10")
    salle7=salleElec(30,False,1,7,28,30)
    salle8=salleInfo(30,False,1,"Unbuntu")
    bat3.AjoutSalle(salle5)
    bat3.AjoutSalle(salle6)
    bat3.AjoutSalle(salle7)
    bat3.AjoutSalle(salle8)
    texte=bat3.affichage()
    conf.text.setText(texte)





if __name__ == "__main__":
   app = QApplication([])
   conf=windows()
   conf.show()
   app.exec_()



