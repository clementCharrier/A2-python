class rational():
    def __init__(self,numerator, denominator):
        self.__numerator=numerator
        self.__denominator=denominator

    def __add__(self, other):
        return rational((self.__numerator*other.__denominator)+(other.__numerator*self.__denominator),self.__denominator*other.__denominator)
    def __sub__(self, other):
        return rational((self.__numerator*other.__denominator)-(other.__numerator*self.__denominator),self.__denominator*other.__denominator)
    def __lt__(self, other):
        return (self.__numerator/self.__denominator)<(other.__numerator/other.__denominator)
    def __le__(self, other):
        return (self.__numerator/self.__denominator)>(other.__numerator/other.__denominator)
    def __eq__(self, other):
        return (self.__numerator/self.__denominator)==(other.__numerator/other.__denominator)
    def __mul__(self, other):
        return rational((self.__numerator*other.__numerator),(self.__denominator*other.__denominator))
    def __truediv__(self, other):
        return rational((self.__numerator*other.__denominator),(self.__denominator*other.__numerator))
    def getN(self):
        return self.__numerator
    def getD(self):
        return self.__denominator




if __name__=='__main__':
    r1=rational(1,2)
    r2=rational(2,3)
    r3=r1+r2
    r4=r1-r2
    r5=r1*r2
    r6=r1/r2
    r7=r1==r2
    r8=r1<r2
    r9=r1>r2
    print(str(r3.getN())+'/'+str(r3.getD()))
    print(str(r4.getN())+'/'+str(r4.getD()))
    print(str(r5.getN())+'/'+str(r5.getD()))
    print(str(r6.getN())+'/'+str(r6.getD()))
    print(r7)

