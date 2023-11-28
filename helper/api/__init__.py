from flask import Blueprint
from flask_restful import Api

from resources.index import Index

blueprint = Blueprint('api', __name__)

api = Api(blueprint, prefix="/api")

api.add_resource(Index, '/')
