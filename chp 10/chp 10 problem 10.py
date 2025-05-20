import json

# Prompt the user for their favorite number
favorite_number = input("What is your favorite number? ")

# Store the favorite number in a file
filename = 'favorite_number.json'

# Open the file and save the number as JSON
with open(filename, 'w') as f:
    json.dump(favorite_number, f)

print("Your favorite number has been saved!")


import json

# Read the favorite number from the file
filename = 'favorite_number.json'

try:
    with open(filename, 'r') as f:
        favorite_number = json.load(f)

    print(f"I know your favorite number! It's {favorite_number}.")

except FileNotFoundError:
    print("Sorry, I couldn't find your favorite number. Please run the first program first!")
