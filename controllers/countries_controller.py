from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.city import City
from models.country import Country
import repositories.country_repository as country_repository
import repositories.city_repository as city_repository

countries_blueprint = Blueprint("countries", __name__)

@countries_blueprint.route("/home")
def home():
    return render_template("index.html")


@countries_blueprint.route("/countries")
def countries():
    return render_template("countries/index.html")


@countries_blueprint.route("/countries/visited")
def countries_visited():
    countries = country_repository.select_all_visited()
    return render_template("countries/visited.html", countries = countries)

@countries_blueprint.route("/countries/notvisited")
def countries_not_visited():
    countries = country_repository.select_all_not_visited()
    return render_template("countries/not_visited.html", countries = countries)


@countries_blueprint.route("/countries/notvisited/<id>/markvisited", methods = ['POST'])
def countries_mark_visited(id):
    country_repository.mark_visited(id)
    return redirect('/countries/notvisited')


@countries_blueprint.route("/countries/visited/<id>/marknotvisited", methods = ['POST'])
def countries_mark_not_visited(id):
    country_repository.mark_not_visited(id)
    return redirect('/countries/visited')


@countries_blueprint.route("/countries/visited/<id>/deletevisited", methods=['POST'])
def delete_visited_country(id):
    country_repository.delete(id)
    return redirect('/countries/visited')


@countries_blueprint.route("/countries/notvisited/<id>/deletenotvisited", methods=['POST'])
def delete_not_visited_country(id):
    country_repository.delete(id)
    return redirect('/countries/notvisited')