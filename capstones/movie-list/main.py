from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


## CREATE DATABASE ------------------------------------------------------
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movie-collection.db"
db = SQLAlchemy(app)
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    
    #Optional: this will allow each movie object to be identified by its title when printed.
    def __repr__(self):
        return f'<Movie {self.title}>'
    
# Create the tables
with app.app_context():
    db.create_all()
    
# # Create initial entry
# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
# with app.app_context():
#     db.session.add(new_movie)
#     db.session.commit()   


## FORMS ----------------------------------------

class EditForm(FlaskForm):
    # Have a look at the basic fields of WTForms: https://wtforms.readthedocs.io/en/2.3.x/fields/#basic-fields
    new_rating = StringField(label='Your Rating Out of 10 e.g. 7.5', validators=[DataRequired()])
    new_review = StringField(label='Your Review', validators=[DataRequired()])
    submit = SubmitField('Update')

class AddForm(FlaskForm):
    # Have a look at the basic fields of WTForms: https://wtforms.readthedocs.io/en/2.3.x/fields/#basic-fields
    new_movie_title = StringField(label='Movie Title', validators=[DataRequired()])
    submit = SubmitField('Add Movie')
    
## PAGE ROUTING ------------------------------------------------------

@app.route("/")
def home():
    # Sort all movies in descending order
    all_movies = Movie.query.order_by(Movie.rating.desc()).all()
    
    # Update their ratings
    for movie in all_movies:
        movie.ranking = all_movies.index(movie) + 1
        db.session.commit()
    
    return render_template("index.html", movies=all_movies)

@app.route("/add", methods=['POST', 'GET'])
def add():
    add_form = AddForm()
    
    if add_form.validate_on_submit():
        # --------- Code to search API for movie details goes here 👇 -----------
        query = add_form.new_movie_title.data
        parameters = {
            "api_key": os.environ.get('TMDB_API'),
            "query": query
        }

        response = requests.get("https://api.themoviedb.org/3/search/movie", params=parameters, verify=False)
        response.raise_for_status() # Raise exceptions
        data = response.json()
        movies = data['results']
        return render_template("select.html", movies=movies)    
    
    return render_template("add.html", form=add_form)

@app.route("/find")
def find_movie():
    
    # The movie argument is a dictionary passed as string through the URL -> needs to be converted to dict
    movie = eval(request.args.get('movie')) 

    if movie:
        # Add the movie to the database
        new_movie = Movie(
            title=movie['title'],
            year=movie['release_date'][:4],
            description=movie['overview'],
            rating=0,
            ranking=0,
            review="",
            img_url=f"https://image.tmdb.org/t/p/w500{movie['poster_path']}"
        )
        db.session.add(new_movie)
        db.session.commit()
        
        # Redirect to edit page after getting the new movie ID
        # db_movie = Movie.query.filter_by(title=movie['title']).first()
        # movie_id = db_movie.id
        # print("================================================")
        # print(type(movie_id), movie_id)
        # print("================================================")
        
        return redirect(url_for('edit', id=new_movie.id))

@app.route("/edit", methods=['POST', 'GET'])
def edit():
    
    edit_form = EditForm()
    movie_id = request.args.get('id')
    
    if edit_form.validate_on_submit():
        
        # get the movie from the database and update values from the form
        movie_to_update = Movie.query.get(movie_id)
        movie_to_update.rating = edit_form.new_rating.data
        movie_to_update.review = edit_form.new_review.data
        
        # Commit Changes
        db.session.commit()
            
        return redirect(url_for('home'))   
    
    return render_template("edit.html", form=edit_form)


@app.route("/delete", methods=['GET'])
def delete():
    
    movie_id = request.args.get('id')
    movie_to_delete = Movie.query.get(movie_id)     
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
