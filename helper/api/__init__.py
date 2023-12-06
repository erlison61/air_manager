from flask import Blueprint
from flask_restful import Api

from resources.Aula import AulaResource, AulasResource
from resources.Index import IndexResource
from resources.Professor import ProfessorResource
from resources.Sala import SalaResource

blueprint = Blueprint('api', __name__)

api = Api(blueprint, prefix="/api")

api.add_resource(IndexResource, '/')
api.add_resource(ProfessorResource, '/professores/<int:id>', endpoint='professor_by_id')
api.add_resource(ProfessorResource, '/professores', endpoint='professors')

api.add_resource(SalaResource, '/sala/<int:id>', endpoint='sala_by_id')
api.add_resource(SalaResource, '/sala', endpoint='salas')

api.add_resource(AulaResource, '/aulas/<int:id>', endpoint='aula_by_id')
api.add_resource(AulasResource, '/aulas', endpoint='aulas')
