import pdb
from models.city import City
from models.country import Country

import repositories.country_repository as country_repository

country_repository.delete_all()

country1 = Country('Scotland', 'Europe', False)
country_repository.save(country1)




# result = country_repository.select()
# print(result.__dict__)


pdb.set_trace()
