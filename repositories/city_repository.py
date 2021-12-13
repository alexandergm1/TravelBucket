from db.run_sql import run_sql

from models.city import City
from models.country import Country
import repositories.country_repository as country_repository

def save(city):
    sql = "INSERT INTO cities (name, country_id, visited) VALUES (%s, %s, %s) RETURNING *"
    values = [city.name, city.country.id, city.visited]
    results = run_sql(sql, values)
    id = results[0]['id']
    city.id = id
    return city


def select_all():
    cities = []

    sql = "SELECT * FROM cities"
    results = run_sql(sql)

    for row in results:
        country = country_repository.select(row['country_id'])
        city = City(row['name'], country, row['visited'], row['id'])
        cities.append(city)
    return cities



def select(id):
    city = None
    sql = "SELECT * FROM cities WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results is not None:
        country = country_repository.select(results['country.id'])
        city = City(results['name'], country, results['visited'], results['id'])
    return city


def delete_all():
    sql = "DELETE FROM cities"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM cities WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(city):
    sql = "UPDATE cities SET (name, country_id, visited) VALUES (%s %s %s) WHERE id = %s"
    values = [city.name, city.country_id, city.visited, city.id]
    run_sql(sql, values)


def select_all_visited():
    cities = []
    sql = "SELECT * FROM cities WHERE visited = TRUE"
    results = run_sql(sql)

    for row in results:
        country = country_repository.select(results['country.id'])
        city = City(row['name'], country, row['visited'], row['id'])
        cities.append(city)
    return cities



def select_all_not_visited():
    cities = []
    sql = "SELECT * FROM cities WHERE visited = FALSE"
    results = run_sql(sql)

    for row in results:
        country = country_repository.select(results['country.id'])
        city = City(row['name'], country, row['visited'], row['id'])
        cities.append(city)
    return cities


def mark_visited(id):
    sql = "UPDATE cities SET visited = TRUE WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def mark_not_visited(id):
    sql = "UPDATE cities SET visited = FALSE WHERE id = %s"
    values = [id]
    run_sql(sql, values)