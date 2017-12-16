from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_profile import Profiler

from aquila.config import config

bootstrap = Bootstrap()
db = SQLAlchemy()
profiler = Profiler()

def create_app(config_name):
	app = Flask(__name__)
	app.config.from_object(config[config_name])

	# Register our blueprints
	from .default import default as default_blueprint
	app.register_blueprint(default_blueprint)

	# Rest APIs

    # Initialize any extensions we are using
	bootstrap.init_app(app)
	db.init_app(app)

	# Flask-Profile is only actived under debug mode
	#app.debug = True
	#profiler.init_app(app)

	return app