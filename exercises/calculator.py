import os
clear = lambda: os.system('clear')
clear()

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def divide(num1, num2):
    return num1 / num2

def multiply(num1, num2):
    return num1 * num2

operations = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply
}

def calculate(num1=int, num2=int, operation=str):
    """Take two numbers, and perform the operation on them, like a calculator"""
    # if operation == "+":
    #     return num1 + num2
    # elif operation == "-":
    #     return num1 - num2
    # elif operation == "*":
    #     return num1 * num2
    # elif operation == "/":
    #     return num1 / num2
    # else:
    #     return "ERROR"
    return operations[operation](num1, num2)



def calc_app():
    clear()
    print(logo)
    num1 = float(input("\nWhat's the first number? "))
    print("\n+\n-\n*\n/")

    while True:        
        operation = input("\nPick an operation: ")
        num2 = float(input("\nWhats the next number? "))
        answer = calculate(num1, num2, operation)
        if answer == "ERROR":
            print("\nSorry! That could not be calculated.")
        else:
            print(f"{num1} {operation} {num2} = {answer}\n")
            
        repeat = input(f"Type 'y' to continue calculating with {answer}, type 'n' to start a new calculation, or 'x' to exit: ")

        if repeat == 'x':
            print("\nGoodbye!\n\n")
            exit()
        elif repeat == 'y':
            num1 = answer
        else:
            calc_app()


calc_app()