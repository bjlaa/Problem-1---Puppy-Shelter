import sqlalchemy
import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_puppies import Base, Shelter, Puppy


engine = create_engine('sqlite:///puppies.db')
Base.metadata.bind=engine
Session = sessionmaker(bind=engine)
session = Session()

#1. Query all of the puppies and return the results in ascending alphabetical order
dogs = session.query(Puppy).order_by(Puppy.name).all()
dogsNames = session.query(Puppy.name).order_by(Puppy.name).all()
#print dogs
#print dogsNames

#2. Query all of the puppies that are less than 6 months old organized by the youngest first
sixMonthsOld = datetime.date.today() - datetime.timedelta(days=180)
youngDogs = session.query(Puppy.name).filter(Puppy.dateOfBirth > sixMonthsOld)
#print youngDogs

#3. Query all puppies by ascending weight
weightDogs = session.query(Puppy.weight).order_by(Puppy.weight).all()
#print weightDogs

#4. Query all puppies grouped by the shelter in which they are staying
puppiesGrouped = session.query(Puppy).join(Shelter).order_by(Puppy.shelter_id).all()
print puppiesGrouped