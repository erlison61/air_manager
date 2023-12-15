from flask import Blueprint
from flask_restful import Api

from resources.Aula import AulaResource, AulasResource
from resources.Index import IndexResource
from resources.Professor import ProfessorResource, ProfessoresResource
from resources.Sala import SalaResource, SalasResource
from resources.Coped import CopedResource
from resources.TecnicoAdministrativo import TecnicoAdministrativoResource, TecnicosAdministrativosResource
from resources.arCondicionado import ArCondicionadoResource, ArCondicionadosResource

blueprint = Blueprint('api', __name__)

api = Api(blueprint, prefix="/api")

api.add_resource(IndexResource, '/')
api.add_resource(ProfessorResource, '/professores/<int:id>')
api.add_resource(ProfessoresResource, '/professores')

api.add_resource(SalaResource, '/sala/<int:id>')
api.add_resource(SalasResource, '/sala')

api.add_resource(AulaResource, '/aulas/<int:id>')
api.add_resource(AulasResource, '/aulas')

api.add_resource(CopedResource, '/coped')

api.add_resource(TecnicoAdministrativoResource, '/tecnicoAdministrativo')
api.add_resource(TecnicosAdministrativosResource, '/tecnicoAdministrativo/<int:id>')

api.add_resource(ArCondicionadoResource, '/arcondicionado')
api.add_resource(ArCondicionadosResource, '/arcondicionado/<int:id>')

