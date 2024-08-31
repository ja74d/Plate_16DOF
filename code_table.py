import numpy as np

num_nodes = 9
num_dofs_per_node = 4

node_dofs = {}

for node in range(1, num_nodes+1):
    start_dof = (node-1)*num_dofs_per_node+1
    node_dofs[node] = list(range(start_dof, start_dof+num_dofs_per_node))

"""
{
 1: [1, 2, 3, 4],
 2: [5, 6, 7, 8],
 3: [9, 10, 11, 12],
 4: [13, 14, 15, 16],
 5: [17, 18, 19, 20],
 6: [21, 22, 23, 24],
 7: [25, 26, 27, 28],
 8: [29, 30, 31, 32],
 9: [33, 34, 35, 36]
}

"""

Nex = 2
Ney = 2

code = np.zeros((Nex*Ney, 16), dtype=int)
print(code)

num_nodes_x = Nex + 1
num_nodes_y = Ney + 1

elements = []

for j in range(Ney):
    for i in range(Nex):
        n1 = j * num_nodes_x + i + 1
        n2 = n1 + 1
        n3 = n1 + num_nodes_x + 1
        n4 = n1 + num_nodes_x
        elements.append([n1, n2, n3, n4])
elements = np.array(elements)

code = []

for i in elements:
    for j in i:
        for n in node_dofs[j]:
            code.append(n)

def split_into_groups(lst, num_groups=4):
    # Calculate the size of each group
    n = len(lst)
    group_size = n // num_groups
    remainder = n % num_groups
    
    # Create the result list of lists
    groups = []
    
    start = 0
    for i in range(num_groups):
        # Determine the end index for the current group
        end = start + group_size + (1 if i < remainder else 0)
        # Append the current group to the result list
        groups.append(lst[start:end])
        # Update the start index for the next group
        start = end
    
    return groups
code = split_into_groups(code)
code = np.array(code)
print(code)