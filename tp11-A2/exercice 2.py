class complexe():
    def __init__(self,reel,imaginaire):
        self.__reel=reel
        self.__imaginaire=imaginaire

    def getR(self):
        return self.__reel
    def getI(self):
        return self.__imaginaire

    def __add__(self,c1):
        return complexe(self.__reel+c1.__reel,self.__imaginaire+c1.__imaginaire)
    def __sub__(self,c1):
        return complexe(self.__reel-c1.__reel,self.__imaginaire-c1.__imaginaire)
    def __mul__(self,c1):
        return complexe(self.__reel*c1.__reel+(-1)*(self.__imaginaire*c1.__imaginaire),self.__imaginaire*c1.__reel+self.__reel*c1.__imaginaire)
    def __truediv__(self, c1):
        return complexe(self.__reel*c1.__reel+(+1)*(self.__imaginaire*c1.__imaginaire),self.__imaginaire*c1.__reel+self.__reel*c1.__imaginaire)
    def __eq__(self, other):
        return self.__imaginaire== other.__imaginaire and self.__reel==other.__reel
    def __ne__(self, other):
        return self.__imaginaire!= other.__imaginaire and self.__reel!=other.__reel
    def __abs__(self):
        return ((self.__reel)**2+self.__imaginaire**2)**(1/2)

if __name__=='__main__':
    c1=complexe(1,2)
    c2=complexe(4,6)
    c3=c1+c2
    c4=c1*c2
    c5=c1/c2
    c6=c1==c2
    c7=c1!=c2
    c8=abs(c1)
    print(c7)
    print(str(c5.getR())+"+i"+str(c5.getI()))
