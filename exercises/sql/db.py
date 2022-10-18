from msilib.schema import CreateFolder
from shutil import ReadError
import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# -------------------- THE OLD WAY ------------------

# # Connect to the database, it will be created if none exist
# db = sqlite3.connect("books-collection.db")

# # Cursor to navigate the database and add data
# cursor = db.cursor()

# # Execute SQL commands
# # cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

# # Insert data
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")

# # Save the data after insertion
# db.commit()

# -------------------- SQL ALCHEMY ------------------

# Create
# Read
# Update
# Delete

app = Flask(__name__)

##CREATE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
#Optional: But it will silence the deprecation warning in the console.
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define a table as a class
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

    # Add an entry to the Books table (Primary Key fields are optional as they will be automatically generated)
    new_book = Book(title="Blades of Glory", author="The Boss", rating="3.7")
    db.session.add(new_book)
    db.session.commit()
    
    
    # # Read all Records
    # all_books = db.session.query(Book).all()
    
    # # Read using Query
    # book = Book.query.filter_by(title="Harry Potter").first()
    
    # # Update particular record by Query
    # book_to_update = Book.query.filter_by(title="Harry Potter").first()
    # book_to_update.title = "Harry Potter and the Chamber of Secrets"
    # db.session.commit()  
    
    # Update a record by Primary Key
    # book_id = 1
    # book_to_update = Book.query.get(book_id)
    # book_to_update.title = "Harry Potter and the Goblet of Fire"
    # db.session.commit()  
    
    # # Delete a particular record by Primary Key
    # book_id = 1
    # book_to_delete = Book.query.get(book_id)
    # db.session.delete(book_to_delete)
    # db.session.commit()