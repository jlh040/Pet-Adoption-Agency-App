from flask import Flask, session, render_template, flash, redirect, request
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
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
    all_pets = db.session.query(Pet).filter(Pet.id > 0).order_by('id').all()
    return render_template('homepage.html', pets=all_pets)

@app.route('/add', methods=['POST', 'GET'])
def add_pet():
    """Add a pet to the database."""
    form = AddPetForm()
    pet_name = form.pet_name.data
    species = form.species.data
    photo_url = form.photo_url.data if form.photo_url.data else None
    age = form.age.data
    notes = form.notes.data

    if form.validate_on_submit():
        pet = Pet(pet_name=pet_name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(pet)
        db.session.commit()
        return redirect('/')

    return render_template('add_pet.html', form=form)

@app.route('/<int:pet_id_number>', methods=['GET', 'POST'])
def edit_pet(pet_id_number):
    """Edit an existing pet."""
    pet = Pet.query.get(pet_id_number)
    form = AddPetForm(obj=pet)
    print(form.data)
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = True if form.available.data == True else False
        db.session.commit()
        return redirect('/')

    return render_template('edit_page.html', pet=pet, form=form)