from flask_restful import Resource, reqparse, marshal_with
from model.Aula import Aula, aula_fields
from helper.database import db
from datetime import datetime


class AulaResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('inicio', type=str, help="Formato inválido para o campo 'inicio'. Use o formato ISO8601.")
        self.parser.add_argument('fim', type=str, help="Formato inválido para o campo 'fim'. Use o formato ISO8601.")
        self.parser.add_argument('professor_id', type=str, help="ID do professor é obrigatório.")
        self.parser.add_argument('sala_id', type=int, help="ID da sala é obrigatório.")

    @marshal_with(aula_fields)
    def get(self, id):
        aula = Aula.query.filter_by(id=id).first()
        if aula:
            return aula, 200
        else:
            return {'message': 'Aula não encontrada'}, 404

    def post(self):
        args = self.parser.parse_args()
        
        inicio = datetime.fromisoformat(args['inicio'])
        fim = datetime.fromisoformat(args['fim'])
        professor_id = args['professor_id']
        sala_id = args['sala_id']

        nova_aula = Aula(inicio=inicio, fim=fim, professor_id=professor_id, sala_id=sala_id)
        db.session.add(nova_aula)
        db.session.commit()

        return nova_aula, 201

    def put(self, id):
        args = self.parser.parse_args()

        aula = Aula.query.filter_by(id=id).first()

        if not aula:
            return {'message': 'Aula não encontrada'}, 404

        if args['inicio']:
            aula.inicio = datetime.fromisoformat(args['inicio'])
        if args['fim']:
            aula.fim = datetime.fromisoformat(args['fim'])
        if args['professor_id']:
            aula.professor_id = args['professor_id']
        if args['sala_id']:
            aula.sala_id = args['sala_id']

        db.session.commit()

        return aula, 200

    def delete(self, id):
        aula = Aula.query.filter_by(id=id).first()

        if not aula:
            return {'message': 'Aula não encontrada'}, 404

        db.session.delete(aula)
        db.session.commit()

        return {'message': 'Aula deletada com sucesso'}, 200
