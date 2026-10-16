# Continue in for loop to print only odd numbers
for number in range(1, 10):
    if number % 2 == 0:
        continue
    print("Odd number:", number)

# Continue with strings
word = "Python"
for letter in word:
    if letter == "o":
        continue
    print("Letter:", letter)
