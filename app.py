import math
import h5py
import pandas as pd
import numpy as np
import sympy as sp
from input import *
from mesh import Nex, Ney, a, b
from code_table import code
from scipy.linalg import eig

#SYMBOLES
x, y = sp.symbols('x y')

#Hermitian sape functions
Nx1 = 1-3*(x/a)**2 + 2*(x/a)**3
Ny1 = 1-3*(y/b)**2 + 2*(y/b)**3

Nx2 = a*((x/a) -2*(x/a)**2 + (x/a)**3)
Ny2 = b*((y/b) -2*(y/b)**2 + (y/b)**3)

Nx3 = 3*(x/a)**2 - 2*(x/a)**3
Ny3 = 3*(y/b)**2 - 2*(y/b)**3

Nx4 = a*( (x/a)**3 - (x/a)**2 )
Ny4 = b*( (y/b)**3 - (y/b)**2 )

#2D PLATE SHAPE FUNCTIONS
N1 = Nx1*Ny1
N2 = Nx1*Ny2
N3 = Nx2*Ny1
N4 = Nx2*Ny2
N5 = Nx3*Ny1
N6 = Nx3*Ny2
N7 = Nx4*Ny1
N8 = Nx4*Ny2
N9 = Nx3*Ny3
N10 = Nx3*Ny4
N11 = Nx4*Ny3
N12 = Nx4*Ny4
N13 = Nx1*Ny3
N14 = Nx1*Ny4
N15 = Nx2*Ny3
N16 = Nx2*Ny4

N = np.array([N1, N2, N3, N4, N5, N6, N7, N8, N9, N10, N11, N12, N13, N14, N15, N16])

#second derivative of shape functions with respect to x
second_diffN_x = []
for i in range(0, len(N)):
    secon_diffN = sp.diff(sp.diff(N[i], x), x)
    #print(secon_diffN)
    second_diffN_x.append(secon_diffN)
second_diffN_x = np.array(second_diffN_x)

#second derivative of shape functions with respect to y
second_diffN_y = []
for j in range(0, len(N)):
    secon_diffN = sp.diff(sp.diff(N[j], y), y)
    #print(secon_diffN)
    second_diffN_y.append(secon_diffN)
second_diffN_y = np.array(second_diffN_y)

#drivative of shape functions over x and y
second_diffN_xy = []
for k in range(0, len(N)):
    secon_diffNxy = sp.diff(sp.diff(N[k], x), y)
    #print(secon_diffN)
    second_diffN_xy.append(secon_diffNxy)
second_diffN_xy = np.array(second_diffN_xy)

#D matrix
d = E*h**3/(12*(1-nu**2))
D = d*np.array([[1, nu, 0], [nu, 1, 0], [0, 0, (1-nu)/2]])

B = []
for l in range(len(N)):
    BB = np.array([-1*second_diffN_x[l], -1*second_diffN_y[l], -2*second_diffN_xy[l]])
    B.append(BB)
#B = np.array([B])

#DIRECT INTEGRATION METHOD
def K(r, s):
    s = int(s)
    r = int(r)
    fk11 = B[r].T@D@B[s] 
    k = sp.integrate(sp.integrate(fk11, (x, 2, 4)), (y, 2, 4))
    return k
# diret method
#K_e1 = np.zeros((16, 16))
#for o in range(0, 16):
#    for p in range(0, 16):
#       K_e1[o, p] = K(o, p)
#
#print(K_e1)
#print()
#print(len(K_e1))

# NUMERICAL INTEGRATION METHOD
ww = [ 0.568889, 0.478629, 0.478629, 0.236927, 0.236927 ]
xx = [ 0, 0.538469, -0.538469, 0.90618, -0.90618 ]

K_e = np.zeros([16, 16])
K_gxe = np.zeros([16, 16])
K_gye = np.zeros([16, 16])

