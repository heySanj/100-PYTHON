from flask import Flask, render_template
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

@app.route('/')
@app.route('/index.html')
def home():
    return render_template('index.html')

@app.route('/pages/<page_name>')
def load_page(page_name):
    return render_template("./pages/" + page_name)


@app.route('/username/<name>/<int:age>')
def greet(name, age):
    return f"Hello there {escape(name)}, you are {age} years old!"


if __name__ == '__main__':
    app.run(debug=True) # Run in debug mode to allow changes to be made without having to reload
