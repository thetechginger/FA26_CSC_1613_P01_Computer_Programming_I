import math # syntax

concreteCost = 8.75 # semantic

name = str(input("Enter your name: ")) # syntax
area = float(input("Enter the square footage: ")) # syntax
side_length = math.sqrt(area)

cost = concreteCost * area
tax = cost * 0.07
total_cost = cost - tax
3
print("\nCustomer: " + name)
print("Area:", area,  " square feet")
print("Side Length: ", round(side_length, 2), " feet") # syntax
print("Concrete Cost: ",  f"${round(cost, 2)}") # syntax
print("Tax: ", f"${round(tax, 2)}") # syntax
print("Total Cost: ", f"${round(total_cost, 2)}") # syntax