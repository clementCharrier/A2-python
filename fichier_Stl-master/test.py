import stl
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
        for n in range(0,len(a)): #on parcour pour le nombre de facettes

            """ajustement de la hauteur de la coque """
            a[n][0][2]+=hauteur
            a[n][1][2]+=hauteur
            a[n][2][2]+=hauteur

            """Calcule de la surface total et de chaque facette"""
            V=(a[n][1][0]-a[n][0][0],a[n][1][1]-a[n][0][1],a[n][1][2]-a[n][0][2])
            W=(a[n][2][0]-a[n][0][0],a[n][2][1]-a[n][0][1],a[n][2][2]-a[n][0][2])
            Ds=np.linalg.norm(np.cross(V,W))/2
            Stot+=Ds #surface totale de la coque
            # print(Ds)
            DsVec=Ds*normale[n]

            """Calcule de la hauteur d'une facette """
            Zfk=(a[n][0][2]+a[n][1][2]+a[n][2][2])/3
            # print(a[i][0][2],a[i][0][2],a[i][0][2])

            """condition pour que une facette soit compté comme immergé """
            if Zfk <0:
                F_Archimede+=Rho*g*Zfk*DsVec
            else : F_Archimede+=0

        """calcule du poid de la coque selon l'axe Oz"""
        masse=1000 #g
        F_Poid=(0,0,masse*g)

        """On determine la norme de la resultante du poid et d'archimède"""
        normeArchimede=np.linalg.norm(F_Archimede)
        normePoid=np.linalg.norm(F_Poid)

        difference= normePoid-normeArchimede #Si <0 alors Poid < Archimede sinon >0 alors Poid > Archimede

        return difference

    def Dichotomie(Haut,Bas,Presicion):
        ecart=Haut-Bas
        Zmilieu=0
        while ecart>Presicion:
            difference=CalculForce(a,normale,Zmilieu)
            if difference>0 :
                Haut=Zmilieu
            else : Bas=Zmilieu
            ecart=Haut-Bas

        return Zmilieu

    figure= pyplot.figure()
    axes=mplot3d.Axes3D(figure)
    fichier=mesh.Mesh.from_file(lien)
    a=(fichier.vectors)
    normale=(fichier.normals)
    print(normale)
    print(a)
    # print(a[1])
    # print(len(a))
    print(Dichotomie(0,-4,0.01))
    axes.add_collection3d(mplot3d.art3d.Poly3DCollection(fichier.vectors))
    scale = fichier.points.flatten()
    axes.auto_scale_xyz(scale, scale, scale)

    pyplot.show()



affichage_fichier_stl('Cylindrical_HULL.stl')
