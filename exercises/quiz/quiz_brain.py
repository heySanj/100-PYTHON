class QuizBrain:
    
    
    def __init__(self, q_list):
        # Initialise attributes
        self.question_number = 0
        self.question_list = q_list
        self.score = 0   
    
    # Check to see if the user is correct and increase their score    
    def is_correct(self, question, answer):
        if answer == question.answer:
            print("You got it right!")
            self.score += 1
        else:
            print("Sorry that was incorrect...")
        
        print(f"The correct answer was: {question.answer}")
        print(f"Your current score is: {self.score}/{self.question_number}.\n\n")
    
    # Print out the next question and increment    
    def next_question(self):
        
        from html import unescape
        import textwrap
        
        # Get the question before incrementation
        current_question = self.question_list[self.question_number]
        
        # Increment questions
        self.question_number += 1
        
        # Ask the question and ask for user input
        q_text = textwrap.fill(f"Q{self.question_number}. {unescape(current_question.text)} (True/False)?: ", 90)
        answer = input(q_text + " ").title()
        
        # See if the user is correct 
        self.is_correct(current_question, answer)
        
        
    
    # Return the amount of questions remaining    
    def questions_remaining(self):
        return self.question_number < len(self.question_list)