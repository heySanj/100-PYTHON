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

# Create a window
window = Tk()
window.title("My First GUI Program")
window.minsize(width=500,height=300)
window["bg"] = "#202740"
window.config(padx=20,pady=20)

def button_clicked():
    label1["text"] = input.get()

# Label
label1 = Label(text="Hello World!", font=("Arial Black", 14, "bold"))
label1["fg"] = "#debc12"
label1["bg"] = "#202740"
label1.grid(column=0,row=0,padx=10,pady=5, sticky="W")

# Entry fields
input = Entry(width=30,font=("Arial Black", 10, "bold"))
#Add some text to begin with
input.insert(END, string="Some text to begin with.")
input.grid(column=3,row=2,padx=10,pady=5, sticky="W")

# button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1,row=1,padx=10,pady=5, sticky="W")

button2 = Button(text="Click Me", command=button_clicked)
button2.grid(column=2,row=0,padx=10,pady=5, sticky="W")


# built in Tkinter function that loops constantly, listening for user input
# Should be at the end of the program
window.mainloop()