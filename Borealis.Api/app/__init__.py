from flask import Flask, jsonify
from flask_restful import Api
from app.extension import db
from app.api.endpoints import *
from .extension import marshmallow, migrate


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("configuration/development.py")
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
    app.register_blueprint(pollution_blueprint)
    app.register_blueprint(density_blueprint)
    app.register_blueprint(holiday_blueprint)
    app.register_blueprint(weather_blueprint)
    app.register_blueprint(traffic_blueprint)
    return app
