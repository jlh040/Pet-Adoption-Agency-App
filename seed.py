from models import db, Pet
from app import app

#Create pets
cornelius = Pet(pet_name = 'Cornelius', species = 'dog', age = 15, notes = 'Very good dog', photo_url = 'https://images.unsplash.com/photo-1583511655857-d19b40a7a54e?ixid=MXwxMjA3fDB8MHxzZWFyY2h8Mnx8ZG9nfGVufDB8fDB8&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60')
sandra = Pet(pet_name = 'Sandra', species = 'dog', age = 7, notes = 'Also a very good dog', photo_url = 'https://images.unsplash.com/photo-1587300003388-59208cc962cb?ixid=MXwxMjA3fDB8MHxzZWFyY2h8NHx8ZG9nfGVufDB8fDB8&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60')
matthew = Pet(pet_name = 'Matthew', species = 'cat', age = 15, notes = 'A devious cat', photo_url = 'https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MXx8Y2F0fGVufDB8fDB8&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60')
bubbles = Pet(pet_name = 'Bubbles', species = 'porcupine', age = 25, notes = 'A wise and happy dolphin', available = False,
            photo_url = 'https://images.unsplash.com/photo-1574671652898-fc04f34c7517?ixid=MXwxMjA3fDB8MHxzZWFyY2h8OHx8cG9yY3VwaW5lfGVufDB8fDB8&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60')

#Create all tables
db.drop_all()
db.create_all()

#Delete any data if there is any
Pet.query.delete()

#Add to session
db.session.add_all([cornelius, sandra, matthew, bubbles])

#Commit the data to the database
db.session.commit()