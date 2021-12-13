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

china = Country('China', 'Asia')
country_repository.save(china)

taiwan = Country('Taiwan', 'Asia')
country_repository.save(taiwan)

india = Country('India', 'Asia')
country_repository.save(india)

zimbabwe = Country('Zimbabwe', 'Africa')
country_repository.save(zimbabwe)

ethiopia = Country('Ethiopia', 'Africa')
country_repository.save(ethiopia)

nigeria = Country('Nigeria', 'Africa')
country_repository.save(nigeria)

united_states = Country('United States of America', 'North America')
country_repository.save(united_states)

england_city1 = City('London', england)
city_repository.save(england_city1)

wales_city1 = City('Cardiff', wales)
city_repository.save(wales_city1)

ireland_city1 = City('Dublin', ireland)
city_repository.save(ireland_city1)

northern_ireland_city1 = City('Belfast', northern_ireland)
city_repository.save(northern_ireland_city1)

norway_city1 = City('Oslo', norway)
city_repository.save(norway_city1)

sweden_city1 = City('Stockholm', sweden)
city_repository.save(sweden_city1)

france_city1 = City('Paris', france)
city_repository.save(france_city1)

germany_city1 = City('Berlin', germany)
city_repository.save(germany_city1)

russia_city1 = City('Moscow', russia)
city_repository.save(russia_city1)

zimbabwe_city1 = City('Harare', zimbabwe)
city_repository.save(zimbabwe_city1)

ethiopia_city1 = City('Addis Ababa', ethiopia)
city_repository.save(ethiopia_city1)

china_city1 = City('Beijing', china)
city_repository.save(china_city1)

india_city1 = City('Delhi', india)
city_repository.save(india_city1)

united_states_city1 = City('New York', united_states)
city_repository.save(united_states_city1)

nigeria_city1 = City('Lagos', nigeria)
city_repository.save(nigeria_city1)

taiwan_city1 = City('Taipei', taiwan)
city_repository.save(taiwan_city1)



pdb.set_trace()
