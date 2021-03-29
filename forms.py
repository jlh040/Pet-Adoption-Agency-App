from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField

class AddPetForm(FlaskForm):
    """Make a form for adding a pet."""
    pet_name = StringField('Pet name')
    species = StringField('Species')
    photo_url = StringField('Photo URL')
    age = IntegerField('Age')
    notes = StringField('Notes')