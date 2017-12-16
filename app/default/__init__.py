from flask import Blueprint
from config import Config

default = Blueprint('cast', __name__, static_folder=Config.STATIC_FOLDER, static_url_path='')
from . import routes
from . import rest_train
rest_train.init()
print("Data loaded!")
