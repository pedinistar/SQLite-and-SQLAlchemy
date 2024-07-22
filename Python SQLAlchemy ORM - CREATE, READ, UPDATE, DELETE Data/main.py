# Creation of a database table using SQLAlchemy ORM
# import the modules
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import declarative_base

# URL
db_url = 'sqlite:///Python SQLAlchemy ORM - CREATE, READ, UPDATE, DELETE Data/database-2.py'

# Data engine creation
engine = create_engine(db_url)

# Declarative Base Class
Base = declarative_base() # (here Base is the base class from where other classes will be inheriting)

# Declaring a new Class Student
class Student(Base):
  __tablename__ = 'students'
  student_id = Column(Integer, primary_key=True)
  name = Column(String(40), nullable=False)



