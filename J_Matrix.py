import numpy as np
import sympy as sp

a = 2
b = 2

# k stands for ksi-x/a
# e stands for eta-y/b



k, e = sp.symbols('k e')

#Hermitian sape functions
Nk1 = 1-3*(k)**2 + 2*(k)**3
Ne1 = 1-3*(e)**2 + 2*(e)**3

Nk2 = a*((k) -2*(k)**2 + (k)**3)
Ne2 = b*((e) -2*(e)**2 + (e)**3)

Nk3 = 3*(k)**2 - 2*(k)**3
Ne3 = 3*(e)**2 - 2*(e)**3

Nk4 = a*( (k)**3 - (k)**2 )
Ne4 = b*( (e)**3 - (e)**2 )

#2D PLATE SHAPE FUNCTIONS
N1 = Nk1*Ne1
N2 = Nk1*Ne2
N3 = Nk2*Ne1
N4 = Nk2*Ne2
N5 = Nk3*Ne1
N6 = Nk3*Ne2
N7 = Nk4*Ne1
N8 = Nk4*Ne2
N9 = Nk3*Ne3
N10 = Nk3*Ne4
N11 = Nk4*Ne3
N12 = Nk4*Ne4
N13 = Nk1*Ne3
N14 = Nk1*Ne4
N15 = Nk2*Ne3
N16 = Nk2*Ne4

#shape functions that will be used for jacobian matrix
#N1
#N5
#N9
#N13

#global coordinations of one element:
G_cor = {1 :[[0, 2, 0], [2, 2, 0], [2, 0, 0], [0, 0, 0]] }
#print(G_cor[1])
cor = G_cor[1]
x1, x2, x3, x4 = cor[0][0], cor[1][0], cor[2][0], cor[3][0]
y1, y2, y3, y4 = cor[0][1], cor[1][1], cor[2][1], cor[3][1]

X = N1*x1 + N5*x2 + N9*x3 + N13*x4
Y = N1*y1 + N5*y2 + N9*y3 + N13*y4 

J11 = sp.diff(X, k)
J12 = sp.diff(X, e)

J21 = sp.diff(Y, k)
J22 = sp.diff(Y, e)

#Jacobian Matrix
J = np.array([ [ J11, J12 ], [ J21, J22 ] ])

#Jacobian
JJ = J11*J22 - J12*J21

J_Inv = (JJ**-1) * np.array([ [J22, -J21], [-J12, J11] ])


