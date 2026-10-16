# Handling ZeroDivisionError
try:
    dividend = 10
    divisor = 0
    result = dividend / divisor
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

# Handling ValueError
try:
    parsed_number = int("abc")
except ValueError:
    print("Error: Invalid number format!")

# Try, Except, Else, Finally
try:
    quotient = 10 / 2
except ZeroDivisionError:
    print("Division error")
else:
    print("Division successful, result is:", quotient)
finally:
    print("This block always executes.")
