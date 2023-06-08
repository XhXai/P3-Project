from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

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
engine = create_engine('sqlite:///site.db')

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Create a table defined by the class structure
Base.metadata.create_all(engine)


 # User Input
name = input("Enter name of site.....")


# Create a site instance
new_site = Sites(site_name=name)


# Add the new site to the session
session.add(new_site)


# Commit the session
session.commit()

# Query the site by its site_id or any other unique identifier
# site_id = 1  # Replace with the actual site ID you want to update
# site = session.query(Site).filter_by(site_id=site_id).first()

# if site:
#     # Modify the attributes of the site object
#     site.site_name = "FaceBook"
#     site.url = "https://www.facebook.com/"

#     # Commit the session to persist the changes
#     session.commit()
#     print("Site updated successfully.")
# else:
#     print("Site not found.")


# Query the site by its site_id or any other unique identifier
# site_id = 1 # Replace with the actual site ID you want to delete
# site = session.query(Sites).filter_by(site_id=site_id).first()

# if site:
#     # Delete the site
#     session.delete(site)
#     session.commit()
#     print("Site deleted successfully.")
# else:
#     print("Site not found.")

