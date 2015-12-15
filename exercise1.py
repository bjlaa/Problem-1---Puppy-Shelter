import sqlalchemy

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from puppies import Base, Shelter, Puppy


engine = create_engine('sqlite:///exercise2')
Base.metadata.bind=engine
Session = sessionmaker(bind=engine)
session = Session()

dogs = session.query(Puppy).all()