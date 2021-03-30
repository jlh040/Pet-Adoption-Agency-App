from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField
from wtforms.validators import AnyOf, Optional, URL, NumberRange

class AddPetForm(FlaskForm):
    """Make a form for adding a pet."""
    pet_name = StringField('Pet name', render_kw={'placeholder': 'Enter a pet name'})
    species = StringField('Species', render_kw={'placeholder': 'Enter a species'}, validators=[AnyOf(values=['cat', 'dog', 'porcupine'])])
    photo_url = StringField('Photo URL', render_kw={'placeholder': 'Enter a photo url'}, validators=[URL(), Optional()])
    age = IntegerField('Age', render_kw={'placeholder': 'Enter an age'}, validators=[NumberRange(min=0, max=30), Optional()])
    notes = TextAreaField('Notes', render_kw={'placeholder': 'Provide notes for the animal'})