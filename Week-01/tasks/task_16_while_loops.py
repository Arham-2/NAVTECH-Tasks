# Counter while loop
count = 0
while count < 5:
    print("Count:", count)
    count += 1

# Factorial using while loop
number = 5
factorial = 1
remaining = number
while remaining > 1:
    factorial *= remaining
    remaining -= 1
print("Factorial of", number, "is", factorial)

# While else
step = 0
while step < 3:
    print("Step:", step)
    step += 1
else:
    print("Loop finished normally")
