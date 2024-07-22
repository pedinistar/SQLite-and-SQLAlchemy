from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base

db_url = "sqlite:///database.db"

engine = create_engine(db_url)

# DECLARATIVE BASE CLASS
Base = declarative_base()

# CREATING A TABLE
class User(Base):
  # class name ka plural version hoga table ka naam
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True)
  name = Column(String)
  age = Column(Integer)

# THIS WILL CREATE THE DATABASE AND ALL THE TABLES ASSOCIATED WITH IT
Base.metadata.create_all(engine)
