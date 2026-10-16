# Creating a tuple
fruit_tuple = ("apple", "banana", "cherry", "apple")
print("Tuple:", fruit_tuple)

# Accessing elements
print("First item:", fruit_tuple[0])
print("Last item:", fruit_tuple[-1])
print("Slice [1:3]:", fruit_tuple[1:3])

# Tuple methods
print("Count of 'apple':", fruit_tuple.count("apple"))
print("Index of 'banana':", fruit_tuple.index("banana"))

# Tuple unpacking
first, second, third, fourth = fruit_tuple
print("Unpacked values:", first, second, third, fourth)
