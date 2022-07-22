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
import pandas as pd
import os
from random import choice, randint, shuffle
import pyperclip

BG_COLOUR = "#f8f8ec"
RED = "#cf4742"
FONT = ("Arial", 11, "bold")

DEFAULT_USER = "hello@sanjeevprasad.com"


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
    
    website = input_website.get()
    user = input_user.get()
    password = input_pass.get()
    
    if len(website) is 0 or len(user) is 0 or len(password) is 0:
        messagebox.showerror("Error", "Some fields have no data!")
    else:    
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nUser: {user} "
                                                            f"\nPassword: {password} \nIs it okay to save?")
        
        if is_ok:
            # Get the strings from input fields and save to data frame
            add_data = pd.DataFrame({
                'WEBSITE': [website],
                'USER': [user],
                'PASS': [password]
            })
            
            # if file does not exist write header 
            if not os.path.isfile('pw.csv'):
                add_data.to_csv('pw.csv', index=False, header=['WEBSITE', 'USER', 'PASS'])
            else: # else it exists so append without writing the header
                add_data.to_csv('pw.csv', mode='a', index=False, header=False)
                
            # Clear fields
            clear_entry()
            
        else:
            pass

        


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
input_website = Entry(width=44,font=FONT, justify='left')
input_user = Entry(width=44,font=FONT, justify='left')
input_pass = Entry(width=24,font=FONT, justify='left')

input_website.grid(column=1,row=1,columnspan=2, sticky='W')
input_website.focus() # Focus the cursor on this entry field
input_user.grid(column=1,row=2,columnspan=2, sticky='W')
input_user.insert(0, DEFAULT_USER) # Insert existing text
input_pass.grid(column=1,row=3, sticky='W')

# Buttons
btn_generate = Button(text="Generate Password", width=16, font=FONT, command=generate_pw)
btn_add = Button(text="Add", width=39, font=FONT, command=save_pw)

btn_generate.grid(column=2,row=3, sticky='W')
btn_add.grid(column=1,row=4,columnspan=2, sticky='W')

window.mainloop()