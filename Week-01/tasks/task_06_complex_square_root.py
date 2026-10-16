# Find square root of real or complex numbers
# Importing the complex math module
import cmath

number = 1 + 2j

# To take input from the user
# number = eval(input('Enter a number: '))

square_root = cmath.sqrt(number)
print('The square root of {0} is {1:0.3f}+{2:0.3f}j'.format(number, square_root.real, square_root.imag))
