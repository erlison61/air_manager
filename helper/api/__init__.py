from flask import Blueprint
from flask_restful import Api

from resources.Index import IndexResource

blueprint = Blueprint('api', __name__)

api = Api(blueprint, prefix="/api")

api.add_resource(IndexResource, '/')
