from exercice_1 import *

class BinaryTree():
    def __init__(self,root):
        self.__root=root

    def getRoot(self):
        return self.__root

    def isRoot(self,noeud):
        return self.__root==noeud

    def size(self,noeud):



# racine
N1=Node(12)
Tree=BinaryTree(N1)
# première ligne
N2=Node(5)
N3=Node(17)
N1.setLeft(N2)
N1.setRight(N3)
# deuxieme ligne
N4=Node(4)
N5=Node(6)
N6=Node(19)
N2.setLeft(N4)
N2.setRight(N5)
N3.setRight(N6)
# troisieme ligne
N7=Node(3)
N8=Node(18)
N9=Node(21)
N4.setLeft(N7)
N6.setLeft(N8)
N6.setRight(N9)

print(Tree.isRoot(N1))
