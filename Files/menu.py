from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from users import User
from sites import Sites
from password import Password

# Create the engine
engine = create_engine('sqlite:///password.db')

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

def display_menu():
    print("Password Manager Menu")
    print("1. Add a new user")
    print("2. Delete a user")
    print("3. Add a new site")
    print("4. Update a site")
    print("5. Delete a site")
    print("6. Add a new password")
    print("7. Delete a password")
    print("8. Display all users")
    print("9. Display all sites")
    print("10. Exit")

def add_user():
    username = input("Enter the username: ")
    email = input("Enter the email: ")

    # Create a new User instance
    new_user = User(username=username, email=email)

    # Add the new user to the session
    session.add(new_user)
    session.commit()
    print("User added successfully.")

def delete_user():
    user_id = input("Enter the user ID to delete: ")

    # Query the User instance by user_id
    user = session.query(User).filter_by(user_id=user_id).first()

    if user:
        # Delete the user
        session.delete(user)
        session.commit()
        print("User deleted successfully.")
    else:
        print("User not found.")

def add_site():
    site_name = input("Enter the name of the site: ")
    url = input("Enter the URL: ")
    user_id = input("Enter the user ID associated with the site: ")

    # Query the User instance by user_id
    user = session.query(User).filter_by(user_id=user_id).first()

    if user:
        # Create a new Site instance associated with the user
        new_site = Sites(site_name=site_name, url=url, user=user)

        # Add the new site to the session
        session.add(new_site)
        session.commit()
        print("Site added successfully.")
    else:
        print("User not found.")

def update_site():
    site_id = input("Enter the site ID to update: ")

    # Query the Site instance by site_id
    site = session.query(Sites).filter_by(site_id=site_id).first()

    if site:
        new_site_name = input("Enter the new site name (leave blank to keep current): ")
        new_url = input("Enter the new URL (leave blank to keep current): ")

        if new_site_name:
            site.site_name = new_site_name

        if new_url:
            site.url = new_url

        session.commit()
        print("Site updated successfully.")
    else:
        print("Site not found.")

def delete_site():
    site_id = input("Enter the site ID to delete: ")

    # Query the Site instance by site_id
    site = session.query(Sites).filter_by(site_id=site_id).first()

    if site:
        # Delete the site
        session.delete(site)
        session.commit()
        print("Site deleted successfully.")
    else:
        print("Site not found.")

def add_password():
    site_id = input("Enter the site ID for the password: ")
    password = input("Enter the password: ")

    # Query the Site instance by site_id
    site = session.query(Sites).filter_by(site_id=site_id).first()

    if site:
        # Create a new Password instance associated with the site
        new_password = Password(password=password, site=site)

        # Add the new password to the session
        session.add(new_password)
        session.commit()
        print("Password added successfully.")
    else:
        print("Site not found.")

def delete_password():
    password_id = input("Enter the password ID to delete: ")

    # Query the Password instance by password_id
    password = session.query(Password).filter_by(password_id=password_id).first()

    if password:
        # Delete the password
        session.delete(password)
        session.commit()
        print("Password deleted successfully.")
    else:
        print("Password not found.")

def display_users():
    users = session.query(User).all()
    print("Users:")
    for user in users:
        print(f"User ID: {user.user_id}, Username: {user.username}, Email: {user.email}")

def display_sites():
    sites = session.query(Sites).all()
    print("Sites:")
    for site in sites:
        print(f"Site ID: {site.site_id}, Name: {site.site_name}, URL: {site.url}, User ID: {site.user_id}")


# Create a table defined by the class structure
User.metadata.create_all(engine)
Sites.metadata.create_all(engine)
Password.metadata.create_all(engine)

if __name__ == "__main__":
    while True:
        display_menu()
        choice = input("Enter your choice (1-10): ")

        if choice == '1':
            add_user()
        elif choice == '2':
            delete_user()
        elif choice == '3':
            add_site()
        elif choice == '4':
            update_site()
        elif choice == '5':
            delete_site()
        elif choice == '6':
            add_password()
        elif choice == '7':
            delete_password()
        elif choice == '8':
            display_users()
        elif choice == '9':
            display_sites()
        elif choice == '10':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
