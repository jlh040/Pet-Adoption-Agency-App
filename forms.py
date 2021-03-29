from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField

class AddPetForm(FlaskForm):
    """Make a form for adding a pet."""
    pet_name = StringField('Pet name', render_kw={'placeholder': 'Enter a pet name'})
    species = StringField('Species', render_kw={'placeholder': 'Enter a species'})
    photo_url = StringField('Photo URL', render_kw={'placeholder': 'Enter a photo url'})
    age = IntegerField('Age', render_kw={'placeholder': 'Enter an age'})
    notes = StringField('Notes', render_kw={'placeholder': 'Provide notes for the animal'})