from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """Make a table of pets."""

    __tablename__ = 'pets'

    id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    pet_name = db.Column(db.Text, nullable = False)
    species = db.Column(db.Text, nullable = False)
    photo_url = db.Column(db.Text, default = 'https://images.unsplash.com/photo-1439405326854-014607f694d7?ixid=MXwxMjA3fDB8MHxzZWFyY2h8NHx8b2NlYW58ZW58MHx8MHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60')
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable = False, default = True)