import h5py
import numpy as np
from input import file_name
import scipy

with h5py.File('(testfile_Saved at 2024-11-14 22:22:46.413953).h5', 'r') as hdf:
    # Access datasets
    K = hdf['Matrices/Stiffness_Matrix'][:]
    F = hdf['Matrices/Force_Matrix'][:]
    Delta = hdf['Nodal_Data/Nodal_Displacement'][:]
    
    # Print to confirm
    #print("Stiffness Matrix:\n", K)
    #print("Force Matrix:\n", F)
    #print("Nodal Displacement:\n", Delta)


