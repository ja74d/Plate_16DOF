import gmsh
from input import *
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

#number of elements
Nel = len(node_per_element)

#Physical group--for B.C.
# This part of the code findes the Boundary Nodes

boundary_nodes_by_name1 = {}
boundary_nodes_by_name2 = {}

physical_groups = gmsh.model.getPhysicalGroups()

for dim, tag in physical_groups:
    name = gmsh.model.getPhysicalName(dim, tag)
    
    if dim == 1:
        entities = gmsh.model.getEntitiesForPhysicalGroup(dim, tag)
        
        boundary_nodes = set()
        for entity in entities:
            node_tags, _, _ = gmsh.model.mesh.getNodes(dim=1, tag=entity)
            boundary_nodes.update(node_tags)
        
        boundary_nodes_by_name2[name] = sorted(boundary_nodes)

for dim, tag in physical_groups:
    name = gmsh.model.getPhysicalName(dim, tag)
    
    if dim == 0:
        entities = gmsh.model.getEntitiesForPhysicalGroup(dim, tag)
        
        boundary_nodes = set()
        for entity in entities:
            node_tags, _, _ = gmsh.model.mesh.getNodes(dim=0, tag=entity)
            boundary_nodes.update(node_tags)
        
        boundary_nodes_by_name1[name] = sorted(boundary_nodes)
#print(boundary_nodes_by_name1)
#print(boundary_nodes_by_name2)

Boundary = {}

for key in set(boundary_nodes_by_name1.keys()).union(boundary_nodes_by_name2.keys()):
    Boundary[key] = boundary_nodes_by_name1.get(key, []) + boundary_nodes_by_name2.get(key, [])

#DOFs for each edge of the plate
left_dofs = []
for i in Boundary['Left']:
    L = [int(4*i-3), int(4*i-2), int(4*i-1), int(4*i)]
    left_dofs.append(L)

right_dofs = []
for i in Boundary['Right']:
    R = [int(4*i-3), int(4*i-2), int(4*i-1), int(4*i)]
    right_dofs.append(R)

top_dofs = []
for i in Boundary['Top']:
    T = [ int(4*i-3), int(4*i-2), int(4*i-1), int(4*i) ]
    top_dofs.append(T)

bottom_dofs = []
for i in Boundary['Bottom']:
    B = [ int(4*i-3), int(4*i-2), int(4*i-1), int(4*i) ]
    bottom_dofs.append(B)

elements = np.array(node_per_element)

#numbr of elements in x and y direction
Nex = len(Boundary['Left']) - 1
Ney = len(Boundary['Top']) - 1

a = Lx/Nex
b = Ly/Ney


gmsh.finalize()