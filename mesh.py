import gmsh
import numpy as np

gmsh.initialize()
gmsh.option.setNumber("General.Terminal", 1)
gmsh.open('/home/javad/Plate_16DOF/Mesh_models/msh.msh')

#Nodes info
node_tags, node_coords, _ = gmsh.model.mesh.getNodes()
#Node tags = a list of all nodes in mesh
#Node coords = a list of coordinations of nodes

#Elements info
element_types, element_tags, node_tages_per_element = gmsh.model.mesh.getElements()
#node_coords = node_coords.reshape((-1, 3))

# rectangular elements are specified by "element_tags[1]"

# A list that contains lists of nodes for each elemete
node_per_element = node_tages_per_element[1].reshape(-1, 4)
