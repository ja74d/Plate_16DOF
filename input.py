#from mesh import Nex, Ney

#NUMBER OF ELEMENTS
#Nex = 32
#Ney = 32

#PLATE PROPERTIES
nu = 0.3
E = 1
h = 1
Lx = 16
Ly = 16

#BOUNDARY CONDITIONS
BCleft, BCright, BCtop, BCbottom = 'S', 'S', 'S', 'S'

#DISTRIBUTED LOAD APPLIED TO THE PLATE
po = 1

#POINT LOAD
#F_e = np.array([[250], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]])