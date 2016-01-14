import sqlalchemy
import datetime
import math

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_puppies import Base, Shelter, Puppy


engine = create_engine('sqlite:///puppies.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

#1. Query all of the puppies and return the results in ascending alphabetical order
dogs = session.query(Puppy).order_by(Puppy.name).all()
#for dog in dogs:
#	print dog.name


#2. Query all of the puppies that are less than 6 months old organized by the youngest first
sixMonthsOld = datetime.date.today() - datetime.timedelta(days=180)
youngDogs = session.query(Puppy).filter(Puppy.dateOfBirth > sixMonthsOld)
#for youngDog in youngDogs:
#	print youngDog.name

#3. Query all puppies by ascending weight
weightDogs = session.query(Puppy).order_by(Puppy.weight)
#for weightDog in weightDogs:
#	print (math.ceil(weightDog.weight*1))

#4. Query all puppies grouped by the shelter in which they are staying
puppiesGrouped = session.query(Puppy).join(Shelter).order_by(Puppy.shelter_id).all()
for puppyGrouped in puppiesGrouped:
	print puppyGrouped.name, puppyGrouped.shelter_id