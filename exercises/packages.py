from prettytable import PrettyTable

def clear():
    from os import system, name  
    # for windows
    if name == 'nt':
        _ = system('cls')  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
        
clear()

# Set up table
table = PrettyTable()

# Add data column by column
table.add_column(
    "Pokemon Name",
    ["Pikachu", "Squirtle", "Charmander"]
)
table.add_column(
    "Type",
    ["Electric", "Water", "Fire"]
)

# Change table looks
table.align = "l"

print(table)
