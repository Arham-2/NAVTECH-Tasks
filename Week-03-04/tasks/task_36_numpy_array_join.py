import numpy as np

# Joining 1-D arrays with concatenate
first_array = np.array([1, 2, 3])
second_array = np.array([4, 5, 6])
joined_1d = np.concatenate((first_array, second_array))
print("Joined 1-D array:", joined_1d)

# Joining 2-D arrays along rows (axis=0) and columns (axis=1)
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])

concat_axis0 = np.concatenate((matrix_a, matrix_b), axis=0)
print("\nConcatenate axis 0 (rows):\n", concat_axis0)

concat_axis1 = np.concatenate((matrix_a, matrix_b), axis=1)
print("\nConcatenate axis 1 (columns):\n", concat_axis1)

# Joining arrays using stack, hstack, vstack
stacked = np.stack((first_array, second_array), axis=1)
print("\nStack along axis 1:\n", stacked)

h_stacked = np.hstack((first_array, second_array))
print("Horizontal stack (hstack):", h_stacked)

v_stacked = np.vstack((first_array, second_array))
print("Vertical stack (vstack):\n", v_stacked)
