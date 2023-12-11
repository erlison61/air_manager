from flask_restful import Resource, reqparse, marshal

from model.Coped import Coped, coped_fields
from helper.database import db

class CopedResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('tecnicoAdministrativo', type=dict, help="Técnico administrativo é obrigatório.")

    def get(self, id):
        coped = Coped.query.get(id)
        if coped:
            return marshal(coped, coped_fields), 200
        
        return {'message': 'Coped não encontrada'}, 404

    def put(self, id):
        args = self.parser.parse_args()
        coped = Coped.query.get(id)

        if not coped:
            return {'message': 'Coped não encontrada'}, 404

        if args['tecnicoAdministrativo']:
            coped.tecnicoAdministrativo = args['tecnicoAdministrativo']

        db.session.commit()
        return marshal(coped, coped_fields), 200

    def delete(self, id):
        coped = Coped.query.get(id)

        if not coped:
            return {'message': 'Coped não encontrada'}, 404

        db.session.delete(coped)
        db.session.commit()

        return {'message': 'Coped deletada com sucesso'}, 200
