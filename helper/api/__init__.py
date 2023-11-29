from flask import Blueprint
from flask_restful import Api
from resources.Professor import ProfessorResource
from resources.Aula import AulaResource

from resources.Index import IndexResource

blueprint = Blueprint('api', __name__)

api = Api(blueprint, prefix="/api")

api.add_resource(IndexResource, '/')
api.add_resource(ProfessorResource, '/professores/<int:id>')
api.add_resource(AulaResource, '/aulas/<int:id>')
