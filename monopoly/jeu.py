import random as rd
import pygame
from pygame import *
import time


class case():
    def __init__(self,nom,valeur,statue,coord):
        self.__nom=nom
        self.__valeur=valeur
        self.__statue=statue
        self.__coord=coord

    def getName(self):
        return self.__name
    def getVal(self):
        return self.__valeur
    def getStatue(self):
        return self.__statue
    def getCoord(self):
        return self.__coord

    def setStatue(self,valeur):
        self.__Statue=valeur
    def setCoord(self,valeur):
        self.__coord=valeur

class joueur():
    def __init__(self,nom,argent=10000,listProp=[]):
        self.__nom=nom
        self.__argent=argent
        self.__listProp=listProp

    def getArgent(self):
        return self.__argent
    def getList(self):
        return self.__listProp

    def setList(self,valeur):
        self.__listProp.append(valeur)

    def setArgent(self,valeur):
        self.__argent+=valeur


def de():
    n=rd.randint(1,7)
    return n

#dessin plateau
pygame.init()
size=(1000,800)
fenetre=pygame.display.set_mode(size)
pygame.FULLSCREEN
pygame.draw.line(fenetre,(255,255,255),(100,20),(990,20),8)
pygame.draw.line(fenetre,(255,255,255),(990,20),(990,700),8)
pygame.draw.line(fenetre,(255,255,255),(990,700),(100,700),8)
pygame.draw.line(fenetre,(255,255,255),(100,700),(100,20),8)
pygame.display.update()
