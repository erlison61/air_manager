from flask_restful import Resource, reqparse, marshal

from helper.database import db
from model.TecnicoAdministrativo import TecnicoAdministrativo, tecnico_administrativo_fields

class TecnicoAdministrativoResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('nome', type=str, required=True, help="Nome é obrigatório.")
        self.parser.add_argument('telefone', type=str, required=True, help="Telefone é obrigatório.")
        self.parser.add_argument('cargo', type=str, required=True, help="Cargo é obrigatório.")
        self.parser.add_argument('email', type=str, required=True, help="Cargo é obrigatório.")

    def get(self, id):
        tecnico_administrativo = TecnicoAdministrativo.query.get(id)
        if tecnico_administrativo:
            return marshal(tecnico_administrativo, tecnico_administrativo_fields), 200
        return {'message': 'Técnico Administrativo não encontrado'},

    def put(self, id):
        args = self.parser.parse_args()
        tecnico_administrativo = TecnicoAdministrativo.query.get(id)

        if not tecnico_administrativo:
            return {'message': 'Técnico Administrativo não encontrado'}, 404

        tecnico_administrativo.nome = args['nome']
        tecnico_administrativo.telefone = args['telefone']
        tecnico_administrativo.cargo = args['cargo']
        tecnico_administrativo.email = args['email']

        db.session.commit()

        return marshal(tecnico_administrativo, tecnico_administrativo_fields), 200

    def delete(self, id):
        tecnico_administrativo = TecnicoAdministrativo.query.get(id)

        if not tecnico_administrativo:
            return {'message': 'Técnico Administrativo não encontrado'}, 404

        db.session.delete(tecnico_administrativo)
        db.session.commit()

        return {'message': 'Técnico Administrativo deletado com sucesso'}, 200


class TecnicosAdministrativosResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('nome', type=str, required=True, help="Nome é obrigatório.")
        self.parser.add_argument('telefone', type=str, required=True, help="Telefone é obrigatório.")
        self.parser.add_argument('cargo', type=str, required=True, help="Cargo é obrigatório.")
        self.parser.add_argument('email', type=str)

    def get(self):
        tecnico_administrativos = TecnicoAdministrativo.query.all()
        return marshal({'tecnico_administrativos': tecnico_administrativos}, tecnico_administrativo_fields), 200

    def post(self):
        args = self.parser.parse_args()

        novo_tecnico_administrativo = TecnicoAdministrativo(
            nome=args['nome'],
            telefone=args['telefone'],
            cargo=args['cargo'],
            email=args['email']
        )

        db.session.add(novo_tecnico_administrativo)
        db.session.commit()

        return marshal(novo_tecnico_administrativo, tecnico_administrativo_fields), 201