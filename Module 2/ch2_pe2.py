## Gross Pay Calculator

employeeName = str(input("Enter your name: \n")) # Requests user to input their name
hours = float(input("How many hours did you work? \n")) # Requests user to input how many hours they worked
hourlyRate = float(input("Hourly rate: \n")) # Requests user to input their hourly rate

grossPay = round(hours * hourlyRate, 2) # Calculates the gross pay and rounds to the second decimal

print(f"\n\nEmployee Name: {employeeName}"
f"\nHours Worked: {hours}"
f"\nHourly Rate: ${hourlyRate}"
f"\nGross Pay: ${grossPay}") # Displays the users name, hours, rate, and final gross pay on 4 seperate lines