#NUMBER OF ELEMENTS
Nex = 8
Ney = 8

#PLATE PROPERTIES
nu = 0.3
E = 1
h = 1
Lx = 8
Ly = 8

a = Lx/Nex
b = Ly/Ney

#BOUNDARY CONDITIONS
BCleft, BCright, BCtop, BCbottom = 'S', 'S', 'S', 'S'

#DISTRIBUTED LOAD APPLIED TO THE PLATE
po = 1

#POINT LOAD
#F_e = np.array([[250], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]])