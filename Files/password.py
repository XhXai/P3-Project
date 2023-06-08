from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
import random
import string

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    sites = relationship("Sites", back_populates='user')

class Sites(Base):
    __tablename__ = 'sites'

    site_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    site_name = Column(String(100), nullable=False)
    url = Column(String(200))
    passwords = relationship('Password', back_populates='site')
    user = relationship('User', back_populates='sites')

class Password(Base):
    __tablename__ = 'passwords'

    password_id = Column(Integer, primary_key=True, autoincrement=True)
    site_id = Column(Integer, ForeignKey('sites.site_id'))
    password = Column(String(100), nullable=False)

    site = relationship('Sites', back_populates='passwords')

# Create the engine
engine = create_engine('sqlite:///password.db')

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Create a table defined by the class structure
Base.metadata.create_all(engine)

def generate_password(length=10):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def check_password_strength(password):
    length = len(password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)

    if length >= 8 and has_upper and has_lower and has_digit and has_special:
        return "Strong"
    elif length >= 6 and (has_upper or has_lower) and (has_digit or has_special):
        return "Moderate"
    else:
        return "Weak"
    

# User Input
site_name = input("Enter the name of the site: ")

# Create a site instance
new_site = Sites(site_name=site_name)

# Generate passwords as a list
passwords = [generate_password() for _ in range(5)]  # Generate 5 passwords

# Create password instances and add them to the site
for password in passwords:
    new_password = Password(password=password, site=new_site)
    session.add(new_password)

# Check the password strength for each password in the list
strengths = [check_password_strength(password) for password in passwords]

# Add the new site and passwords to the session
session.add(new_site)

# Commit the session
session.commit()

print("Passwords generated and stored successfully.")
print("Password strengths: ", strengths)



