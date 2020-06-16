import outil
from stl import mesh,main
from mpl_toolkits import mplot3d
from matplotlib import pyplot
import numpy as np
def affichage_fichier_stl(lien) :


    fig= pyplot.figure()
    axes=pyplot.axes()

    fichier=mesh.Mesh.from_file(lien)
    a=(fichier.vectors)
    normale=(fichier.normals)

    normale[7][0]=1  #Vecteur normal du fichié V dans le mauvais sens des x


    #print(a[1])
    # print(len(a))
    # print(CalculForce(a,normale,0))   #Dans l'outil fichier
    # print(CalculForce(a,normale,-2))
    # print(CalculForce(a,normale,-0.5))


    """baisser la présicion"""

    #print('milieu ',Dichotomie(0,-4,0.0000001))
    #print(CalculForce(a,normale,Dichotomie(0,-4,0.0000001)))

    """Problème pour le fichier Mini_650 te V avec les vecteurs normaux"""
    hauteur,nb_rep,liste=outil.Dichotomie(2,-2,0.00001,a,normale,Rho=1000,masse=2000)
    outil.translation(2,a,hauteur)
    axes.plot(nb_rep,liste)
    pyplot.ylabel('fonction sinus')
    pyplot.xlabel("l'axe des abcisses")
    pyplot.show()


affichage_fichier_stl('Mini650_HULL.stl')

