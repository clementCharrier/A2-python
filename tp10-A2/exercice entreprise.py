class multinationale():
    def __init__(self,nom,pays):
        self.__nom=nom
        self.__pays=pays
        self.__filiale=[]

    def Addfili(self,f):
        self.__filiale.append(f)

    def affichage(self):
        print('La multinationale '+str(self.__nom)+" est compose de "+str(len(self.__filiale))+" filiales. Son pays d'origine est "+str(self.__pays)
              +".")
        liste_annee=[]
        nb_emploi=0
        for i in self.__filiale:
            liste_annee.append(i.getDate())
            nb_emploi+=len(i.getS())
        j=liste_annee.index(min(liste_annee))
        print("- La fililale la plus ancienne de cette multinationale est : "+str(self.__filiale[j].getN())+". Elle est composée \n de "
              +str(len(self.__filiale[j].getS()))+" salariés")
        print(str(self.__nom)+" est composée de "+str(nb_emploi)+" salariés :")

        for i in self.__filiale:
            i.affichage()

class filiale():
    def __init__(self,nom,pays,date):
        self.__nom=nom
        self.__pays=pays
        self.__date=date
        self.__salarie=[]

    def setS(self,s):
        self.__salarie.append(s)

    def getDate(self):
        return self.__date
    def getS(self):
        return self.__salarie
    def getN(self):
        return self.__nom
    def affichage(self):
        pays=self.__pays
        for j in self.__salarie:
            j.affichage(pays)
class salarie():
    def __init__(self,nom,prenom,echelon_sociale,Id):
        self._nom=nom
        self._prenom=prenom
        self._echelon=echelon_sociale
        self._id=Id


class directeur(salarie):
    def __init__(self,annee,nom,prenom,echelon,id):

        self.__annee=annee
        salarie.__init__(self,nom,prenom,echelon,id)

    def affichage(self,pays):
        print("[id="+str(self._id)+"] "+str(self._nom)+" "+str(self._prenom)+", salaire : "+str(self._echelon)+", satut : Directuer, Année de nomination : "+
              str(self.__annee)+" \nsite : "+str(pays))

class employe(salarie):
    def __init__(self,nomm,prenom,echelon,id,anb,nbt):
        salarie.__init__(self,nomm,prenom,echelon,id)
        self._anb=anb
        self._nbt=nbt

class admin(employe):
    def __init__(self,nom,prenom,echelon,id,anb,nbt,service):
        employe.__init__(self,nom,prenom,echelon,id,anb,nbt)
        self.__service=service

    def affichage(self,pays):
        print("[id="+str(self._id)+"] "+str(self._nom)+" "+str(self._prenom)+", salaire : "+str(self._echelon)+", satut : Admin, Année d'embauche : "+
              str(self._anb)+" \nsite : "+str(pays)+" Nombre de jours de travail : "+str(self._nbt)+", service : "+str(self.__service))



class inge(employe):
    def __init__(self,nom,prenom,echelon,id,anb,nbt,nbp,nbg):
        employe.__init__(self,nom,prenom,echelon,id,anb,nbt)
        self._nbp=nbp
        self._nbg=nbg


class ingeJ(inge):
    def __init__(self,nom,prenom,echelon,id,anb,nbt,nbp,nbg,exp):
        inge.__init__(self,nom,prenom,echelon,id,anb,nbt,nbp,nbg)
        self.__exp=exp
    def affichage(self,pays):
        print("[id="+str(self._id)+"] "+str(self._nom)+" "+str(self._prenom)+", salaire : "+str(self._echelon)+", satut : Ingernieur Junior , Année d'embauche : "+
              str(self._anb)+" \n site : "+str(pays)+" Nombre de jours de travail : "+str(self._nbt)+", Nombre d'heure de projet : "+str(self._nbp)+
              ", Nombre d'heure de gestion : "+str(self._nbg)+", Nombre d'année d'experience : "+str(self.__exp))


class ingeS(inge):
    def __init__(self,nom,prenom,echelon,id,anb,nbt,nbp,nbg,resp):
        inge.__init__(self,nom,prenom,echelon,id,nbt,anb,nbp,nbg)
        self.__resp=resp

    def affichage(self,pays):
        print("[id="+str(self._id)+"] "+str(self._nom)+" "+str(self._prenom)+", salaire : "+str(self._echelon)+", satut : Ingenieur Sénior , Année d'embauche : "+
              str(self._anb)+" \nsite : "+str(pays)+" Nombre de jours de travail : "+str(self._nbt)+", Nombre d'heure de projet : "+str(self._nbp)+
              ", Nombre d'heure de gestion : "+str(self._nbg)+", Responsabilité : "+str(self.__resp))


Edf=multinationale('RCAT','France')
f1=filiale('RCAT-Tunisie','Tunisie',1950)
f2=filiale('RCAT-Maroc','Maroc',1960)
f3=filiale('RCAT-Allemagne','Allemagne',1970)
f4=filiale('RCAT-Belgique','Belgique',1980)

Edf.Addfili(f1)
Edf.Addfili(f2)
Edf.Addfili(f3)
Edf.Addfili(f4)

S1=directeur(1930,'Franck','Charles',7,133)
S2=admin('patrick','lepoint',2,153,2019,253,'RH')
S3=ingeS('george','delafont',3,121,2015,253,300,300,'respnsable tobogan')
S4=admin('antoine','dupont',2,154,2017,253,'comptabilité')
S5=ingeJ('michelle','blanc',2,122,2020,250,303,300,2)
S6=ingeS('laurent','maison',3,121,2015,253,300,300,'chef projet balancoire')

f1.setS(S1)
f1.setS(S2)
f1.setS(S3)
f2.setS(S4)
f3.setS(S5)
f4.setS(S6)

Edf.affichage()
