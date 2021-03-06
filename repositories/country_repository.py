from db.run_sql import run_sql
from models.city import City
from models.country import Country


def save(country):
    sql = "INSERT INTO countries (name, continent, visited) VALUES (%s, %s, %s) RETURNING id"
    values = [country.name, country.continent, country.visited]
    results = run_sql(sql, values)
    country.id = results[0]['id']
    return country


def select_all():
    countries = []

    sql = "SELECT * FROM countries"
    results = run_sql(sql)
    for row in results:
        country = Country(row['name'], row['continent'], row['visited'], row['id'])
        countries.append(country)
    return countries


def select(id):
    sql = "SELECT * FROM countries WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)[0]

    if results is not None:
        country = Country(results['name'], results['continent'], results['visited'], results['id'])
    return country


def delete_all():
    sql = "DELETE FROM countries"
    run_sql(sql)



def delete(id):
    sql = "DELETE FROM countries WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)


def update(country):
    sql = "UPDATE countries SET (name, continent, visited) = (%s, %s, %s) WHERE id = %s"
    values = [country.name, country.continent, country.visited, country.id]
    run_sql(sql, values)


def select_all_visited():
    countries = []
    sql = "SELECT * FROM countries WHERE visited = TRUE"
    results = run_sql(sql)

    for row in results:
        country = Country(row['name'], row['continent'], row['visited'], row['id'])
        countries.append(country)
    return countries



def select_all_not_visited():
    countries = []
    sql = "SELECT * FROM countries WHERE visited = FALSE"
    results = run_sql(sql)

    for row in results:
        country = Country(row['name'], row['continent'], row['visited'], row['id'])
        countries.append(country)
    return countries


def mark_visited(id):
    sql = "UPDATE countries SET visited = TRUE WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def mark_not_visited(id):
    sql = "UPDATE countries SET visited = FALSE WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def cities(country):
    cities = []

    sql = "SELECT * FROM cities WHERE country_id = %s"
    values = [country.id]
    results = run_sql(sql, values)

    for row in results:
        city = City(row['name'], row['visited'], row['id'])
        cities.append(city)
    return cities