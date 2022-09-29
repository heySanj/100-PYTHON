from flask import Flask

# Initialize new Flask application
app = Flask(__name__)

# What to do when the user visits the home page ('/')
@app.route('/') # Python decorator syntax
def hello_world():
    return 'Hello, World!'

@app.route('/bye') # Python decorator syntax
def say_bye():
    return "Bye"


# 'flask run' in the command line to run the server!

# OR run this application ONLY if it is in the MAIN SCOPE, by checking to see if __name__ is equal to __main__
# IE: dont execute this if it is being imported and run by another script
if __name__ == '__main__':
    app.run()