from flask import Flask
from flaskapp.src.Controller import main_views


def create_app():
    app = Flask(__name__)

    app.register_blueprint(main_views.main_page)

    return app
