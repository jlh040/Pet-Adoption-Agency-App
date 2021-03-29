from flask import Flask, session, render_template, flash, redirect, request
from flask_debugtoolbar import DebugToolbarExtension
from models import connect_db, Pet
from forms import AddPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)

app.config['SECRET_KEY'] = '3m7z9n2x'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

@app.route('/')
def show_homepage():
    """Show a listing of all the pets."""
    all_pets = Pet.query.all()
    return render_template('homepage.html', pets=all_pets)

@app.route('/add')
def add_pet():
    """Add a pet to the database."""
    return render_template('add_pet.html')