import outil
from stl import mesh,main
from mpl_toolkits import mplot3d
from matplotlib import pyplot
import numpy as np
def affichage_fichier_stl(lien) :

    def CalculForce(a,normale,hauteur):
        F_Archimede=0
        Rho=1000
        g=9.81
        Stot=0
        """ajustement de la hauteur de la coque """
        outil.translation(2,a,hauteur)

        for n in range(0,len(a)): #on parcour pour le nombre de facettes

            """Calcule de la surface total et de chaque facette"""
            U=outil.calculVecteur(a[n][0],a[n][1])
            V=outil.calculVecteur(a[n][0],a[n][2])
            Ds=outil.norme(outil.produitVectoriel(U,V))
            Stot+=Ds #surface totale de la coque
            DsVec=Ds*normale[n]

            """Calcule de la hauteur d'une facette """
            Zfk=outil.calculeHauteurFacette(a[n][0],a[n][1],a[n][2])

            """condition pour que une facette soit compté comme immergé """
            if Zfk <0:
                F_Archimede+=Rho*g*Zfk*DsVec
            else : F_Archimede+=0

        """On remet la hauteur de la coque"""
        outil.translation(2,a,-hauteur)

        """calcule du poid de la coque selon l'axe Oz"""
        masse=2000 #g
        F_Poid=(0,0,-1*masse*g)

        """On determine la norme de la resultante du poid et d'archimède"""

        normeArchimede=np.linalg.norm(F_Archimede)
        print("archi ",F_Archimede)
        print("poid ",F_Poid)
        normePoid=np.linalg.norm(F_Poid)

        difference= normeArchimede-normePoid #Si <0 alors Poid < Archimede sinon >0 alors Poid > Archimede

        return difference

    def Dichotomie(Haut,Bas,Presicion):
        ecart=Bas-Haut
        while abs(ecart)>Presicion:
            Zmilieu=(Haut+Bas)/2
            print("ecart ",ecart," haut ",Haut," bas ",Bas," Zmilieu ",Zmilieu)
            difference=CalculForce(a,normale,Zmilieu)
            print("diff ",difference)
            if difference<0 :
                Haut=Zmilieu

            else : Bas=Zmilieu
            ecart=Haut-Bas


        return Zmilieu

    figure= pyplot.figure()
    axes=mplot3d.Axes3D(figure)
    fichier=mesh.Mesh.from_file(lien)
    a=(fichier.vectors)
    normale=(fichier.normals)
    normale[7][0]=1


    #print(a[1])
    # print(len(a))
    # print(CalculForce(a,normale,0))
    # print(CalculForce(a,normale,-2))
    # print(CalculForce(a,normale,-0.5))


    """Ca ne marche pas"""
    print('milieu ',Dichotomie(0,-4,0.0000001))
    print(CalculForce(a,normale,Dichotomie(0,-4,0.0000001)))
    axes.add_collection3d(mplot3d.art3d.Poly3DCollection(fichier.vectors))
    scale = fichier.points.flatten()
    axes.auto_scale_xyz(scale, scale, scale)

    pyplot.show()



affichage_fichier_stl('Rectangular_HULL.stl')
