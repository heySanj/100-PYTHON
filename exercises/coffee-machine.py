import os
clear = lambda: os.system('clear')
clear()

divider = "------------------------------------------------------\n"

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")    
    print(f"Money: ${resources['money']}")
    
def check_resources(ingredients):
    for ingredient in ingredients:
        if resources[ingredient] < ingredients[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True
    
def enter_coins():
    print("Please insert coins: ")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    cash = (.25 * quarters) + (.10 * dimes) + (.05 * nickles) + (.01 * pennies)
    return cash

def process_payment(paid, drink):
    drink_cost = drink['cost']
    resources['money'] += drink_cost
    change = round((paid - drink_cost), 2)
    return change
    
def make_drink(ingredients):
    # deduct resources
    for ingredient in ingredients:
        resources[ingredient] -= ingredients[ingredient]
    
while True:   
    
    choice = input("\n\nWhat would you like? (espresso/latte/cappuccino): ")
    print(divider)
    
    if choice == "report":
        print_report()
    elif choice == "off":
        print("Thank you for using this coffee machine!\n\n")
        quit()
    elif choice in MENU:
        chosen_drink = MENU[choice]

        # Check if there are enough resources to make the drink
        if check_resources(chosen_drink['ingredients']):
            # If so, allow the user to insert coins
            cash = enter_coins()
            if cash >= chosen_drink['cost']:
                print(divider)
                print(f"Here is ${process_payment(cash, chosen_drink)} in change.")
                make_drink(chosen_drink['ingredients'])
                print(f"Here is your {choice} ☕. Enjoy!")
                print(divider)
            else:
                # not enough coins
                print("Sorry that's not enough money. Money refunded.")
        else:
            continue
    else:
        print("Sorry that command is not recognized..")
