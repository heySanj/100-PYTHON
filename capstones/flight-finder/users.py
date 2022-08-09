def clear():
    from os import system, name

    # for windows
    if name == "nt":
        _ = system("cls")
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")
clear()

from data_manager import DataManager

sheet = DataManager() # Establish a connection to the Google sheets

def ask_user():
    first_name = input(f"\nWhat is your first name?\n")
    last_name = input(f"\nWhat is your last name?\n")
    email1 = input(f"\nWhat is your email?\n")
    email2 = input(f"\nPlease type your email again.\n")

    if email1 == email2:
        # Success
        print("\n\nYou're in the club!")
        add_user(first_name, last_name, email1)
    else:
        print("\n\nSorry the emails did not match, please try again")
        
def add_user(first, last, email):
    data = {
        "firstName": first,
        "lastName": last,
        "email": email
    }
    
    sheet.post_data("users", data)

# ---------------------------- MAIN PROGRAM ------------------------------- #

print(f"Welcome to the Flight Club\n---------------------------------\nWe find the best flight deals and email you!\n")

ask_user()