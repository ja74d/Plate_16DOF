import numpy as np

# Number of elements in x and y directions
Nex = 2  # For example, you can change it according to your mesh
Ney = 2  # For example, you can change it according to your mesh

# Total number of elements
num_elements = Nex * Ney

# Number of DOFs per element
num_dofs = 16

# Initialize the code table
code = np.zeros((num_elements, num_dofs), dtype=int)

# Generate the code table directly
for j in range(Ney):
    for i in range(Nex):
        ne = j * Nex + i  # Element number
        
        # Calculate the DOFs for each element and directly populate the `code` table
        code[ne, 0:4] = [(j * (Nex + 1) + i) * 4 + k + 1 for k in range(4)]
        code[ne, 4:8] = [(j * (Nex + 1) + (i + 1)) * 4 + k + 1 for k in range(4)]
        code[ne, 8:12] = [((j + 1) * (Nex + 1) + (i + 1)) * 4 + k + 1 for k in range(4)]
        code[ne, 12:16] = [((j + 1) * (Nex + 1) + i) * 4 + k + 1 for k in range(4)]



res = np.sort(code.flatten())[::-1]
size_res = len(res)

# Perform DOF reduction
for k in range(size_res-1, -1, -1):  # This simulates the reverse iteration in MATLAB
    for j in range(Nex * Ney):
        for i in range(16):
            if code[j, i] == res[k]:
                code[j, i] = 0
            elif code[j, i] > res[k]:
                code[j, i] -= 1

# Print the modified code table
print("Code Table after DOF Reduction:")
print(code)
