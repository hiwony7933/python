def coffee_machine():
    
    print()
    print("#1. Boil the water")
    print("#2. Prep for a cup")

    if coffee == 1:
        print("#3. Prep for Americano")
    elif coffee == 2:
        print("#3. Prep for Latte")
    elif coffee == 3:
        print("#3. Prep for Cappuccino")
    else:
        print("#3. Prepr anything")

    print("#4. Filling the water")
    print("#5. Stir with spoon or spooning")
    print()

while True:
    coffee = input("What kind of coffee would you like? (1: Americano, 2: Latte, 3: Cappuccino)")
    name = input("What is your name? ")
    menu = {"1": "Americano", "2": "Latte", "3": "Cappuccino"}
    coffee_machine()
    print("{0}, here is your {1}".format(name, menu[coffee])) 
    continue
