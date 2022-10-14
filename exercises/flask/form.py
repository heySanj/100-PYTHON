from flask import Flask, render_template, request
from markupsafe import escape # Escape input strings to prevent injection attacks
import random
import datetime
import requests

# -----------------------------------------------------------------------------

# Initialize new Flask application
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")


# Use flask request to catch POST or PUT data: https://flask.palletsprojects.com/en/1.1.x/quickstart/#the-request-object
@app.route('/login', methods=['POST', 'GET'])
def login():
    username = ""
    password = ""
    error = ""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
    else:        
        error = 'GET method not supported'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', username=username, password=password, error=error)


if __name__ == '__main__':
    app.run(debug=True) # Run in debug mode to allow changes to be made without having to reload
