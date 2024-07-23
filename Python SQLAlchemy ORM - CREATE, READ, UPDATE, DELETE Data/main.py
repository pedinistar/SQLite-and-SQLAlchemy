# Creation of a database table using SQLAlchemy ORM
# import the modules
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import declarative_base, sessionmaker

# URL
db_url = 'sqlite:///Python SQLAlchemy ORM - CREATE, READ, UPDATE, DELETE Data/database-2.db'

# Data engine creation
engine = create_engine(db_url)

# Declarative Base Class
Base = declarative_base() # (here Base is the base class from where other classes will be inheriting)

# Declaring a new Class Student
class Student(Base):
  __tablename__ = 'students'
  student_id = Column(Integer, primary_key=True)
  name = Column(String(40), nullable=False)
  date_of_birth = Column(Integer, nullable=False)


# Now lets create the table
# Base.metadata.create_all(engine)
# The create_all function creates all tables as per the metadata
# As the above table is already in our database we have disabled the above line, if it is not disables, it will do no harm.
# Actually, if the table exists, it will not be created.





# Insertion of records in database tables using AQLAlchemy ORM

# Now lets create a session
Session = sessionmaker(bind=engine)
session = Session()


# Now create an object of a Student class
# student = Student(name='Ann', date_of_birth='1985-04-12')
# session.add(student)  # inserts an object as a record in the table
# session.commit()

# Lets create mutiple objects
# student1 = Student(name='Elsa', date_of_birth='1985-04-12')
# student2 = Student(name='Monaki', date_of_birth='1985-04-12')
# student3 = Student(name='Kira', date_of_birth='1985-04-12')
# session.add_all([student1, student2, student3])
# session.commit()




# SEARCH QUERY
student = session.query(Student).filter(Student.name == 'Monaki').first()
if student:
  print(student.student_id, student.name, student.date_of_birth)
else:
  print("No record found!")


students = session.query(Student.student_id, Student.name).all()
print(students)






# UPDATE RECORDS
student = session.query(Student).filter(Student.name=='Kira').first()
if student:
  student.name = 'Light'
  student.date_of_birth = 2323

session.commit()

print(students)





# Delete a particular record
student = session.query(Student).filter(Student.name=='Ann').first()
if student:
  session.delete(student)

session.commit()

print(students)