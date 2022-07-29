from tkinter import *
import time
from quiz_brain import QuizBrain

FONT = ("Arial", 18, "italic")
THEME_COLOR = "#375362"
WHITE = "#f2fae0"

RIGHT_COLOR = "#cefa66"
WRONG_COLOR = "#ff896c"

class QuizInterface():

    def __init__(self, brain: QuizBrain):
        
        self.quiz = brain
        
        # ---------------------------- UI SETUP ------------------------------- #
        self.window = Tk()
        self.window.title("Quizzler")
        self.window["bg"] = THEME_COLOR
        self.window.config(padx=20,pady=20)

        # GRID ------------------------ 2 columns, 3 rows
        
        # Score Text
        self.score = Label(text="Score: 0", font=("Arial Black", 16, "bold"), bg=THEME_COLOR, fg=WHITE)
        self.score.grid(column=1,row=0,pady=20)
        
        # Canvas
        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.canvas.grid(column=0,row=1, columnspan=2,pady=20)

        # Timer Text
        self.question = self.canvas.create_text(150,125,text="The Question will be displayed here",fill=THEME_COLOR,font=FONT, width=250)

        # Buttons
        tick_img = PhotoImage(file="images/true.png")
        cross_img = PhotoImage(file="images/false.png")
        self.btn_true = Button(image=tick_img, highlightthickness=0, bd = 0, command=lambda: self.check_answer('True'))
        self.btn_false = Button(image=cross_img, highlightthickness=0, bd = 0, command=lambda: self.check_answer('False'))

        self.btn_true.grid(column=0,row=2,pady=20)
        self.btn_false.grid(column=1,row=2,pady=20)
                
        self.next_question()
        
        self.window.mainloop()
        
    def next_question(self):
        
        # Canvas color
        self.canvas.configure(bg=WHITE)
        
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)            
            # Update score
            self.score.config(text=f"Score: {self.quiz.score}")
        else:
            
            # Quiz Over
            self.canvas.itemconfig(self.question, text=f"Quiz Complete!\n\nYou scored {self.quiz.score}/{self.quiz.question_number}")  
            self.btn_true.config(state="disabled")
            self.btn_false.config(state="disabled")
            
        
    def check_answer(self, answer: str):
        is_right = self.quiz.check_answer(answer)            
        self.give_feedback(is_right) # Change colour of canvas 
            
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg=RIGHT_COLOR)
        else:
            self.canvas.config(bg=WRONG_COLOR)                        
        self.window.after(600, self.next_question)
        