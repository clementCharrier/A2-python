class Cercle :
    def __init__(self,rayon):
        self.__ray=rayon

    def __add__(self,c1):
        return(Cercle(self.__ray+c1.__ray))
    def __lt__(self,c1):
        return self.__ray<c1.__ray
    def __le__(self,c1):
        return self.__ray>c1.__ray

if __name__=='__main__':
    c1=Cercle(2)
    c2=Cercle(4)
    c3=c1+c2
    c4=c1<c2
    c5=c2>c3
    print(c4)
print("test pour github")
