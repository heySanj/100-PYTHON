from flask import Flask, render_template, request
from markupsafe import escape # Escape input strings to prevent injection attacks
import random
import datetime
import requests
import os

# -----------------------------------------------------------------------------

from smtp.mail_message import Email

def send_email(name, email, phone, message):
    
    new_message = f'''
        Name: {name}
        Email: {email}
        Phone: {phone}
        _____________________________________________
            
        {message}'''
        
    new_email = Email(
        username=os.environ.get("EMAIL_USER"),
        password=os.environ.get("EMAIL_PASS"),
        sender="Blog Contact Form",
        recipient=os.environ.get("RECIPIENT"),
        subject=f"{name} wants to get in touch!",
        message=new_message
    )
   
    # Send it
    new_email.send()

# -----------------------------------------------------------------------------

# Initialize new Flask application
app = Flask(__name__)

def get_posts():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    response.raise_for_status() # Raise an error if it occurs
    return response.json()

@app.route('/')
def home():
    all_posts = get_posts()
    return render_template("index.html", posts=all_posts)

@app.route('/about')
def about():
    return render_template('about.html')

# @app.route('/contact')
# def contact():
#     return render_template('contact.html')

@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']    
        send_email(name,email,phone,message)
        return render_template('contact.html', sent=True)
    return render_template('contact.html', sent=False)

@app.route('/post/<num>')
def post(num):
    all_posts = get_posts()
    this_post = next((post for post in all_posts if post["id"] == int(escape(num))), None) # Find the specific post using ID
    return render_template("post.html", post=this_post)

if __name__ == '__main__':
    app.run(debug=True) # Run in debug mode to allow changes to be made without having to reload
