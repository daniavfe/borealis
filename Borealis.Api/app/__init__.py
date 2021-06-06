from flask import Flask, jsonify
from flask_restful import Api
from app.extension import db
from app.api.endpoints import *
from .extension import marshmallow, migrate


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config/default.py")
    app.config.from_envvar('APP_CONFIG_FILE')
    #app.config.from_pyfile("config/development.py")

    # app.config.from_object(settings_module)
    # Inicializa las extensiones
    db.init_app(app)
    marshmallow.init_app(app)
    migrate.init_app(app, db)

    # Captura todos los errores 404
    Api(app, catch_all_404s=True)
    # Deshabilita el modo estricto de acabado de una URL con /
    app.url_map.strict_slashes = False
    
    #Api Blueprints
    app.register_blueprint(measurement_blueprint)
    app.register_blueprint(magnitude_blueprint)
    app.register_blueprint(station_blueprint)
    app.register_blueprint(density_blueprint)
    app.register_blueprint(holiday_blueprint)
    app.register_blueprint(event_blueprint)
    app.register_blueprint(report_blueprint)
    app.register_blueprint(timeline_blueprint)
    app.register_blueprint(town_blueprint)
    return app
