import sqlalchemy

from sqlalchemy import create_engine
engine = create_engine('sqlite:///exercise2', echo=True)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)

