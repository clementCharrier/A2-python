class Node():
    def __init__(self,val,right=None,left=None):
        self.__val=val
        self.__right=right
        self.__left=left

    def getVal(self):
        return self.__val
    def getRight(self):
        return self.__right
    def getLeft(self):
        return self.__left

    def setVal(self,valeur):
        self.__valeur=valeur
    def setRight(self,valeur):
        self.__right=valeur
    def setLeft(self,valeur):
        self.__left=valeur

# # racine
# N1=Node(12)
# # première ligne
# N2=Node(5)
# N3=Node(17)
# N1.setLeft(N2)
# N1.setRight(N3)
# # deuxieme ligne
# N4=Node(4)
# N5=Node(6)
# N6=Node(19)
# N2.setLeft(N4)
# N2.setRight(N5)
# N3.setRight(N6)
# # troisieme ligne
# N7=Node(3)
# N8=Node(18)
# N9=Node(21)
# N4.setLeft(N7)
# N6.setLeft(N8)
# N6.setRight(N9)

