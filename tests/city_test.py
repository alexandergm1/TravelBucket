import unittest
from models.city import City
from models.country import Country

class TestCity(unittest.TestCase):

    def setUp(self):
        country1 = Country('Scotland', 'Europe')
        self.city1 = City('Inverness', country1)


    def test_city_has_name(self):
        self.assertEqual('Inverness', self.city1.name)


    # def test_country_visited_starts_as_false(self):
    #     self.assertEqual(False, self.city1.visited)


    # def test_country_has_continent(self):
    #     self.assertEqual('Europe', self.city1.country)


    # def test_can_mark_visited(self):
    #     self.country1.mark_visited()
    #     self.assertEqual(True, self.city1.visited)