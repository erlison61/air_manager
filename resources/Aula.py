from flask_restful import Resource, reqparse, marshal, marshal_with
from datetime import datetime

from model.Aula import Aula, aula_fields
from model.Sala import Sala
from model.Professor import Professor, professor_fields
from helper.database import db


class AulaResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument(
            'inicio', type=str, help="Formato inválido para o campo 'inicio'. Use o formato ISO8601.")
        self.parser.add_argument(
            'fim', type=str, help="Formato inválido para o campo 'fim'. Use o formato ISO8601.")
        self.parser.add_argument(
            'professor', type=dict, help="Professor é obrigatório.")
        self.parser.add_argument(
            'sala', type=dict, help="Sala é obrigatório.")

    def get(self, id):
        aula = Aula.query.filter_by(id=id).first()
        if aula is not None:
            return marshal(aula, aula_fields), 200
        
        return {'message': 'Aula não encontrada'}, 404

    def put(self, id):
        args = self.parser.parse_args()

        aula = Aula.query.filter_by(id=id).first()

        if not aula:
            return {'message': 'Aula não encontrada'}, 404

        if args['inicio']:
            aula.inicio = datetime.fromisoformat(args['inicio'])
        if args['fim']:
            aula.fim = datetime.fromisoformat(args['fim'])
        if args['professor']:
            aula.professor = args['professor']
        if args['sala']:
            aula.sala = args['sala']

        db.session.commit()

        return marshal(aula, aula_fields), 200

    def delete(self, id):
        aula = Aula.query.filter_by(id=id).first()

        if not aula:
            return {'message': 'Aula não encontrada'}, 404

        db.session.delete(aula)
        db.session.commit()

        return {'message': 'Aula deletada com sucesso'}, 200


class AulasResource(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument(
            'inicio', type=str, help="Formato inválido para o campo 'inicio'. Use o formato ISO8601.")
        self.parser.add_argument(
            'fim', type=str, help="Formato inválido para o campo 'fim'. Use o formato ISO8601.")
        self.parser.add_argument(
            'professor', type=dict, help="Professor é obrigatório.")
        self.parser.add_argument(
            'sala', type=dict, help="Sala é obrigatório.")

    def post(self):
        args = self.parser.parse_args()

        # {
        #     "inicio": "2023-12-04 14:11:00",
        #     "fim": "2023-12-04 14:11:00",
        #     "professor": {"id": 1, "id_professor": 1},
        #     "sala": {"id":1}
        # }
        inicio = datetime.fromisoformat(args['inicio'])
        print(inicio)
        fim = datetime.fromisoformat(args['fim'])
        print(fim)
        id_professor = args['professor']['id_professor']
        id_sala = args['sala']['id']

        professor = Professor.query.filter_by(
            id_professor=id_professor).first()
        sala = Sala.query.filter_by(id=id_sala).first()

        aula = Aula(inicio, fim, professor, sala)
        db.session.add(aula)
        db.session.commit()

        return marshal(aula, aula_fields), 201
