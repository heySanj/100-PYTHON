from flask import Flask, render_template
from markupsafe import escape # Escape input strings to prevent injection attacks

# -----------------------------------------------------------------------------

# Initialize new Flask application
app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def home():
    return render_template('index.html')

@app.route('/pages/<page_name>')
def load_page(page_name):
    return render_template("./pages/" + escape(page_name))

if __name__ == '__main__':
    app.run(debug=True) # Run in debug mode to allow changes to be made without having to reload
