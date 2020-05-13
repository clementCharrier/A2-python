from exercice_1 import *

class BinaryTree():
    def __init__(self,root):
        self.__root=root

    def getRoot(self):
        return self.__root

    def isRoot(self,noeud):
        return self.__root==noeud



    def size(self,noeud):
        if noeud==None :
            return 0
        if noeud.getLeft()==None and noeud.getRight()==None :
            return 1
        else :
            return 1+self.size(noeud.getLeft())+ self.size(noeud.getRight())



    def printValues(self,noeud):
        if noeud==None :
            return ""
        if noeud.getLeft()==None and noeud.getRight()==None :
            return str(noeud.getVal())
        else :
            return self.printValues(noeud.getLeft()) +" "+ self.printValues(noeud.getRight()) +" "+str(noeud.getVal())

    def sumValues(self,noeud):
        if noeud==None :
            return 0
        if noeud.getLeft()==None and noeud.getRight()==None :
            return noeud.getVal()
        else :
            return noeud.getVal()+self.sumValues(noeud.getLeft())+self.sumValues(noeud.getRight())


    def numberLeaves(self,noeud):
        if noeud==None :
            return 0
        if noeud.getLeft()==None and noeud.getRight()==None :
            return 1
        else :
            return self.numberLeaves(noeud.getLeft())+self.numberLeaves(noeud.getRight())

    def numlberInternalNodes(self,noeud):
        if noeud==None :
            return 0
        if noeud.getLeft()==None and noeud.getRight()==None :
            return 0
        else :
            return 1 + self.numberLeaves(noeud.getLeft())+self.numberLeaves(noeud.getRight())



    def height(self,noeud):
        if noeud is None :
            return 0
        if noeud.getLeft()==None and noeud.getRight()==None:
            return 1
        else:
            g=1+self.height(noeud.getLeft())
            d=1+self.height(noeud.getRight())
            return max(g-1,d-1) #-1 car on enlève le premier


    def belongs(self,noeud,valeur):
        if noeud is None:
            return False
        if noeud.getVal()==valeur:
            return True
        else :
            a=self.belongs(noeud.getLeft(),valeur)
            b=self.belongs(noeud.getRight(),valeur)
            if a==True or b==True :
                return True
            else :return False


    def ancestor(self,noeud,valeur):

        if noeud is None:
            return ""
        if noeud.getVal()==valeur:
            return True
        else :
            a=self.ancestor(noeud.getLeft(),valeur)
            b=self.ancestor(noeud.getRight(),valeur)
            if a==True or b==True :
                print(noeud.getVal())
                return True


    def decandant(self,noeud,valeur):
        if noeud is None:
            return ""
        if noeud.getVal()==valeur:
            return True
        else :
            a=self.decandant(noeud.getLeft(),valeur)
            b=self.decandant(noeud.getRight(),valeur)
            if a==True or b==True :
                return str(noeud.getVal())
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
print("la taille de l'arbre est :",Tree.size(N1))
print("la liste des valeurs de l'arbre ",Tree.printValues(N1))
print("somme totale ",Tree.sumValues(N1))
print("Nombre de feuilles ",Tree.numberLeaves(N1))
print("Nombre de noeud interne ", Tree.numlberInternalNodes(N1))
print("La taille de l'arbre est " ,Tree.height(N1))
print("La valeur appartient à l'arbre ",Tree.belongs(N1,19))
print("teste",Tree.ancestor(N1,19))
print("je ne suis que fougere", Tree.decandant(N1,19))
