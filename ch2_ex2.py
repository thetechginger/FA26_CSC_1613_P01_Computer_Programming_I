"""
USING THE MATH MODULE

Use the math module to find the following of a circle:
    -diameter
    -circumference
    -area
Remember to import the math module
"""
from math import pi, pow

radius = int(input("Enter the radius: "))

diameter = round(radius * 2)
circumference = round(2 * pi * radius)
area = round(pi * pow(radius, 2))

print("The diameter is:", diameter, "\nThe circumference is:", circumference, "\nThe area is:", area)