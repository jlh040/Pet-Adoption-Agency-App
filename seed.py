from models import db, Pet
from app import app

#Create pets
cornelius = Pet('Cornelius', 'dog', age = 15, notes = 'Very good dog')
sandra = Pet('Sandra', 'dog', age = 7, notes = 'Also a very good dog')
matthew = Pet('Matthew', 'cat', age = 15, notes = 'A devious cat')
bubbles = Pet('Bubbles', 'dolphin', age = 67, notes = 'A wise and happy dolphin', available = False,
            photo_url = 'https://images.unsplash.com/photo-1570481662006-a3a1374699e8?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=802&q=80')

#Create all tables
db.drop_all()
db.create_all()

#Delete any data if there is any
Pet.query.delete()

#Add to session
db.session.add_all([cornelius, sandra, matthew, bubbles])

#Commit the data to the database
db.session.commit()