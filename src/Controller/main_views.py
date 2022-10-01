import pymongo as pymongo
from flask import Blueprint

main_page = Blueprint("main", __name__, url_prefix='/')


@main_page.route('/')
def hello_world():
    return 'Hello World!'
