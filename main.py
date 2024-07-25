from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

db_url = "sqlite:///database.db"

engine = create_engine(db_url)

Base = declarative_base()

class User(Base):
  __tablename__ = 'users'

  # id = Column(Integer, primary_key= True)


Base.metadata.create_all(engine)
