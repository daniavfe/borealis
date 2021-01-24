from flask import Flask, jsonify
from flask_restful import Api
from app.extension import db
from app.api.endpoints import measurement_blueprint, station_blueprint, density_blueprint
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
    # Registra los blueprints
    app.register_blueprint(measurement_blueprint)
    app.register_blueprint(station_blueprint)
    app.register_blueprint(density_blueprint)
    return app