for ii in range(0, 16):
    for jj in range(0, 16):
        fun = B[ii].T @ D @ B[jj]
        fungx = sp.diff(N[ii], x)*sp.diff(N[jj], x)
        fungy = sp.diff(N[ii], y)*sp.diff(N[jj], y)
        ke=0
        kgxe=0
        kgye=0
        for l1 in range(0, 5):
            for l2 in range(0, 5):
                x1 = 0.5*xx[l1]*a + 0.5*a
                y1 = 0.5*xx[l2]*b + 0.5*b

                fun_evaluated = fun.subs({x: x1, y: y1}).evalf()
                fun_evaluatedgx = fungx.subs({x: x1, y: y1}).evalf()
                fun_evaluatedgy = fungy.subs({x: x1, y: y1}).evalf()
                ke += (a*b/4) * ww[l1] * ww[l2] * fun_evaluated
                kgxe += (a*b/4)* ww[l1] * ww[l2] * fun_evaluatedgx
                kgye += (a*b/4)* ww[l1] * ww[l2] * fun_evaluatedgy
                K_e[ii, jj] = ke
                K_gxe[ii, jj] = kgxe
                K_gye[ii, jj] = kgye
#print(K_e)
#F matrix
#DISTRIBUTED LOAD
F_e = np.zeros((16, 1))
F = []

for bb in range(0, 16):
    N = N.T
    f = sp.integrate(sp.integrate(po*N[bb], (x, 0, a)), (y, 0, b))
    F.append(f)

for m in range(0, 16):
    F_e[m, 0] = F[m]
#F_e = (p0*a*b)*np.array([1/4, a/24, b/24, (a*b)/14, 1/4, -a/24, b/24, -(a*b)/144, 1/4, -a/24, -b/24, (a*b)/144, 1/4, a/24, -b/24, -(a*b)/144])

#Assembling
num_dofs = np.max(code)

K = np.zeros((num_dofs, num_dofs))
Kgx = np.zeros((num_dofs, num_dofs))
Kgy = np.zeros((num_dofs, num_dofs))
F = np.zeros(num_dofs)

num_elements = code.shape[0]

for elem in range(num_elements):
    for i in range(16):
        if code[elem, i] != 0:
            for j in range(16):
                if code[elem, j] != 0:
                    K[code[elem, i] - 1, code[elem, j] - 1] += K_e[i, j]
                    #Kgx[code[elem, i] - 1, code[elem, j] - 1] += K_gxe[i, j]
                    #Kgy[code[elem, i] - 1, code[elem, j] - 1] += K_gye[i, j]
            F[code[elem, i] - 1] += F_e[i, 0]

Delta = np.linalg.inv(K) @ F

#eigenvaluesx, eigenvectorsx = eig(K, Kgx)
#eigenvaluesy, eigenvectorsy = eig(K, Kgy)
#print(eigenvalues)
#Load Factor

#ncr = float(min(eigenvaluesx))
#ncr = ncr.real

midelem = int(np.fix(Ney / 2) * Nex + np.fix(Nex / 2) + 1)

corXmid = (Nex / 2 - np.fix(Nex / 2)) * a
corYmid = (Ney / 2 - np.fix(Ney / 2)) * b


Wmid = 0
for i in range(16):
    if code[midelem - 1, i] != 0:  # Zero-based indexing in Python
        Wmid += float(N[i].subs(x, corXmid).subs(y, corYmid) * Delta[code[midelem - 1, i] - 1])

#NON-DIMENTIONAL DISPLACEMENT
wmidND = Wmid / (po * Lx**4 / d)
#wmidND = Wmid*((E*h**3)/(Lx**4*po))

# Output the result
print(f"number of elements: {Nex*Ney}")
print(f"displacement at midpoint: {Wmid}")
print(f"Non-dimensional displacement at midpoint: {wmidND}")
#print('critical load: ',ncr)
#print(Delta)

#Displacement Based on element number and node number


#print(Delta)
#Delta = Delta / (po * Lx**4 / d)

# Create an HDF5 file
with h5py.File(f'({file_name}).h5', 'w') as hdf:

    # Create a group for matrices
    matrices_group = hdf.create_group('Matrices')
    matrices_group.create_dataset('Stiffness_Matrix', data=K)
    matrices_group.create_dataset('Force_Matrix', data=F)

    # Create a group for nodal data
    nodal_group = hdf.create_group('Nodal_Data')
    nodal_group.create_dataset('Nodal_Displacement', data=Delta)

    # You can also add attributes for metadata
    hdf.attrs['Description'] = 'Finite Element Analysis Results'
    hdf.attrs['Version'] = '1.0'

print(f"Data has been saved in '{file_name}.h5'")