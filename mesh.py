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

#number of elements
Nel = len(node_per_element)

#Physical group--for B.C.
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

print(Boundary)

gmsh.finalize()