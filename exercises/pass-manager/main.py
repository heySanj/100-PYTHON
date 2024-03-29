def clear():
    from os import system, name

    # for windows
    if name == "nt":
        _ = system("cls")
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")
clear()

from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

BG_COLOUR = "#f8f8ec"
RED = "#cf4742"
FONT = ("Arial", 11, "bold")

DEFAULT_USER = "user@testmail.com"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_pw():
    chars = []
    chars += [choice(letters) for _ in range(randint(8,10))]
    chars += [choice(symbols) for _ in range(randint(2,4))]
    chars += [choice(numbers) for _ in range(randint(2,4))]

    shuffle(chars)
    
    password = ''.join(chars)
        
    # Put the password in the password field after clearing it
    input_pass.delete(0, END)
    input_pass.insert(0, password)
    pyperclip.copy(password) # Copy the password to clipboard

# ---------------------------- SAVE PASSWORD ------------------------------- #

def clear_entry():
    input_website.delete(0, END)
    input_pass.delete(0, END)
    

def save_pw():
    
    website = input_website.get().title()
    user = input_user.get()
    password = input_pass.get()
    
    # Save in dictionary for JSON format
    new_data = {
        website: {
            'user': user,
            'password': password
        }
    }
    
    if len(website) is 0 or len(user) is 0 or len(password) is 0:
        messagebox.showerror("Error", "Some fields have no data!")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file) # Read the old data
            
        except FileNotFoundError:        
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4) # Write new data to data_file
                
        else:            
            data.update(new_data) # update old data with new data                        
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4) # Write updated data to data_file
                
        finally:
            # Clear fields
            clear_entry() 
      
# ---------------------------- SEARCH WEBSITE ------------------------------- #

def find_password():
    website = input_website.get().title()
    
    try:
        with open("data.json", "r") as data_file:
                data = json.load(data_file) # Read the old data
            
    except FileNotFoundError:        
        messagebox.showerror("Error", "Sorry, no data file could be found.")
            
    else:
        # Use if/else statements for error handling if possible. 
        # Use Try/except in exceptional cases where needed
        if website in data:
            user = data[website]['user']
            password = data[website]['password']
            messagebox.showinfo(f"{website} details", f"User: {user}\nPass: {password}")
        else:
            messagebox.showerror("Error", f"Sorry, no details for {website} exist.")
                    
        # try:
        #     user = data[website]['user']
        #     password = data[website]['password']
        #     messagebox.showinfo(f"{website} details", f"User: {user}\nPass: {password}")
        # except KeyError as errormessage:
        #     messagebox.showerror("Error", f"Sorry, no details for {errormessage} exist.")
            
    finally:
        # Clear fields
        clear_entry() 
    
    
    
# ---------------------------- UI SETUP ------------------------------- #

# Create a window
window = Tk()
window.title("My Pass: Password Manager")
window["bg"] = BG_COLOUR
window.config(padx=30,pady=30)

# GRID ------------------------ 3 columns, 5 rows

# Canvas
canvas = Canvas(width=200, height=200, bg=BG_COLOUR, highlightthickness=0)
canvas.grid(column=1,row=0)

# Logo
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)

# Labels
label_website = Label(text="Website: ", font=FONT, fg=RED, bg=BG_COLOUR)
label_user = Label(text="Email/Username: ", font=FONT, fg=RED, bg=BG_COLOUR)
label_pass = Label(text="Password: ", font=FONT, fg=RED, bg=BG_COLOUR)

label_website.grid(column=0,row=1, sticky='E')
label_user.grid(column=0,row=2, sticky='E')
label_pass.grid(column=0,row=3, sticky='E')

# Input Fields
input_website = Entry(width=24,font=FONT, justify='left')
input_user = Entry(width=44,font=FONT, justify='left')
input_pass = Entry(width=24,font=FONT, justify='left')

input_website.grid(column=1,row=1,columnspan=2, sticky='W')
input_website.focus() # Focus the cursor on this entry field
input_user.grid(column=1,row=2,columnspan=2, sticky='W')
input_user.insert(0, DEFAULT_USER) # Insert existing text
input_pass.grid(column=1,row=3, sticky='W')

# Buttons
btn_search = Button(text="Search", width=16, font=FONT, command=find_password)
btn_generate = Button(text="Generate Password", width=16, font=FONT, command=generate_pw)
btn_add = Button(text="Add", width=39, font=FONT, command=save_pw)

btn_search.grid(column=2,row=1, sticky='W')
btn_generate.grid(column=2,row=3, sticky='W')
btn_add.grid(column=1,row=4,columnspan=2, sticky='W')

window.mainloop()