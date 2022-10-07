from flask import Flask, render_template
from markupsafe import escape # Escape input strings to prevent injection attacks
import datetime

# -----------------------------------------------------------------------------

# Initialize new Flask application
app = Flask(__name__)

@app.route('/')
def home():
    year = datetime.date.today().year
    return render_template('index.html', year=year)

if __name__ == '__main__':
    app.run(debug=True) # Run in debug mode to allow changes to be made without having to reload
