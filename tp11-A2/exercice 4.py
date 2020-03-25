class Duree():
    def __init__(self,heure,minute,seconde):
        self.__heure=heure
        self.__minute=minute
        self.__seconde=seconde

    def affichage(self):
        print(str(self.__heure)+'h'+str(self.__minute)+'m'+str(self.__seconde))

    def __add__(self, other):
        minute=0
        heure=0
        seconde=self.__seconde+other.__seconde
        if seconde>=60:
            minute+=1
            seconde-=60
        minute+=self.__minute+other.__minute
        if minute>=60 :
            heure+=1
            minute-=60
        heure+=self.__heure+other.__heure
        return Duree(heure,minute,seconde)

if __name__=='__main__':
    d1=Duree(2,35,20)
    d2=Duree(1,35,45)
    d3=d1+d2
    d3.affichage()



