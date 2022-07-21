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
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TIMER_FONT = (FONT_NAME, 35, "bold")
BTN_FONT = (FONT_NAME, 14, "bold")
CHECK = "✔"
global timer
timer = None

global counting
counting = False

global reps
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    if timer != None:
        window.after_cancel(timer)
    global counting
    global reps
    counting = False
    reps = 0
    marks["text"] = ""
    title["text"] = f"Timer"
    title["fg"] = GREEN
    canvas.itemconfig(timer_txt, text="00:00")
    

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start():
   
    global counting
    global reps
        
    if not counting:
        counting = True
                
        reps += 1
        
        if reps > 8:
            window.after_cancel(timer)
            reset_timer()
            
        # Big Break                
        elif reps % 8 == 0:
            countdown(LONG_BREAK_MIN * 60)
            marks["text"] += CHECK
            title["text"] = f"Big Break!"
            title["fg"] = RED
        
        # Short Break
        elif reps % 2 == 0:
            countdown(SHORT_BREAK_MIN * 60)
            marks["text"] += CHECK
            title["text"] = f"Break"
            title["fg"] = PINK
        
        # Work
        else:
            countdown(WORK_MIN * 60)
            title["text"] = f"Working"
            title["fg"] = GREEN

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global counting
    global timer
    # Repeat this method every second until count = 0

    if count >= 0 and counting:        
        timer = window.after(1000, countdown, count - 1)
        
        # Format text
        canvas.itemconfig(timer_txt, text=f"{math.floor(count / 60):02d}:{(count % 60):02d}")
    else:
        counting = False
        start()
        count = 0
# ---------------------------- UI SETUP ------------------------------- #

# Create a window
window = Tk()
window.title("Pomodoro")
window["bg"] = YELLOW
window.config(padx=20,pady=20)

# Canvas
canvas = Canvas(width=210, height=230, bg=YELLOW, highlightthickness=0)

# Tomato
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(105, 115, image=tomato_img)

# Timer Text
timer_txt = canvas.create_text(105,140,text="00:00",fill=YELLOW,font=TIMER_FONT)
# canvas.place(relx=0.5, rely=0.5, anchor=CENTER)
canvas.grid(row=1, column=1, pady=10)

# Title Label
title = Label(text="Timer", font=TIMER_FONT, fg=GREEN, bg=YELLOW)
title.grid(row=0, column=1, pady=10, sticky="ew")

# Completed Labels
marks = Label(text="", font=(FONT_NAME, 22, "bold"), fg=GREEN, bg=YELLOW)
marks.grid(row=3, column=1, pady=10, sticky="ew")

# Start and Reset Butons
start_btn = Button(text="Start", width=8, font=BTN_FONT, command=start)
start_btn.grid(row=2, column=0, pady=10, sticky="e")

reset_btn = Button(text="Reset", width=8, font=BTN_FONT, command=reset_timer)
reset_btn.grid(row=2, column=3, pady=10, sticky="w")



window.mainloop()