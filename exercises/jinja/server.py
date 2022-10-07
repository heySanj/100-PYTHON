from flask import Flask, render_template
from markupsafe import escape # Escape input strings to prevent injection attacks
import random
import datetime
import requests

# -----------------------------------------------------------------------------

# Initialize new Flask application
app = Flask(__name__)

def get_age(name):
    response = requests.get(url=f"https://api.agify.io?name={name}")
    response.raise_for_status() # Raise an error if it occurs
    age = response.json()['age']
    return age

def get_gender(name):
    response = requests.get(url=f"https://api.genderize.io/?name={name}")
    response.raise_for_status() # Raise an error if it occurs
    gender = response.json()['gender']
    return gender

@app.route('/')
def home():
    random_number = random.randint(1,100)
    year = datetime.date.today().year
    return render_template('index.html', num=random_number, year=year)

@app.route('/guess/<name>')
def guess(name):
    age = get_age(name)
    gender = get_gender(name)
    return render_template('guess.html', name=name.title(), age=age, gender=gender)

@app.route('/blog')
def blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    response.raise_for_status() # Raise an error if it occurs
    all_posts = response.json()
    return render_template('blog.html', posts=all_posts)


if __name__ == '__main__':
    app.run(debug=True) # Run in debug mode to allow changes to be made without having to reload
