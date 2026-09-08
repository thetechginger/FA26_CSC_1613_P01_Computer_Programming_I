# Get the user's current age by using the current year and the user's birth year, and find the represented ASCII value of the user's age
# HINT: subtract the user's age from 128

currentYear = int(input("Enter the current year: "))
birthYear = int(input("Enter the birth year: "))

cAge = currentYear - birthYear

character = (chr(128 - cAge))

age = 128 - ord(character)

print(age)