favorite_places = {
    'Ali': ['Paris', 'Tokyo', 'New York'],
    'Saad': ['London', 'Berlin'],
    'Hashim': ['San Francisco', 'Austin', 'Miami']
}

for person, places in favorite_places.items():
    print(f"{person}'s favorite places are:")
    for place in places:
        print(f"- {place}")
    print()  
