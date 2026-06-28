# Calculate area of a regular polygon

import math

number_of_sides = int(input("Number of sides: "))
side_length = float(input("Length of side: "))

area = (number_of_sides * side_length ** 2) / (4 * math.tan(math.pi / number_of_sides))

print("Area of polygon:", area)