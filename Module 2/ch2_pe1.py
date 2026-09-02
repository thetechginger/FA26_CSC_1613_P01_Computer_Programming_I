## Fahrenheit to Celsius Temperature Converter

F = float(input("°F = ")) # User defines degrees Fahrenheit via input
C = round((F - 32) * 5 / 9, 2) # Convert inputted degree Fahrenheit to Celsius & rounds to two decimal places
F = f"{F}°F" # Adds °F to end of F variable
C = f"{C}°C" # Adds °C to end of C variable
print(f"{F}"" =", C) # Outputs converted temperature in degrees Celsius