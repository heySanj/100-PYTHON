def clear():
    from os import system, name

    # for windows
    if name == "nt":
        _ = system("cls")
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")
clear()

BG_COLOUR = "#f8f8ec"
RED = "#cf4742"
FONT = ("Arial", 11, "bold")

from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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
input_user.grid(column=1,row=2,columnspan=2, sticky='W')
input_pass.grid(column=1,row=3, sticky='W')

# Buttons
btn_generate = Button(text="Generate Password", width=16, font=FONT)
btn_add = Button(text="Add", width=39, font=FONT)

btn_generate.grid(column=2,row=3, sticky='W')
btn_add.grid(column=1,row=4,columnspan=2, sticky='W')

window.mainloop()