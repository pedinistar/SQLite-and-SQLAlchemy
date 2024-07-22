from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base

# URL
db_url = 'sqlite:///database-2.py'

# Engine Creation
engine = create_engine(db_url)

# Base
Base = declarative_base()


# DECLARING A NEW DERIVED CLASS User
# Creating a table
class User(Base):
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True)
  name = Column(String)
  age = Column(Integer)


# Create the Database and Table
Base.metadata.create_all(engine)
# As the above table is already in our database we have disabled the above line, if it is not disables, it will do no harm.
# Actually, if the table exists, it will not be created.
