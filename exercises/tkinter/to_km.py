def clear():
    from os import system, name

    # for windows
    if name == "nt":
        _ = system("cls")
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")
clear()

FONT = ("Arial", 12, "bold")
BG_COLOUR = "#202740"
TEXT_COLOUR = "#8b99c9"
HIGHLIGHT_COLOUR = "#debc12"


from tkinter import *


# Create a window
window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=200,height=100)
window["bg"] = BG_COLOUR
window.config(padx=20,pady=20)

def convert():
    km = float(input.get()) * 1.609
    label_result["text"] = "{:.2f}".format(km)

# MILES label
label_m = Label(text="Miles", font=FONT)
label_m["fg"] = TEXT_COLOUR
label_m["bg"] = BG_COLOUR
label_m.grid(row=1, column=2, pady=5)

# IS EQUAL TO
label_equal = Label(text="is equal to ", font=FONT)
label_equal["fg"] = TEXT_COLOUR
label_equal["bg"] = BG_COLOUR
label_equal.grid(row=2, column=0, pady=5)

# ANSWER LABEL
label_result = Label(text="0", font=FONT, justify='center')
label_result["fg"] = HIGHLIGHT_COLOUR
label_result["bg"] = BG_COLOUR
label_result.grid(row=2, column=1, pady=5)

# KM
label_km = Label(text="Km", font=FONT)
label_km["fg"] = HIGHLIGHT_COLOUR
label_km["bg"] = BG_COLOUR
label_km.grid(row=2, column=2, pady=5)

# INPUT FIELD
input = Entry(width=10,font=FONT, justify='center')
#Add some text to begin with
input.insert(END, string="0")
input.grid(row=1, column=1, pady=5)

# button
button = Button(text="Calculate", command=convert)
button.grid(row=4, column=1, pady=5)


# built in Tkinter function that loops constantly, listening for user input
# Should be at the end of the program
window.mainloop()