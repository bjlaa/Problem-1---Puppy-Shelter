import sqlalchemy

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_puppies import Base, Shelter, Puppy


engine = create_engine('sqlite:///puppies.db')
Base.metadata.bind=engine
Session = sessionmaker(bind=engine)
session = Session()

dogs = session.query(Puppy).all()
print dogs