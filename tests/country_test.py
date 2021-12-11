import unittest
from models.country import Country

class TestCountry(unittest.TestCase):

    def setUp(self):
        self.country1 = Country('Norway', 'Europe', False)


    def test_country_has_name(self):
        self.assertEqual('Norway', self.country1.name)