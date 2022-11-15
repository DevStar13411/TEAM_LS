from flask import Flask
from src.Controller import main_views
from flask_cors import CORS



def create_app():
    app = Flask(__name__)
    app.config['JSON_AS_ASCII'] = False
    app.register_blueprint(main_views.main_page)
    CORS(app, resources={r'*':{'origins':'http://localhost:8080'}})
    return app
