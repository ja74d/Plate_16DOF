from mesh import node_coords, elements
import matplotlib.pyplot as plt
import numpy as np

# Convert node coordinates to NumPy array
nodes = np.array(node_coords)

# Ensure the number of tensions matches the number of nodes
tensions = np.random.rand(len(nodes)) * 20  # Example: Random tension values for each node

# Plotting the tension distribution using pcolormesh for quadrilateral elements
plt.figure()

# Loop through each quadrilateral element
for elem in elements:
    x = nodes[elem, 0]  # x-coordinates of the 4 corner nodes
    y = nodes[elem, 1]  # y-coordinates of the 4 corner nodes
    t = tensions[elem].mean()  # Mean tension in the element (for color)
    
    # Create a filled polygon (quadrilateral)
    plt.fill(x, y, color=plt.cm.viridis(t / max(tensions)), edgecolor='k')

# Add colorbar and labels
plt.colorbar(plt.cm.ScalarMappable(cmap='viridis'), label="Tension (Pa)")
plt.title("Nodal Tension Distribution in the Plate (Quadrilateral Elements)")
plt.xlabel("x-coordinate")
plt.ylabel("y-coordinate")
plt.show()