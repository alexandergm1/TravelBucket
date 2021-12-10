import pdb
from models.city import City
from models.country import Country

import repositories.country_repository as country_repository


country1 = Country('Scotland', 'Europe', False)
country_repository.save(country1)



pdb.set_trace()
