from web.app.endpoints.auto_order import AutoOrder
from web.app.endpoints.order import Order
from web.app.view_page import app
from web.restapi import api
from web import settings

from flask import Blueprint

def configure_app(flask_app):
    flask_app.config['SERVER_NAME'] = settings.FLASK_SERVER_NAME
    # flask_app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
    # flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP


def initialize_app(flask_app):
    configure_app(flask_app)

    blueprint = Blueprint('api', __name__,)
    api.init_app(blueprint)
    api.add_namespace(Order)
    api.add_namespace(AutoOrder)
    flask_app.register_blueprint(blueprint)

    # db.init_app(flask_app)

if __name__ == '__main__':
    initialize_app(app)
    app.run(debug=settings.FLASK_DEBUG)