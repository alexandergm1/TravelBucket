import pdb
from models.city import City
from models.country import Country

import repositories.country_repository as country_repository
import repositories.city_repository as city_repository

country_repository.delete_all()

scotland = Country('Scotland', 'Europe')
country_repository.save(scotland)

scotland_city1 = City('Inverness', scotland)
city_repository.save(scotland_city1)

lithuania = Country('Lithuania', 'Europe')
country_repository.save(lithuania)

lithuania_city1 = City('Veiveriai', lithuania)
city_repository.save(lithuania_city1)

spain = Country('Spain', 'Europe')
country_repository.save(spain)

germany = Country('Germany', 'Europe')
country_repository.save(germany)

france = Country('France', 'Europe')
country_repository.save(france)

northern_ireland = Country('Northern Ireland', 'Europe')
country_repository.save(northern_ireland)

ireland = Country('Ireland', 'Europe')
country_repository.save(ireland)

wales = Country('Wales', 'Europe')
country_repository.save(wales)

england = Country('England', 'Europe')
country_repository.save(england)

sweden = Country('Sweden', 'Europe')
country_repository.save(sweden)

russia = Country('Russia', 'Europe')
country_repository.save(russia)

norway = Country('Norway', 'Europe')
country_repository.save(norway)

china = Country('China', 'Europe')
country_repository.save(china)

taiwan = Country('Taiwan', 'Europe')
country_repository.save(taiwan)

india = Country('India', 'Europe')
country_repository.save(india)

zimbabwe = Country('Zimbabwe', 'Europe')
country_repository.save(zimbabwe)









pdb.set_trace()
