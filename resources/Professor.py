from flask_restful import Resource, marshal_with, reqparse, marshal

from model.Professor import Professor, professor_fields
from helper.database import db


class ProfessorResource(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument(
            'nome', type=str, help="problema com a conversão do nome")
        self.parser.add_argument(
            'sobrenome', type=str, help="problema com a conversão do sobrenome")
        self.parser.add_argument(
            'email', type=str, help="problema com a conversão do email")
        self.parser.add_argument('telefone', type=str,
                                 help="problema com a conversão do telefone")
        self.parser.add_argument(
            'numero_matricula', type=str, help="problema com a conversão da matrícula")
        self.parser.add_argument(
            'titulacao', type=str, help="problema com a conversão da titulação")

    def get(self, id):
        professor = Professor.query.filter_by(id=id).first()
        if professor is not None:
            return marshal(professor, professor_fields), 200
        
        return {'message': 'Professor not found'}, 404

    def put(self, id):
        args = self.parser.parse_args()

        professor = Professor.query.filter_by(id=id).first()

        if not professor:
            return {'message': 'Professor not found'}, 404

        if args['nome']:
            professor.nome = args['nome']
        if args['sobrenome']:
            professor.sobrenome = args['sobrenome']

        db.session.commit()

        return marshal(professor, professor_fields), 200

    def delete(self, id):
        professor = Professor.query.filter_by(id=id).first()

        if not professor:
            return {'message': 'Professor not found'}, 404

        db.session.delete(professor)
        db.session.commit()

        return {'message': 'Professor deleted successfully'}, 200


class ProfessoresResource(Resource):

    def __init__(self) -> None:
        super().__init__()
        self.parser = reqparse.RequestParser()
        self.parser.add_argument(
            'nome', type=str, help="problema com a conversão do nome")
        self.parser.add_argument(
            'sobrenome', type=str, help="problema com a conversão do sobrenome")
        self.parser.add_argument(
            'email', type=str, help="problema com a conversão do email")
        self.parser.add_argument('telefone', type=str,
                                 help="problema com a conversão do telefone")
        self.parser.add_argument(
            'numero_matricula', type=str, help="problema com a conversão da matricula")
        self.parser.add_argument(
            'titulacao', type=str, help="problema com a conversão da titulacao")

    @marshal_with(professor_fields)
    def get(self):
        professores = Professor.query.all()
        return professores, 200

    @marshal_with(professor_fields)
    def post(self):
        args = self.parser.parse_args()
        nome = args['nome']
        sobrenome = args['sobrenome']
        email = args['email']
        telefone = args['telefone']
        numero_matricula = args['numero_matricula']
        titulacao = args['titulacao']

        professor = Professor(nome, sobrenome, email,telefone,numero_matricula,titulacao)

        db.session.add(professor)
        db.session.commit()

        return professor
