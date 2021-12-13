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