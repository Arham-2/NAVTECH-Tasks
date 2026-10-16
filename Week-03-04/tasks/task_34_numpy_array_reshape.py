import numpy as np

# Reshape from 1-D to 2-D (4 rows, 3 columns)
numbers = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
reshaped_2d = numbers.reshape(4, 3)
print("Reshaped to 2-D:\n", reshaped_2d)

# Reshape from 1-D to 3-D (2 arrays, each 3x2)
reshaped_3d = numbers.reshape(2, 3, 2)
print("\nReshaped to 3-D:\n", reshaped_3d)

# Unknown dimension using -1 (NumPy calculates remaining dimension)
reshaped_inferred = numbers.reshape(2, 2, -1)
print("\nReshaped with -1:\n", reshaped_inferred)

# Flattening the array back to 1-D
flattened = reshaped_2d.reshape(-1)
print("\nFlattened array:", flattened)
