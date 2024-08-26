import gmsh
import numpy as np

gmsh.initialize()
gmsh.option.setNumber("General.Terminal", 1)
gmsh.open('/home/javad/Plate_16DOF/Mesh_models/msh.msh')

node_tags, node_coords, _ = gmsh.model.mesh.getNodes()

element_types, element_tags, element_node_tags = gmsh.model.mesh.getElements()

node_coords = node_coords.reshape((-1, 3))
#print(element_tags[1])
element_nodes = int(len(element_node_tags[1])/4)

El_nodes = []
for i in range(0,16,4):
    nd = element_node_tags[1][i:i+4]
    nd = list(nd)
    El_nodes.append(nd)


for  elem_type, elem_tag, elem_nodes in zip(element_types, element_tags, element_node_tags):
    num_nodes_per_elm = len(elem_nodes)//len(elem_tag)
    #print(f"Element Type: {elem_type}, Number of Elements: {len(elem_tag)}")

    for i in range(len(elem_tag)):
        elem_node_indices = elem_nodes[i * num_nodes_per_elm:(i + 1) * num_nodes_per_elm]
        elem_node_coords = node_coords[elem_node_indices - 1]  # Get the coordinates for these nodes

        #if elem_type == 3:
            #print(elem_tag)
            #print(f"  Element {elem_tag[i]} has nodes with coordinates:")
            #for j, node_coord in enumerate(elem_node_coords):
            #    print(f"    Node {elem_node_indices[j]}: {node_coord}")


gmsh.finalize()