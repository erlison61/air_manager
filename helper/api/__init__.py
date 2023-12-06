from flask import Blueprint
from flask_restful import Api

from resources.Aula import AulaResource, AulasResource
from resources.Index import IndexResource
from resources.Professor import ProfessorResource, ProfessoresResource
from resources.Sala import SalaResource, SalasResource

blueprint = Blueprint('api', __name__)

api = Api(blueprint, prefix="/api")

api.add_resource(IndexResource, '/')
api.add_resource(ProfessorResource, '/professores/<int:id>')
api.add_resource(ProfessoresResource, '/professores')

api.add_resource(SalaResource, '/sala/<int:id>')
api.add_resource(SalasResource, '/sala')

api.add_resource(AulaResource, '/aulas/<int:id>')
api.add_resource(AulasResource, '/aulas')
