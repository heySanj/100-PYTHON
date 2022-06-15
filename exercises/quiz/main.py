def clear():
    from os import system, name  
    # for windows
    if name == 'nt':
        _ = system('cls')  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
clear()

import random

from quiz_brain import QuizBrain
from question_model import Question
from data import open_tdb_quiz

# import the questions and put them into a list
questions = []

for question in open_tdb_quiz:
    questions.append(Question(question['question'], question['correct_answer'].title()))

random.shuffle(questions)    
quiz = QuizBrain(questions)

# Run the quiz while there are still questions remaining
while quiz.questions_remaining():
    quiz.next_question()
    
print("You've completed the quiz!")
print(f"You're final score was: {quiz.score}/{quiz.question_number}\n\n")