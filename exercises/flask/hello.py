from flask import Flask
from markupsafe import escape # Escape input strings to prevent injection attacks

# Decorators
def make_bold(function):
    def wrapper_function():
        return f"<b>{function()}</b>"    
    return wrapper_function

def make_italic(function):
    def wrapper_function():
        return f"<em>{function()}</em>"    
    return wrapper_function

def make_underline(function):
    def wrapper_function():
        return f"<u>{function()}</u>"    
    return wrapper_function

# -----------------------------------------------------------------------------

# Initialize new Flask application
app = Flask(__name__)

# What to do when the user visits the home page ('/')
@app.route('/') # Python decorator syntax
def hello_world():
    return '''  <h1 style="color: navy">Hello, World!</h1>
                <p>This is a paragraph</p>
                <img src="https://media4.giphy.com/media/Vbtc9VG51NtzT1Qnv1/giphy.gif?cid=ecf05e47yb50lgq4gqsgwiql3ntyv3x59qsitw29sqjhr29u&rid=giphy.gif&ct=g">'''

@app.route('/bye') # Python decorator syntax
@make_bold
@make_italic
@make_underline
def say_bye():
    return "Bye"

@app.route('/username/<name>/<int:age>')
def greet(name, age):
    return f"Hello there {escape(name)}, you are {age} years old!"

# 'flask run' in the command line to run the server!

# OR run this application ONLY if it is in the MAIN SCOPE, by checking to see if __name__ is equal to __main__
# IE: dont execute this if it is being imported and run by another script
if __name__ == '__main__':
    app.run(debug=True) # Run in debug mode to allow changes to be made without having to reload