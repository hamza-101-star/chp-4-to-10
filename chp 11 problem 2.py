# city_functions.py


def city_country(city, country, population=None):
    """Return a formatted string with optional population."""
    if population:
        return f"{city.title()}, {country.title()} – population {population}"
    else:
        return f"{city.title()}, {country.title()}"


# test_cities.py

import unittest
from city_functions import city_country

class CityCountryTestCase(unittest.TestCase):
    """Tests for the city_country() function."""

    def test_city_country(self):
        """Does city_country() return 'Santiago, Chile' properly?"""
        formatted = city_country('santiago', 'chile')
        self.assertEqual(formatted, 'Santiago, Chile')

    def test_city_country_population(self):
        """Does city_country() return 'Santiago, Chile – population 5000000' properly?"""
        formatted = city_country('santiago', 'chile', population=5000000)
        self.assertEqual(formatted, 'Santiago, Chile – population 5000000')

if __name__ == '__main__':
    unittest.main()
