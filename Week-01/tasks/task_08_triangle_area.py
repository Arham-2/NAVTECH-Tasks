# Python Program to find the area of triangle

side_a = 5
side_b = 6
side_c = 7

# Uncomment below to take inputs from the user
# side_a = float(input('Enter first side: '))
# side_b = float(input('Enter second side: '))
# side_c = float(input('Enter third side: '))

# calculate the semi-perimeter
semi_perimeter = (side_a + side_b + side_c) / 2

# calculate the area
area = (semi_perimeter * (semi_perimeter - side_a) * (semi_perimeter - side_b) * (semi_perimeter - side_c)) ** 0.5
print('The area of the triangle is %0.2f' % area)
