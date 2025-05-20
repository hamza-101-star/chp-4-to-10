import json
import os

filename = 'username.json'

def greet_user():
    """Greet the user, verifying their username."""
    if os.path.exists(filename):
        try:
            with open(filename, 'r') as f:
                username = json.load(f)

            correct_username = input(f"Is your username {username}? (yes/no) ").strip().lower()

            if correct_username == 'yes':
                print(f"Welcome back, {username}!")
            else:
                get_new_username()

        except json.JSONDecodeError:
            print("There was an error reading the username.")
    else:
        get_new_username()

def get_new_username():
    """Get a new username from the user and store it."""
    username = input("What is your username? ")
    with open(filename, 'w') as f:
        json.dump(username, f)
    print(f"Welcome, {username}! Your username has been saved.")

greet_user()
