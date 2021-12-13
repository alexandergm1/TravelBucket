from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.city import City
from models.country import Country
import repositories.country_repository as country_repository
import repositories.city_repository as city_repository

newitems_blueprint = Blueprint("newitems", __name__)


@newitems_blueprint.route("/newitems")
def newitems():
    return render_template("newitems/index.html")


@newitems_blueprint.route("/newitems/countries")
def newitems__cities():
    return render_template("newitems/countries.html")

@newitems_blueprint.route("/newitems/cities")
def newitems__cities():
    return render_template("newitems/cities.html")



@newitems_blueprint.route("/newitems/countries", methods=['POST'])
def create_country():
    name = request.form['name']
    continent = request.form['continent']
    new_country = Country(name, continent)
    country_repository.save(new_country)
    return redirect("newitems/countries.html")


@newitems_blueprint.route("/newitems/cities", methods=['POST'])
def create_city():
    name = request.form['name']
    country  = country_repository.select(request.form['author_id'])
    new_city = City(name, country)
    city_repository.save(new_city)
    return redirect("newitems/cities.html")