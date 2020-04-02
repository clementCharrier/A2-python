import numpy as np
import turtle
import pygame
from pygame import *
import random as rd
#
# class joueur():
#     def __init__(self,tour,matrice):
#
# class ordinateur():
class case():
    def __init__(self,coord,statut,position_matrice):
        self.__coord=coord
        self.__statut=statut
        self.__position=position_matrice

    def getCoord(self):
        return self.__coord
    def getStatut(self):
        return self.__statut
    def getPos(self):
        return self.__position

    def setCoord(self,valeur):
        self.__coord=valeur
    def setStatut(self,valeur):
        self.__statut=valeur
    def setPos(self,valeur):
        self.__position=valeur


def condVictory(mat):
    i=0
    continuer=1
    for lines in mat:
        condL=0
        i+=1
        for j in lines:
            condL+=j

            if condL==3:
                print("GAGNE sur la ligne "+str(i))
                continuer=0
                break
            elif condL==12:
                print("GAGNE JOUEUR Ordinateur")
                continuer=0
                break

    i=0
    for colonne in range(3):
        i+=1
        condC=0

        for lines in range(3):
            condC+=mat[lines,colonne]
            if condC==3:
                print("GAGNE sur la colonne "+str(i))
                continuer=0
                break
            elif condC==12:
                print("GAGNE JOUEUR Ordinateur colonne")
                continuer=0
                break

    condD=0
    condOD=0
    for i in range(3):
        condD+=mat[i,i]
        condOD+=mat[i,2-i]
        if condD==3 or condOD==3:
            print("GAGNE sur la colonne "+str(i))
            continuer=0
            break
        elif condD==12 or condOD==12:
            print("GAGNE JOUEUR Ordinateur diagonale")
            continuer=0
            break

    nul=0
    for lines in range(3):
        for j in range(3):
            nul+=mat[lines,j]
            if nul==21 or nul==24:
                print("Match nul")
                continuer=0
                quit()
                exit()
                break
    return continuer


def robot(mat,list_case,list_proba):
    passe=0
    for indice in range(8):
        compteur=0
        for case in range(3):
            # print(combinaison[liste_proba[indice]][case].getPos())
            compteur+=mat[combinaison[list_proba[indice]][case].getPos()[0],combinaison[list_proba[indice]][case].getPos()[1]]
            if compteur==2:
                for i in range (3):
                    if (combinaison[list_proba[indice]][i].getStatut())==0:
                        mat[combinaison[list_proba[indice]][i].getPos()[0],combinaison[list_proba[indice]][i].getPos()[1]]=4
                        combinaison[list_proba[indice]][i].setStatut(4)
                        pygame.draw.circle(fenetre,(255,255,255),combinaison[list_proba[indice]][i].getCoord(),30,5)
                        pygame.display.update()
                        passe=1
                        print(matrice_gen)

                        break

    continuer=condVictory(mat)
    while passe==0 :
        X=rd.randint(0,8)
        # print(list_case[X].getStatut(),list_case[X].getPos())
        if list_case[X].getStatut()==0:
            list_case[X].setStatut(4)
            mat[list_case[X].getPos()[0],list_case[X].getPos()[1]]=4
            pygame.draw.circle(fenetre,(255,255,255),list_case[X].getCoord(),30,5)
            pygame.display.update()
            passe=1
            print(matrice_gen)
        continuer=condVictory(mat)

    # continuer=condVictory(mat)
    tour=False
    return tour,continuer





#programme principale
matrice_gen=np.array([[0,0,0],
                      [0,0,0],
                      [0,0,0]])
# matrice_gen[0,0]=2
# matrice_gen[0,1]=2
# matrice_gen[0,2]=2
print(matrice_gen)
condVictory(matrice_gen)
liste_proba=['L1','L2','L3','C1','C2','C3','D1','D2'] # liste des combinaisons pour gagner
""" L : Ligne , C : Colonne , D : Diagonale """


#-------------------------------Dessin_plateau------
# turtle.setup(600,600)
# turtle.speed('fastest')
# turtle.pensize(10)
#
# turtle.up()
# turtle.goto(-300,-100)
# turtle.down()
# turtle.goto(300,-100)
# turtle.up()
# turtle.goto(300,100)
# turtle.down()
# turtle.goto(-300,100)
# turtle.up()
# turtle.goto(-100,300)
# turtle.down()
# turtle.goto(-100,-300)
# turtle.up()
# turtle.goto(100,-300)
# turtle.down()
# turtle.goto(100,300)

