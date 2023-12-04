from flask_restful import Resource, marshal_with

from model.Pessoa import Pessoa, pessoa_fields

class PessoasResource(Resource):
    @marshal_with(pessoa_fields)
    def get(self):
        pessoas  = Pessoa.query.all()
        return pessoas, 200

