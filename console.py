import pdb
from models.city import City
from models.country import Country

import repositories.country_repository as country_repository
import repositories.city_repository as city_repository

country_repository.delete_all()

country1 = Country('Scotland', 'Europe')
country_repository.save(country1)

city1 = City('Inverness', country1)
city_repository.save(city1)

country2 = Country('Lithuania', 'Europe')
country_repository.save(country2)

city2 = City('Veiveriai', country2)
city_repository.save(city2)


# result = country_repository.select()
# print(result.__dict__)


pdb.set_trace()
