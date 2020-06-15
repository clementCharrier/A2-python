import stl
from stl import mesh,main
from mpl_toolkits import mplot3d
from matplotlib import pyplot
import numpy as np
def affichage_fichier_stl(lien) :


    figure= pyplot.figure()
    axes=mplot3d.Axes3D(figure)
    fichier=mesh.Mesh.from_file(lien)
    a=(fichier.vectors)
    """ ajustement de la hauteur de x"""
    hauteur =-2 # La hauteur a ajusté
    for n in range(0,len(a)):
        a[n][0][2]+=hauteur
        a[n][1][2]+=hauteur
        a[n][2][2]+=hauteur

    normale=(fichier.normals)
    print(normale)
    # print(a)
    # print(a[1])
    # print(len(a))


    """Calcule de la surface total et de chaque facette"""
    Rho=1000
    g=9.81
    STot=0
    F=0
    for i in range(0,len(a)):
        V=(a[i][1][0]-a[i][0][0],a[i][1][1]-a[i][0][1],a[i][1][2]-a[i][0][2])
        W=(a[i][2][0]-a[i][0][0],a[i][2][1]-a[i][0][1],a[i][2][2]-a[i][0][2])
        Ds=np.linalg.norm(np.cross(V,W))/2
        print(Ds)
        DsVec=Ds*normale[i]
        print(DsVec)
        Zfk=(a[i][0][2]+a[i][0][2]+a[i][0][2])/3
        if Zfk <0:
            F+=Rho*g*Zfk*DsVec
        else : F+=0
        STot+=Ds
    print(F)



    axes.add_collection3d(mplot3d.art3d.Poly3DCollection(fichier.vectors))
    scale = fichier.points.flatten()
    axes.auto_scale_xyz(scale, scale, scale)
    pyplot.show()
affichage_fichier_stl('Rectangular_HULL.stl')
