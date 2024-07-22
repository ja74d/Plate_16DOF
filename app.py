import numpy as np
import sympy as sp


x, y = sp.symbols('x y')
#, h = sp.symbols('E h')
a1, a2, a3, a4, a5, a6, a7, a8, a9 = sp.symbols('a1 a2 a3 a4 a5 a6 a7 a8 a9')
# = sp.symbols('a')
a = 8
b = a
nu = 0.3
E = 1
h = 1

w = np.array([[1], [x], [y], [x**2], [x*y], [y**2], [x**3], [(x**2*y + x*y**2)], [y**3]])

alpha = np.array([a1, a2, a3, a4, a5, a6, a7, a8, a9])
W = alpha@w
W = W[0]

#Hermitian
Nx1 = 1-3*(x/a)**2 + 2*(x/a)**3
Ny1 = 1-3*(y/b)**2 + 2*(y/b)**3

Nx2 = a*((x/a) -2*(x/a)**2 + (x/a)**3)
Ny2 = Nx2 = b*((y/b) -2*(y/b)**2 + (y/b)**3)

Nx3 = 3*(x/a)**2 - 2*(x/a)**3
Ny3 = 3*(y/b)**2 - 2*(y/b)**3

Nx4 = a*( (x/a)**3 - (x/a)**2 )
Ny4 = b*( (y/b)**3 - (y/b)**2 )

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

second_diffN_x = []

#second derivative with respect to x
for i in range(0, len(N)):
    secon_diffN = sp.diff(sp.diff(N[i], x), x)
    #print(secon_diffN)
    second_diffN_x.append(secon_diffN)
second_diffN_x = np.array(second_diffN_x)

#second derivative with respect to y
second_diffN_y = []
for j in range(0, len(N)):
    secon_diffN = sp.diff(sp.diff(N[j], y), y)
    #print(secon_diffN)
    second_diffN_y.append(secon_diffN)
second_diffN_y = np.array(second_diffN_y)

#curve
second_diffN_xy = []
for k in range(0, len(N)):
    
    secon_diffNxy = sp.diff(sp.diff(N[k], x), y)
    #print(secon_diffN)
    second_diffN_xy.append(secon_diffNxy)
second_diffN_xy = np.array(second_diffN_xy)
print(second_diffN_xy[0])
print(sp.diff((sp.diff(N[0], x)), y))

d = E*h**3/(12*(1-nu**2))
D = d*np.array([[1, nu, 0], [nu, 1, 0], [0, 0, (1-nu)/2]])

#B = np.array([second_diffN_x[0], second_diffN_y[0], second_diffN_xy[0]])
B = []
for l in range(len(N)):
    BB = np.array([-second_diffN_x[l], -second_diffN_y[l], -2*second_diffN_xy[l]])
    B.append(BB)
#B = np.array([B])

fk11 = B[0].T@D@B[0]
k11 = sp.integrate(sp.integrate(fk11, (x, 0, a)), (y, 0, b))
print(k11)
#print(B[0])

B_ = np.array([-sp.diff(sp.diff(N[0], x), x), -sp.diff(sp.diff(N[0], y), y), -2*sp.diff(sp.diff(N[0], y), x)])
#print(B)

print(sp.integrate(sp.integrate(B_.T@D@B_, (x, 0, a)), (y, 0, b)))

