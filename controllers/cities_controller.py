from itertools import count
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


@cities_blueprint.route("/cities/visited/<id>/deletevisited", methods=['POST'])
def delete_visited_city(id):
    city_repository.delete(id)
    return redirect('/cities/visited')


@cities_blueprint.route("/cities/notvisited/<id>/deletenotvisited", methods=['POST'])
def delete_not_visited_city(id):
    city_repository.delete(id)
    return redirect('/cities/notvisited')


@cities_blueprint.route("/cities/<id>")
def show_visited_city(id):
    city = city_repository.select(id)
    return render_template('/cities/show.html', city = city)



@cities_blueprint.route("/cities/<id>")
def show_not_visited_city(id):
    city = city_repository.select(id)
    return render_template('/cities/show.html', city = city)


@cities_blueprint.route("/cities/<id>/edit")
def edit_page(id):
    countries = country_repository.select_all()
    city = city_repository.select(id)
    return render_template('/cities/edit.html', city = city, countries = countries)



@cities_blueprint.route("/cities/<id>/editcity", methods=['POST'])
def edit_city(id):
    name = request.form['name']
    country  = country_repository.select(request.form['country_id'])
    updated_city = City(name, country, id)
    city_repository.update(updated_city)
    return redirect('/cities')
