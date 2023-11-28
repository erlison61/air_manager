from flask import Blueprint
from flask_restful import Api 

from resources.index import Index
from resources.estudante import EstudantesResource, EstudanteResource

blueprint = Blueprint('api', __name__)

api = Api(blueprint, prefix="/api")

api.add_resource(Index, '/')
api.add_resource(EstudanteResource, '/estudantes/<string:id>')
api.add_resource(EstudantesResource, '/estudantes')