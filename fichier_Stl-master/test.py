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
    b=(fichier.normals)
    # print(b)
    # print(a)
    # print(a[1])
    # print(len(a))
    """Calcule de la surface total et de chaque facette"""
    DsTot=0
    for i in a :
        V=(i[1][0]-i[0][0],i[1][1]-i[0][1],i[1][2]-i[0][2])
        W=(i[2][0]-i[0][0],i[2][1]-i[0][1],i[2][2]-i[0][2])
        Ds=np.linalg.norm(np.cross(V,W))/2
        print(Ds)
        DsTot+=Ds
    print(DsTot)

    axes.add_collection3d(mplot3d.art3d.Poly3DCollection(fichier.vectors))
    scale = fichier.points.flatten()
    axes.auto_scale_xyz(scale, scale, scale)
    pyplot.show()
affichage_fichier_stl('Mini650_HULL.stl')
