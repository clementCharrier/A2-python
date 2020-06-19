import numpy as np
U=(-4,0,0)
V=(-4,1,1)
print(np.cross(U,V))
Ds=(np.linalg.norm(np.cross(U,V)))/2
print(Ds)
