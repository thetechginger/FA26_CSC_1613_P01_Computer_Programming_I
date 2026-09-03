"""
The Daily Grind customer request
data:
Drinks
    Small coffee: $2.50
    Large coffee: $3.75
    Iced coffee: $4.25
    Latte: $4.50
    Cappuccino: $4.75
Food
    Muffin: $3.25
    Bagel: $2.75
    Breakfast sandwich: $6.50
    Pastry: $3.50
Sales Tax: 8%
BONUS REQUEST  +10 POINTS
I love multiples of 7, so if the amount of items a customer purchases is divisible by 7, we offer a 70% discount to the sale cost (pre-tax).

Outline:
print "Welcome to The Daily Grind!"
name = str input "Enter your name: "
small coffee = int input "how many small coffees would you like?\n"
large coffee = int input "how many large coffees would you like?\n"
iced coffee = int input "how many iced coffees would you like?\n"
latte = int input "how many lattes would you like?\n"
cappuccino = int input "how many cappuccinos would you like?\n"
muffin = int input "how many muffins would you like?\n"
bagel = int input "how many bagels would you like?\n"
breakfast sandwich = int input "how many breakfast sandwiches would you like?\n"
pastry = int input "how many pastries would you like?\n"
if (small coffee + large coffee + iced coffee + latte + cappuccino + muffin + bagel + breakfast sandwich + pastry) % 7 = 0;
    print **************************************

          *You've earned our 70% OFF MEGA SALE!*

          **************************************
sCoffeeCost = small coffee * 2.5
lCoffeeCost = large coffee * 3.75
iCoffeeCost = iced coffee * 4.25
latteCost = latte * 4.5
cappuccinoCost = cappuccino * 4.75
muffinCost = muffin * 3.25
bagelCost = bagel * 2.75
bSandwichCost = breakfast sandwich * 6.5
pastryCost = pastry * 3.5
drinks = sCoffeeCost + lCoffeeCost + iCoffeeCost + latteCost + cappuccinoCost
food = muffinCost + bagelCost + bSandwichCost + pastryCost
subtotal = drinks + food
tax = (subtotal * 0.08) - subtotal
total = subtotal + tax
print f"***** The Daily Grind *****
Customer: {name}
Drinks: ${drinks}
Food: ${food}
Sales Tax: ${tax}
****************************

Total: ${total}
Thank you for visiting The Daily Grind!"
"""

print("Welcome to The Daily Grind!")
name = str(input("Enter your name: "))
sCoffee = int(input("How many small coffees would you like?\n"))
lCoffee = int(input("How many large coffees would you like?\n"))
iCoffee = int(input("How many iced coffees would you like?\n"))
latte = int(input("How many lattes would you like?\n"))
cappuccino = int(input("How many cappuccinos would you like?\n"))
muffin = int(input("How many muffins would you like?\n"))
bagel = int(input("How many bagels would you like?\n"))
bSandwich = int(input("How many breakfast sandwiches would you like?\n"))
pastry = int(input("How many pastries would you like?\n"))

sCoffeeCost = sCoffee * 2.5
lCoffeeCost = lCoffee * 3.75
iCoffeeCost = iCoffee * 4.25
latteCost = latte * 4.5
cappuccinoCost = cappuccino * 4.75
muffinCost = muffin * 3.25
bagelCost = bagel * 2.75
bSandwichCost = bSandwich * 6.5
pastryCost = pastry * 3.5

drinks = sCoffeeCost + lCoffeeCost + iCoffeeCost + latteCost + cappuccinoCost
food = muffinCost + bagelCost + bSandwichCost + pastryCost
subtotal = drinks + food
tax = (subtotal * 0.08)
total = round(subtotal + tax, 2) # added round function

if (sCoffee + lCoffee + iCoffee + latte + cappuccino + muffin + bagel + bSandwich + pastry) % 7 == 0:
    total = round(total * 0.3, 2) # added this in order to give the discount
    print("""\n**************************************

*You've earned our 70% OFF MEGA SALE!*

**************************************\n""")

print(f"""***** The Daily Grind *****
Customer: {name}
Drinks: ${drinks}
Food: ${food}
Sales Tax: ${tax}
****************************
Total: ${total}
Thank you for visiting The Daily Grind!""")