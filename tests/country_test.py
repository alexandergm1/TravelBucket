import unittest
from models.country import Country

class TestCountry(unittest.TestCase):

    def setUp(self):
        self.country1 = Country('Norway', 'Europe')


    def test_country_has_name(self):
        self.assertEqual('Norway', self.country1.name)


    def test_country_visited_starts_as_false(self):
        self.assertEqual(False, self.country1.visited)


    def test_country_has_continent(self):
        self.assertEqual('Europe', self.country1.continent)