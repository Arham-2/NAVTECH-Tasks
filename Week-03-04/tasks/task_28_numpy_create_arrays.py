import numpy as np

# 0-D array
array_0d = np.array(42)
print("0-D array:", array_0d)
print("Dimensions:", array_0d.ndim)

# 1-D array
array_1d = np.array([1, 2, 3, 4, 5])
print("\n1-D array:", array_1d)
print("Dimensions:", array_1d.ndim)

# 2-D array
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2-D array:\n", array_2d)
print("Dimensions:", array_2d.ndim)

# 3-D array
array_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print("\n3-D array:\n", array_3d)
print("Dimensions:", array_3d.ndim)

# Creating higher dimensional array using ndmin
array_5d = np.array([1, 2, 3, 4], ndmin=5)
print("\n5-D array:", array_5d)
print("Number of dimensions:", array_5d.ndim)
