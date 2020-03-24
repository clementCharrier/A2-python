class multinationale():
    def __init__(self,nom,pays):
        self.__nom=nom
        self.__pays=pays
        self.__filiale=[]

    def Addfili(self,f1):
        self.__filiale.append(f1)


class filiale():
    def __init__(self,nom,pays,date):
        self.__nom=nom
        self.__pays=pays
        self.__date=date

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

class employe(salarie):
    def __init__(self,nomm,prenom,echelon,id,anb,nbt):
        salarie.__init__(self,nomm,prenom,echelon,id)
        self._anb=anb
        self._nbt=nbt

class admin(employe):
    def __init__(self,nom,prenom,echelon,id,anb,nbt,service):
        employe.__init__(self,nom,prenom,echelon,id,anb,nbt)
        self.__service=service

class inge(employe)
    def __init__(self,nom,prenom,echelon,id,anb,nbt,nbp,nbg):
        employe.__init__(self,nom,prenom,echelon,id,anb,nbt)

