import json
import os

filename = 'favorite_number.json'

if os.path.exists(filename):
    try:
        with open(filename, 'r') as f:
            favorite_number = json.load(f)
        print(f"I know your favorite number! It's {favorite_number}.")
    except json.JSONDecodeError:
        print("There was an error reading the favorite number from the file.")
else:
    favorite_number = input("What is your favorite number? ")

    with open(filename, 'w') as f:
        json.dump(favorite_number, f)

    print("Your favorite number has been saved!")
