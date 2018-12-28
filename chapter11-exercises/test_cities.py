import unittest
from city_functions import city_functions as cf

class CitiesTestCase(unittest.TestCase):
    def test_city_country(self):
        city_country_string = cf('santiago', 'chile', 500000)
        self.assertEqual(city_country_string, 'Santiago, Chile - population 500000')

unittest.main()