#-------------------------------------creation_des_cases-------------
c1=case((100,100),0,(0,0))
c2=case((300,100),0,(0,1))
c3=case((500,100),0,(0,2))
c4=case((500,300),0,(1,2))
c5=case((500,500),0,(2,2))
c6=case((300,500),0,(2,1))
c7=case((100,500),0,(2,0))
c8=case((100,300),0,(1,0))
c9=case((300,300),0,(1,1))
liste_case=[c1,c2,c3,c8,c9,c4,c7,c6,c5] #Ligne par ligne
""" Pour le statut, 0 : non prise , 1 : prise par le joueur 1 , 4 :prise par l'ordinateur """
combinaison={'L1': [c1,c2,c3],
             'L2': [c8,c9,c4],
             'L3': [c7,c6,c5],
             'C1': [c1,c8,c7],
             'C2': [c2,c9,c6],
             'C3': [c3,c4,c5],
             'D1': [c1,c9,c5],
             'D2': [c3,c9,c7]}
#------------------------------------Déroulement_du_jeu---------------
pygame.init()
size=(600,600)
fenetre = pygame.display.set_mode((600, 600))
# print(c9.getStatut())
tour=False
"""False ==> au joueur de jouer , True ==> à l'ordi de jouer"""


continuer =1
while continuer:
    pygame.draw.line(fenetre,(255,255,255),(0,200),(600,200),10)
    pygame.draw.line(fenetre,(255,255,255),(0,400),(600,400),10)
    pygame.draw.line(fenetre,(255,255,255),(200,0),(200,600),10)
    pygame.draw.line(fenetre,(255,255,255),(400,0),(400,600),10)
    pygame.display.update()

    for event in pygame.event.get():

        if event.type == MOUSEBUTTONDOWN:
            if event.button==1:
                coordonne_clic=(event.pos[0],event.pos[1])

                if 0<coordonne_clic[0]<200 and 0<coordonne_clic[1]<200 and c1.getStatut()==0 :
                    pygame.draw.rect(fenetre,(255,255,255),(75,75,50,50))
                    c1.setStatut(1)
                    pygame.display.update()
                    matrice_gen[0,0]=1
                    print(matrice_gen)
                    tour=True
                if 200<coordonne_clic[0]<400 and 0<coordonne_clic[1]<200 and c2.getStatut()==0 :
                    pygame.draw.rect(fenetre,(255,255,255),(275,75,50,50))
                    c2.setStatut(1)
                    pygame.display.update()
                    matrice_gen[0,1]=1
                    print(matrice_gen)
                    tour=True
                if 400<coordonne_clic[0]<600 and 0<coordonne_clic[1]<200 and c3.getStatut()==0 :
                    pygame.draw.rect(fenetre,(255,255,255),(475,75,50,50))
                    c3.setStatut(1)
                    pygame.display.update()
                    matrice_gen[0,2]=1
                    print(matrice_gen)
                    tour=True
                if 400<coordonne_clic[0]<600 and 200<coordonne_clic[1]<400 and c4.getStatut()==0 :
                    pygame.draw.rect(fenetre,(255,255,255),(475,275,50,50))
                    c4.setStatut(1)
                    pygame.display.update()
                    matrice_gen[1,2]=1
                    print(matrice_gen)
                    tour=True
                if 400<coordonne_clic[0]<600 and 400<coordonne_clic[1]<600 and c5.getStatut()==0 :
                    pygame.draw.rect(fenetre,(255,255,255),(475,475,50,50))
                    c5.setStatut(1)
                    pygame.display.update()
                    matrice_gen[2,2]=1
                    print(matrice_gen)
                    tour=True
                if 200<coordonne_clic[0]<400 and 400<coordonne_clic[1]<600 and c6.getStatut()==0 :
                    pygame.draw.rect(fenetre,(255,255,255),(275,475,50,50))
                    c6.setStatut(1)
                    pygame.display.update()
                    matrice_gen[2,1]=1
                    print(matrice_gen)
                    tour=True
                if 0<coordonne_clic[0]<200 and 400<coordonne_clic[1]<600 and c7.getStatut()==0 :
                    pygame.draw.rect(fenetre,(255,255,255),(75,475,50,50))
                    c7.setStatut(1)
                    pygame.display.update()
                    matrice_gen[2,0]=1
                    print(matrice_gen)
                    tour=True
                if 0<coordonne_clic[0]<200 and 200<coordonne_clic[1]<400 and c8.getStatut()==0 :
                    pygame.draw.rect(fenetre,(255,255,255),(75,275,50,50))
                    c8.setStatut(1)
                    pygame.display.update()
                    matrice_gen[1,0]=1
                    print(matrice_gen)
                    tour=True
                if 200<coordonne_clic[0]<400 and 200<coordonne_clic[1]<400 and c9.getStatut()==0 :
                    pygame.draw.rect(fenetre,(255,255,255),(275,275,50,50))
                    c9.setStatut(1)
                    pygame.display.update()
                    matrice_gen[1,1]=1
                    print(matrice_gen)
                    tour=True

        elif event.type ==KEYDOWN and event.key==K_ESCAPE :
            continuer=0

    if tour==True:
        tour,continuer=robot(matrice_gen,liste_case,liste_proba)

    continuer=condVictory(matrice_gen)


# turtle.exitonclick()
