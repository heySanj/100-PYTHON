from flask import Flask
from markupsafe import escape # Escape input strings to prevent injection attacks
import random

# Initialize new Flask application
app = Flask(__name__)
target_num = random.randint(0,9)

# What to do when the user visits the home page ('/')
@app.route('/')
def home():
    return '''  <h1>Guess a number between 0 and 9</h1>
                <img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'''

@app.route('/<int:num>')
def guess(num):
    if num < target_num:
        return  '''
                    <h1 style="color: red">Too low, try again!</h1>
                    <img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">
                    
                '''
    elif num > target_num:
        return  '''
            <h1 style="color: red">Too high, try again!</h1>
            <img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">
            
        '''        
    else:
        return  '''
            <h1 style="color: green">You found me!</h1>
            <img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">
            
        '''   
        

# 'flask run' in the command line to run the server!

# OR run this application ONLY if it is in the MAIN SCOPE, by checking to see if __name__ is equal to __main__
# IE: dont execute this if it is being imported and run by another script
if __name__ == '__main__':
    app.run(debug=True) # Run in debug mode to allow changes to be made without having to reload