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