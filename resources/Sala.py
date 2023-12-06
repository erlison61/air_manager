from flask_restful import Resource, marshal_with, reqparse, marshal
from model.Sala import Sala, sala_fields
from helper.database import db

class SalaResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('numero_bloco', type=int, help="numero do bloco não existe")
        self.parser.add_argument('capacidade', type=int, help="capacidade invalida")
        self.parser.add_argument('coped', type=dict, help="capacidade invalida")
        self.parser.add_argument('tipo_sala', type=str, help="capacidade invalida")
        

    def get(self, id):
        sala = Sala.query.filter_by(id=id).first()
        if sala is not None:
            return marshal(Sala, sala_fields), 200
        
        return {'message': 'Aula não encontrada'}, 404

    @marshal_with(sala_fields)
    def put(self, id):
        args = self.parser.parse_args()

        sala = Sala.query.get(id)

        if not sala:
            return {'message': 'Sala not found'}, 404

        for field, value in args.items():
            if value is not None:
                setattr(sala, field, value)

        db.session.commit()

        return sala, 200

    def delete(self, id):
        sala = Sala.query.get(id)

        if not sala:
            return {'message': 'Sala not found'}, 404

        db.session.delete(sala)
        db.session.commit()

        return {'message': 'Sala deleted successfully'}, 200


class SalasResource(Resource):

    def __init__(self) -> None:
        super().__init__()
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('numero_bloco', type=int, help="numero do bloco não existe")
        self.parser.add_argument('capacidade', type=int, help="capacidade invalida")
        self.parser.add_argument('coped', type=dict, help="capacidade invalida")
        self.parser.add_argument('tipo_sala', type=str, help="capacidade invalida")

    
    def get(self):
        salas = Sala.query.all()
        if salas is not None:
            return marshal(salas, sala_fields), 200
        return {'message': 'as Aulas não foram encontradas'}, 404
        

    @marshal_with(sala_fields)
    def post(self):
        args = self.parser.parse_args()
        capacidade = args['capacidade']
        tipo_sala = args['tipo_sala']        
        coped = args['coped']
        numero_bloco = args['numero_bloco']

        sala = Sala(numero_bloco, capacidade, tipo_sala, coped)

        db.session.add(sala)
        db.session.commit()

        return sala
