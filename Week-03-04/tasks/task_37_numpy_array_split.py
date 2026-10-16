import numpy as np

# Splitting 1-D array into 3 parts
numbers = np.array([1, 2, 3, 4, 5, 6])
split_parts = np.array_split(numbers, 3)
print("Split 1-D array into 3:")
for part in split_parts:
    print(part)

# Accessing individual split parts
print("\nFirst part:", split_parts[0])
print("Second part:", split_parts[1])
print("Third part:", split_parts[2])

# Splitting 2-D array
matrix = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
split_parts_2d = np.array_split(matrix, 3)
print("\nSplit 2-D array:")
for part in split_parts_2d:
    print(part)

# Horizontal split using hsplit
h_split = np.hsplit(np.array([[1, 2, 3, 4], [5, 6, 7, 8]]), 2)
print("\nHorizontal split:\n", h_split)
