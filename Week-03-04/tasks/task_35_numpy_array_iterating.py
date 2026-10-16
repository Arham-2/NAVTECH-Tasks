import numpy as np

# Iterating 1-D array
arr_1d = np.array([1, 2, 3])
print("Iterating 1-D array:")
for element in arr_1d:
    print(element)

# Iterating 2-D array
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("\nIterating 2-D array elements:")
for row in arr_2d:
    for item in row:
        print(item, end=" ")
print()

# Iterating using nditer()
print("\nIterating with nditer():")
for element in np.nditer(arr_2d):
    print(element, end=" ")
print()

# Enumerated iteration using ndenumerate()
print("\nIterating with ndenumerate():")
for index, element in np.ndenumerate(arr_2d):
    print(index, element)
