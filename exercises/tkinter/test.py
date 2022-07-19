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
window.minsize(width=500,height=600)
window["bg"] = "#202740"

# Function with unlimited arguments allowed
def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

# Functions with unlimited keyword arguments
def calculate(n, **kwargs):
    # for key,value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n

def button_clicked():
    label1["text"] = input.get()

# Label
label1 = Label(text=calculate(2, add=3, multiply=5), font=("Arial Black", 18, "bold"))
label1["fg"] = "#debc12"
label1["bg"] = "#202740"

# button
button = Button(text="Click Me", command=button_clicked)

# Entry fields
input = Entry(width=40)
#Add some text to begin with
input.insert(END, string="Some text to begin with.")

#Text
text = Text(height=5, width=30)
#Puts cursor in textbox.
text.focus()
#Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
#Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))

#Spinbox
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)


#Scale
#Called with current scale value.
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)


#Checkbutton
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()


#Radiobutton
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)



#Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)



# Use .pack() to place components on the window
label1.pack(pady=5)
input.pack(pady=5)
button.pack(pady=5)
text.pack(pady=5)
spinbox.pack(pady=5)
scale.pack(pady=5)
checkbutton.pack(pady=5)
radiobutton1.pack(pady=5)
radiobutton2.pack(pady=5)
listbox.pack(pady=5)

# built in Tkinter function that loops constantly, listening for user input
# Should be at the end of the program
window.mainloop()