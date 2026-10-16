# Break in for loop
for value in range(1, 10):
    if value == 5:
        print("Breaking loop at", value)
        break
    print("Value:", value)

# Break in while loop
counter = 0
while counter < 10:
    if counter == 4:
        break
    print("x is", counter)
    counter += 1
