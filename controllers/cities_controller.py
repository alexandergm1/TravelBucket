from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.city import City
from models.country import Country
import repositories.country_repository as country_repository
import repositories.city_repository as city_repository

cities_blueprint = Blueprint("cities", __name__)



@cities_blueprint.route("/cities")
def cities():
    return render_template("cities/index.html")


@cities_blueprint.route("/cities/visited")
def cities_visited():
    cities = city_repository.select_all_visited()
    return render_template("cities/visited.html", cities = cities)

@cities_blueprint.route("/cities/notvisited")
def cities_not_visited():
    cities = city_repository.select_all_not_visited()
    return render_template("cities/not_visited.html", cities = cities)


@cities_blueprint.route("/cities/notvisited/<id>/markvisited", methods = ['POST'])
def cities_mark_visited(id):
    city_repository.mark_visited(id)
    return redirect('/cities/notvisited')


@cities_blueprint.route("/cities/visited/<id>/marknotvisited", methods = ['POST'])
def cities_mark_not_visited(id):
    city_repository.mark_not_visited(id)
    return redirect('/cities/visited')