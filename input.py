from datetime import datetime
#from mesh import Nex, Ney

date_time = datetime.now()

#File name
file_name = 'testfile'
file_name = f'{file_name}_Saved at {date_time}'

#NUMBER OF ELEMENTS
#Nex = 32
#Ney = 32

#PLATE PROPERTIES
nu = 0.3
E = 1
h = 1
Lx = 10
Ly = 10

#BOUNDARY CONDITIONS
BCleft, BCright, BCtop, BCbottom = 'S', 'S', 'S', 'S'

#DISTRIBUTED LOAD APPLIED TO THE PLATE
po = 1

d = E*h**3/(12*(1-nu**2))

#POINT LOAD
#F_e = np.array([[250], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]])
