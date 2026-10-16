import numpy as np

# Copy example
original_for_copy = np.array([1, 2, 3, 4, 5])
array_copy = original_for_copy.copy()
original_for_copy[0] = 42

print("Original array after change:", original_for_copy)
print("Copy array (not changed):   ", array_copy)

# View example
original_for_view = np.array([1, 2, 3, 4, 5])
array_view = original_for_view.view()
original_for_view[0] = 99

print("\nOriginal array after change:", original_for_view)
print("View array (also changed):  ", array_view)

# Check if array owns its data with .base
print("\nCopy base attribute (owns data):", array_copy.base)
print("View base attribute (shares data):", array_view.base)
