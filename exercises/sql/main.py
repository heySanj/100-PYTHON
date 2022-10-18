from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

##CREATE DATABASE ------------------------------------------------------
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books-collection.db"
db = SQLAlchemy(app)
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    
    #Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'
    
# Create the tables
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    all_books = db.session.query(Book).all()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        # Add the book to the database
        new_book = Book(title=request.form['title'], author=request.form['author'], rating=request.form['rating'])
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    
    return render_template("add.html")


@app.route("/edit", methods=['POST', 'GET'])
def edit():
    
    # If a POST request -- ie: An edit is being sent through
    if request.method == 'POST':
        book_id = request.form['id']
        book_to_update = Book.query.get(book_id)
        book_to_update.rating = request.form['new_rating']
        
        # Commit Changes
        db.session.commit()
            
        return redirect(url_for('home'))
    
    else:
        # Otherwise if its just to display what is being edited
        # Use request.args.get() to access parameters in a URL
        book_id = request.args.get('id')
        book_to_update = Book.query.get(book_id)
        
        return render_template("edit.html", book=book_to_update)


@app.route("/delete", methods=['GET'])
def delete():
    
    book_id = request.args.get('id')
    book_to_delete = Book.query.get(book_id)     
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

