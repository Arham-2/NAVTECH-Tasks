# Looping using enumerate
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)

# Looping using zip
names = ["Ali", "Sara", "Zain"]
marks = [85, 90, 78]
for name, score in zip(names, marks):
    print(name, "scored", score)

# Looping in sorted order
numbers = [40, 10, 30, 20]
for number in sorted(numbers):
    print("Sorted:", number)

# Looping in reverse order
for number in reversed(numbers):
    print("Reversed:", number)
