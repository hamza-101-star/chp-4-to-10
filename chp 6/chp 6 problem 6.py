favorite_languages = {
    'ali': 'python',
    'ahmed': 'java',
    'fahad': 'c++',
    'hassan': 'javascript'
}

# List of people who should take the poll (some have already taken it)
people_to_poll = ['ali', 'ahmed', 'fahad', 'frank', 'hassan']

# Loop through the list and check if they have already taken the poll
for person in people_to_poll:
    if person in favorite_languages:
        print(f"Thank you, {person.title()}, for already taking the poll!")
    else:
        print(f"{person.title()}, please take our favorite programming language poll!")
