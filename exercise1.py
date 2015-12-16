import sqlalchemy

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_puppies import Base, Shelter, Puppy


engine = create_engine('sqlite:///puppies.db')
Base.metadata.bind=engine
Session = sessionmaker(bind=engine)
session = Session()

#1. Query all of the puppies and return the results in ascending alphabetical order
dogs = session.query(Puppy.name).order_by(Puppy.name).all()
print dogs

#2. Query all of the puppies that are less than 6 months old organized by the youngest first
youngDogs = session.query(Puppy.dateOfBirth).filter(Puppy.dateOfBirth > 180)
print youngDogs