from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'NowThisIsASecretKeyAGuyCouldUse'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
login_manager = LoginManager()
login_manager.init_app(app)
db = SQLAlchemy(app)

##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
#Line below only required once, when creating DB. 
# db.create_all()

def delete_all_users():
    db.session.query(User).delete()
    db.session.commit()

@app.route('/')
def home():
    # delete_all_users()
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods = ['GET','POST'])
def register():
    if request.method == 'POST':
        
        # check for an existing user
        user = User.query.filter_by(email=request.form['email']).first()
        
        if not user:            
            new_user = User(
                email = request.form['email'],
                password = generate_password_hash(password=request.form['password'], method="pbkdf2:sha256", salt_length=8),
                name = request.form['name']
            )
            db.session.add(new_user)
            db.session.commit()
                        
            #Log in and authenticate user after adding details to database.
            login_user(new_user)            
            return redirect(url_for('secrets'))
        else:
            # User already exists so go to login page
            flash("You already have an account with that email. Please log in.")
            return redirect(url_for('login'))
        
    return render_template("register.html", logged_in=current_user.is_authenticated)


@app.route('/login', methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        # Log the user in if password matches
        user = User.query.filter_by(email=request.form['email']).first()
        
        #Email doesn't exist
        if not user:
            flash("That email does not exist, please try again.")
            return redirect(url_for('login'))
        #Password incorrect
        elif not check_password_hash(user.password, request.form['password']):
            flash('Password incorrect, please try again.')
            return redirect(url_for('login'))
        #Email exists and password correct
        else:
            login_user(user)
            return redirect(url_for('secrets'))

   
        
    return render_template("login.html", logged_in=current_user.is_authenticated)


@app.route('/secrets', methods = ['GET'])
@login_required
def secrets():
   return render_template("secrets.html", user=current_user, logged_in=current_user.is_authenticated)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download', methods = ['GET'])
@login_required
def download():
    return send_from_directory('static', 'files/cheat_sheet.pdf')


# ------------------------------ user management -------------------------------
@login_manager.user_loader
def load_user(user_id):
    if User.query.get(user_id):
        return User.query.get(user_id)
    return None


if __name__ == "__main__":
    app.run(debug=True)
