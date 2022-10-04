from flask import Flask, render_template
from markupsafe import escape # Escape input strings to prevent injection attacks

# -----------------------------------------------------------------------------

# Initialize new Flask application
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True) # Run in debug mode to allow changes to be made without having to reload
