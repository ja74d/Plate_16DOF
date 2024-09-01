import numpy as np

def code_table(Nex, Ney):
    num_nodes = (Nex+1)*(Ney+1)
    node_dofs = {}

    for node in range(1, num_nodes+1):
        start_dof = (node-1)*4+1
        node_dofs[node] = list(range(start_dof, start_dof+4))

    code = np.zeros((Nex*Ney, 16), dtype=int)
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