pet_1 = {
    'animal': 'dog',
    'name': 'Buddy',
    'owner': 'Alice'
}

pet_2 = {
    'animal': 'cat',
    'name': 'Whiskers',
    'owner': 'Brian'
}

pet_3 = {
    'animal': 'parrot',
    'name': 'Polly',
    'owner': 'Catherine'
}

pet_4 = {
    'animal': 'rabbit',
    'name': 'Thumper',
    'owner': 'Diana'
}

pets = [pet_1, pet_2, pet_3, pet_4]

for pet in pets:
    print(f"{pet['owner']} has a {pet['animal']} named {pet['name']}.")
