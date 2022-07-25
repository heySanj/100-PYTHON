from typing import final


def clear():
    from os import system, name

    # for windows
    if name == "nt":
        _ = system("cls")
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")
clear()

# try:
#     file = open("a_file.txt")
#     a_dict = {"abc": "def"}
#     no_val = a_dict['abc']
# except FileNotFoundError:
#     print("Could not find the file, so it will be created")
#     file = open("a_file.txt", "w")
#     file.write("something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.")
# # Else will be executed when no errors are found
# else:
#     print("Found file!")
#     content = file.read()
#     print(content)
# finally:
#     print("Done")
#     file.close()


height = float(input("Height: "))
weight = int(input("Weight: "))

if height < 0 or height > 3:
    raise ValueError("Please enter a valid height.")

bmi = weight / height ** 2
print(bmi)