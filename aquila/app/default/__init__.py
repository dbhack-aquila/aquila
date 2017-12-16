from flask import Blueprint
from aquila.config import Config

default = Blueprint('cast', __name__, static_folder=Config.STATIC_FOLDER, static_url_path='')
from . import routes
from . import point_of_interest_api
