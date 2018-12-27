import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'. """

    def test_first_last_name(self):
        """Do names like 'Janis Jolpin' work?"""
        formatted_name = get_formatted_name('janis', 'jolpin')
        self.assertEqual(formatted_name, 'Janis Jolpin')

    def test_first_last_middle_name(self):
        """Do names like 'Wolfgang Amadeus Mozart' work?"""
        formatted_name = get_formatted_name(
            'wolfgang', 'mozart', 'amadeus'
        )
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')
unittest.main()