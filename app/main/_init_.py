from json.tool import main
from flask import Blueprint
main = Blueprint('maiin', __name__)
from . import views