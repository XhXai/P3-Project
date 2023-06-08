from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)


#Create the engine.
engine = create_engine('sqlite:///user.db')

#Create a session.
Session = sessionmaker(bind=engine)
session = Session()

#Create a table defined by the class structure.
Base.metadata.create_all(engine)

#User Input
username = input("Enter your Username.....")
email = input("Enter your Email.....")

#Create a new user instances
new_user = User(username=username, email=email)

#Add the new user to the session
session.add(new_user)

#Commit the session
session.commit()

#Query the site by its site_id or any other unique identifier
# user_id = 2 # Replace with the actual site ID you want to delete
# User = session.query(User).filter_by(user_id=user_id).first()

# if User:
#     # Delete the site
#     session.delete(User)
#     session.commit()
#     print("User deleted successfully.")
# else:
#     print("User not found.")


# Query the site by its site_id or any other unique identifier
# user_id = 3  # Replace with the actual site ID you want to update
# User = session.query(User).filter_by(user_id=user_id).first()

# if User:
#     # Modify the attributes of the site object
#     User.user_name = "FaceBook"
    

#     # Commit the session to persist the changes
#     session.commit()
#     print("User updated successfully.")
# else:
#     print("User not found.")