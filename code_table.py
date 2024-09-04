import numpy as np
from collections import Counter


Nex = 2
Ney = 2

def code_table(Nex, Ney):
    num_nodes = (Nex+1)*(Ney+1)
    node_dofs = {}

    for node in range(1, num_nodes+1):
        start_dof = (node-1)*4+1
        node_dofs[node] = list(range(start_dof, start_dof+4))

    code = np.zeros((Nex*Ney, 16), dtype=int)
    global elements
    elements = []

    for j in range(Ney):
        for i in range(Nex):
            n1 = j * (Nex+1) + i + 1
            n2 = n1 + 1
            n3 = n1 + (Nex+1) + 1
            n4 = n1 + (Nex+1)
            elements.append([n1, n2, n3, n4])
    elements = np.array(elements)
    code = np.zeros((len(elements), 16), dtype=int)

    # Fill the code table
    for i, element in enumerate(elements):
        element_dofs = []
        for node in element:
            element_dofs.extend(node_dofs[node])
        code[i, :] = element_dofs
    
    
    return code
code_table(2, 2)
#print(elements)

def Boundary_nodes(elements):
    all_nodes = [node for element in elements for node in element]
    node_counts = Counter(all_nodes)
    
    edge_nodes = list({ node for node, count in node_counts.items() if count==1 })
    edge_nodes2 = list({ node for node, count in node_counts.items() if count==2 })
    boundary_nodes = []
    for i in edge_nodes:
        boundary_nodes.append(i)
    for j in edge_nodes2:
        boundary_nodes.append(j)
    return boundary_nodes

boundary_nodes = sorted(Boundary_nodes(elements))

top_nodes = boundary_nodes[0:Ney+1]
bottom_nodes = boundary_nodes[-(Ney+1):]

left_nodes = []
for i in range(1, Nex+2):
    left_nodes.append( (Nex+1)*(i-1)+1 )

right_nodes = []
for i in range(1, Nex+2):
    right_nodes.append( (Nex+1)*i )

