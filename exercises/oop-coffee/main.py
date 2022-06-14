def clear():
    from os import system, name  
    # for windows
    if name == 'nt':
        _ = system('cls')  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

clear()

divider = "------------------------------------------------------\n"
logo = """
 .d88b.   .d88b.  d8888b.                        
.8P  Y8. .8P  Y8. 88  `8D                        
88    88 88    88 88oodD'                        
88    88 88    88 88~~~                          
`8b  d8' `8b  d8' 88                             
 `Y88P'   `Y88P'  88                             
                                                 
                                                 
 .o88b.  .d88b.  d88888b d88888b d88888b d88888b 
d8P  Y8 .8P  Y8. 88'     88'     88'     88'     
8P      88    88 88ooo   88ooo   88ooooo 88ooooo 
8b      88    88 88~~~   88~~~   88~~~~~ 88~~~~~ 
Y8b  d8 `8b  d8' 88      88      88.     88.     
 `Y88P'  `Y88P'  YP      YP      Y88888P Y88888P"""

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

maker = CoffeeMaker()
mm = MoneyMachine()
menu = Menu()

is_on = True
print(logo)

while is_on:
    
    choice = input(f"\n\nWhat would you like? ({menu.get_items()}): ")
    print(divider)
    
    if choice == "off":
        is_on = False
    elif choice == "report":
        maker.report()
        mm.report()
        print(divider)
    else:
        drink = menu.find_drink(choice)
        if drink != None:            
            if maker.is_resource_sufficient(drink):
                if mm.make_payment(drink.cost):
                    maker.make_coffee(drink)
                    print(divider)        
        
       
print("Thank you for using this coffee machine!\n\n")
quit()