import numpy as np
from input import po, Lx, d
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import griddata
from code_table import code, coordinations
from mesh import Nex, Ney
#from app import Delta
from READ_HDF5 import Delta

Delta = Delta / (po * Lx**4 / d)
D = -100*Delta

#D = [ 1.42871531e+02, -1.42871531e+02, -1.42871531e+02,  1.42871531e+02, 3.98707348e+02,  3.09391738e-14, -9.85579493e-15, -1.27970898e-13]

D_z = []

for i in range(len(code)):
    for j in range(4):
        if code[i][4*j]!=0:
            D_z.append(D[code[i][4*j]-1])
        else:
            D_z.append(0)
x = []
y = []

for i in range(len(coordinations)):
    for j in range(4):
        x.append(coordinations[i][j][0])
        y.append(coordinations[i][j][1])

z = np.array(D_z)
x = np.array(x)
y = np.array(y)


# Define grid limits for consistent scaling
grid_min, grid_max = 0, 10

# Create a grid for x and y coordinates
grid_x, grid_y = np.mgrid[grid_min:grid_max:32j, grid_min:grid_max:32j]

# Interpolate displacement data onto the grid
grid_z = griddata((x, y), z, (grid_x, grid_y), method='cubic')

# Plot the surface
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot with uniform scaling for each axis
ax.set_box_aspect([1, 1, 1])  # Equal scaling for x, y, z

surf = ax.plot_surface(grid_x, grid_y, grid_z, cmap='rainbow')
#fig.colorbar(surf, shrink=0.5, aspect= 5)
cbar = fig.colorbar(surf, shrink=0.5, aspect=5)

# Define the min and max values for colorbar normalization
z_min, z_max = np.min(grid_z), np.max(grid_z)

# Normalize the color scale to the desired range
from matplotlib.colors import Normalize
norm = Normalize(vmin=z_min, vmax=z_max)

# Update the colorbar with specific ticks: Min, Max, and some intermediate values
cbar.set_ticks([z_min, (z_min + z_max)/7, 2*(z_min + z_max)/7, 3*(z_min + z_max)/7, 4*(z_min + z_max)/7,5*(z_min + z_max)/7, 6*(z_min + z_max)/7 ,z_max])  # Set ticks at min, middle, and max
cbar.set_label("Displacement (Z)")

# Set labels and title
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.title("Deflection of SSSS Plate under Uniformly Distributed Load")

# Set limits to keep axes uniform
#ax.set_xlim(grid_min, grid_max)
#ax.set_ylim(grid_min, grid_max)
ax.set_zlim(-1, 1)

ax.view_init(elev=45, azim=45)

plt.show()