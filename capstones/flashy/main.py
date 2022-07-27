def clear():
    from os import system, name

    # for windows
    if name == "nt":
        _ = system("cls")
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")
clear()

from textwrap import fill
from tkinter import *
from random import choice
import pandas as pd

BG_COLOUR = "#B1DDC6"
RED = "#cf4742"
FONT = ("Arial", 11, "bold")

HEADER_FONT = ("Arial", 35, 'italic')
WORD_FONT = ("Arial", 60, 'bold')

global timer, current_word
timer = None
current_word = {}

# ---------------------------- GET WORDS  ------------------------------- #

try:
    data = pd.read_csv("./data/words_to_learn.csv")    
except FileNotFoundError:        
    data = pd.read_csv("./data/french_words.csv")              
finally:
    words_dict = data.to_dict(orient="records")
    # print(type(words_dict))


# ---------------------------- CARD FUNCTIONALITY  ------------------------------- #

def change_word():
    # check if there is a timer currently running
    if timer != None:
        pass
    else:    
        global current_word
        current_word = choice(words_dict)
        # print(f"The current word is: {current_word}")
        canvas.itemconfig(card_img, image=card_front)
        canvas.itemconfig(header, fill="black", text='French')
        canvas.itemconfig(word, fill="black", text=current_word['French'])

        # Start the countdown
        countdown(3)
    
def flip():
    global timer
    canvas.itemconfig(card_img, image=card_back)
    canvas.itemconfig(header, fill="white", text='English')
    canvas.itemconfig(word, fill="white", text=current_word['English'])
    
    # Cancel Timer
    window.after_cancel(timer)
    timer = None

def correct():
    # check if there is a timer currently running
    if timer != None:
        pass
    else:   
        global current_word
        # print(f"Removing: {current_word}")
        words_dict.remove(current_word)

        # Create updated .csv
        df = pd.DataFrame.from_records(words_dict)
        df.to_csv("./data/words_to_learn.csv", index=False)

        # change card
        change_word()

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global timer
    # Repeat this method every second until count = 0
    if count >= 0:        
        timer = window.after(1000, countdown, count - 1)        
    else:
        flip()




# ---------------------------- UI SETUP ------------------------------- #

# Create a window
window = Tk()
window.title("Flashy: The Flash Card Study App")
window["bg"] = BG_COLOUR
window.config(padx=50,pady=50)

# GRID ------------------------ 2 columns, 2 rows

# Canvas
canvas = Canvas(width=800, height=526, bg=BG_COLOUR, highlightthickness=0)
canvas.grid(column=0,row=0, columnspan=2)

# Card
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_img = canvas.create_image(400, 263, image=card_front)
# Timer Text
header = canvas.create_text(400,150,text="Header",fill='black',font=HEADER_FONT)
word = canvas.create_text(400,275,text="Word",fill='black',font=WORD_FONT)

# Buttons
tick_img = PhotoImage(file="images/right.png")
cross_img = PhotoImage(file="images/wrong.png")
btn_correct = Button(image=tick_img, highlightthickness=0, bd = 0, command=correct)
btn_wrong = Button(image=cross_img, highlightthickness=0, bd = 0, command=change_word)

btn_correct.grid(column=1,row=1)
btn_wrong.grid(column=0,row=1)

# change card
change_word()

window.mainloop()