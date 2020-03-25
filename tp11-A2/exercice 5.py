import numpy as np
class matrice():
    def __init__(self,data):
        self.__mat=data

    def __add__(self,other):
        data=self.__matrice+other.__matrice
        return matrice(data)
    def __iadd__(self, other):
        self.__matrice+=other.__matrice
    def __isub__(self, other):
        self.__matrice-=other.__matrice
    def __sub__(self,other):
        data=self.__matrice-other.__matrice
        return matrice(data)
    def __mul__(self, other):
        data=self.__matrice.dot(other.__matrice)
        return matrice(data)
    def __truediv__(self, other):
        inver=np.linalg.inv(other.__matrice)
        data=self.__matrice.dot(inver)
        return matrice(data)
    def __imul__(self, other):
        self.__matrice=self.__matrice.dot(other.__matrice)
    def __eq__(self, other):
        return np.array_equal(self.__matrice,other.__matrice)

if __name__=='__main__':
    mat1=np.array([[1,0],[0,1]])
    mat2=np.array([[2,1],[4,5]])
    mat3=mat1+mat2
    mat4=mat1-mat2
    mat5=mat1*mat2
    mat6=mat1==mat2
    mat1+=mat2
    print(mat5)
    mat1-=mat2

    mat1*=mat2
