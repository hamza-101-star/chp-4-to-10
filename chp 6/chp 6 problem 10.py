cities = {
    'Paris': {
        'country': 'France',
        'population': 2148000,
        'fact': 'Paris is known as the "City of Light" because it was one of the first cities in the world to have street lighting.'
    },
    'Tokyo': {
        'country': 'Japan',
        'population': 13929286,
        'fact': 'Tokyo is the world’s most populous city and a major international economic hub.'
    },
    'New York': {
        'country': 'USA',
        'population': 8419600,
        'fact': 'New York City is known for its iconic landmarks like the Statue of Liberty and Times Square.'
    }
}

for city, info in cities.items():
    print(f"City: {city}")
    print(f"  Country: {info['country']}")
    print(f"  Population: {info['population']}")
    print(f"  Fact: {info['fact']}\n")
