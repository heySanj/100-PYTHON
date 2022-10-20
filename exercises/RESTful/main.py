from select import select
from xmlrpc.client import boolean
from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import func

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)
    
    
    
# Function that will automatically serialize database info into a dictionary   
def to_dict(self):
    #Method 1. 
    dictionary = {}
    # Loop through each column in the data record
    for column in self.__table__.columns:
        #Create a new dictionary entry;
        # where the key is the name of the column
        # and the value is the value of the column
        dictionary[column.name] = getattr(self, column.name)
    return dictionary
    
    #Method 2. Altenatively use Dictionary Comprehension to do the same thing.
    return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")
    
    
@app.route("/random", methods=['GET'])
def get_random_cafe():
    if request.method == 'GET':
        # Randomly order the list of cafes and then pick the first
        random_cafe = db.session.query(Cafe).order_by(func.random()).first()

        # Manually create a data dictionary that gets serialized into JSON
        data = {'cafe':{
            'name': random_cafe.name,
            'map_url': random_cafe.map_url,
            'img_url': random_cafe.img_url,
            'location': random_cafe.location,
            'seats': random_cafe.seats,
            'has_toilet': random_cafe.has_toilet,
            'has_wifi': random_cafe.has_wifi,
            'has_sockets': random_cafe.has_sockets,
            'can_take_calls': random_cafe.can_take_calls,
            'coffee_price': random_cafe.coffee_price,
        }}
        return jsonify(data)
    
    
@app.route("/all", methods=['GET'])
def get_all_cafes():
    if request.method == 'GET':
        # Randomly order the list of cafes and then pick the first
        all_cafes = Cafe.query.all()
        data_list = []
        
        # Loop through each cafe and turn it into a dictionary
        for cafe in all_cafes:
            cafe_data = to_dict(cafe)
            data_list.append(cafe_data)
            
        data = {'cafes': data_list}
        
        # Can also be done using list comprehension
        # return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])
        
        return jsonify(data)
    
    
@app.route("/search", methods=['GET'])
def search_cafe():
    if request.method == 'GET':
        location_query = request.args.get('loc')
        
        # Find all cafes at the location
        cafes_at_loc = Cafe.query.filter_by(location=location_query)
        
        # Return serialized result
        if cafes_at_loc.count() > 0:
            return jsonify(cafes=[to_dict(cafe) for cafe in cafes_at_loc])
        else:
            return jsonify(error={"Not Found":"Sorry, we don't have a cafe at that location."})


@app.route("/add", methods=['POST'])
def add_cafe():
    if request.method == 'POST':
        # Make sure to eval the boolean values to convert them from string
        new_cafe = Cafe(
            name = request.form.get('name'),
            map_url = request.form.get('map_url'),
            img_url = request.form.get('img_url'),
            location = request.form.get('location'),
            seats = request.form.get('seats'),
            has_toilet = eval(request.form.get('has_toilet')),
            has_wifi = eval(request.form.get('has_wifi')),
            has_sockets = eval(request.form.get('has_sockets')),
            can_take_calls = eval(request.form.get('can_take_calls')),
            coffee_price = request.form.get('coffee_price')
        )
        db.session.add(new_cafe)
        db.session.commit()
        return jsonify(response={"Success":"Successfully added the new cafe."})
    
    
@app.route("/update-price/<cafe_id>", methods=['PATCH'])
def update_price(cafe_id):
    if request.method == 'PATCH':
        new_price = request.args.get('new_price')
                        
        # Get the cafe that needs updating and update price
        cafe = db.session.query(Cafe).get(cafe_id)
        
        # If a cafe was found
        if cafe:        
            cafe.coffee_price = new_price
            db.session.commit()
            return jsonify(success="Successfully updated the price"), 200
        else:
            # Pass a 404 error code as well to show that results weren't found
            return jsonify(error={"Not Found":"Sorry, we couldn't find a cafe with that ID"}), 404


@app.route("/report-closed/<cafe_id>", methods=['DELETE'])
def delete_cafe(cafe_id):
    if request.method == 'DELETE':
        input_key = request.args.get('api_key')
        
        # Get the cafe that is to be deleted
        cafe = db.session.query(Cafe).get(cafe_id)
        
        # If a cafe was found
        if cafe:
            
            # If the api key matches the authorized one
            if input_key == "TopSecretAPIKey":
                db.session.delete(cafe)
                db.session.commit()
                return jsonify(success="Successfully deleted the cafe."), 200
            else:
                return jsonify(error={"Unauthorized":"Sorry, that's not allowed. Please make sure you have the correct API key."}), 403
        else:
            # Pass a 404 error code as well to show that results weren't found
            return jsonify(error={"Not Found":"Sorry, we couldn't find a cafe with that ID"}), 404
            
        
## HTTP GET - Read Record

## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
