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

def calculate(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        return "ERROR"

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
        break
    elif repeat == 'y':
        num1 = answer
    else:
        num1 = float(input("What's the first number? "))