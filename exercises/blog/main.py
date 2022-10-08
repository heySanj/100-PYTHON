from flask import Flask, render_template
from markupsafe import escape # Escape input strings to prevent injection attacks
import random
import datetime
import requests

app = Flask(__name__)

@app.route('/')
def home():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    response.raise_for_status() # Raise an error if it occurs
    all_posts = response.json()
    return render_template("index.html", posts=all_posts)

@app.route('/post/<num>')
def post(num):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    response.raise_for_status() # Raise an error if it occurs
    all_posts = response.json()
    this_post = next((post for post in all_posts if post["id"] == int(escape(num))), None) # Find the specific post using ID
    return render_template("post.html", post=this_post)

if __name__ == "__main__":
    app.run(debug=True)
