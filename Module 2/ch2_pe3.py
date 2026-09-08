## Right-Triangle Calculator

from math import sqrt, pow # Imports needed math functions

print("Right-Triangle Calculator\nFormula: c=√(a²+b²)") # Gives user context

a = float(input("a = ")) # User gives side a value
b = float(input("b = ")) # User gives side b value
c = round(sqrt(pow(a,2) + pow(b,2)), 2) # Inputs given values into formula

print("c =", c) # Displays output to user