# Solve the quadratic equation ax**2 + bx + c = 0

# import complex math module
import cmath

coeff_a = 1
coeff_b = 5
coeff_c = 6

# calculate the discriminant
discriminant = (coeff_b ** 2) - (4 * coeff_a * coeff_c)

# find two solutions
root_1 = (-coeff_b - cmath.sqrt(discriminant)) / (2 * coeff_a)
root_2 = (-coeff_b + cmath.sqrt(discriminant)) / (2 * coeff_a)

print('The solution are {0} and {1}'.format(root_1, root_2))
