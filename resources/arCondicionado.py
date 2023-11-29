from flask_restful import Resource, marshal_with, reqparse
from model.ArCondicionado import ArCondicionado, ar_condicionado_fields
from helper.database import db

class ArCondicionadoResource(Resource):

    @marshal_with(ar_condicionado_fields)
    def get(self, numero_serie):
        ar_condicionado = ArCondicionado.query.filter_by(numero_serie=numero_serie).first()
        return ar_condicionado, 200

    def __repr__(self) -> str:
        return "<ArCondicionadoResource>"

class ArCondicionadosResource(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('status', type=bool, required=True, help='Status é requerido')
        self.parser.add_argument('marca', type=str, required=True, help='Marca é requerida')
        self.parser.add_argument('id_sala', type=int, required=True, help='Sala id é requerido')
        self.parser.add_argument('id_coped', type=int, required=True, help='Coped id é requerido')
        self.parser.add_argument('modelo', type=str, required=True, help='Modelo é requerido')

   

    @marshal_with(ar_condicionado_fields)
    def get(self):
        ar_condicionados = ArCondicionado.query.all()
        return ar_condicionados, 200
    
    @marshal_with(ar_condicionado_fields)
    def post(self):
        args = self.parser.parse_args()

        status = args['status']
        marca = args['marca']
        id_sala = args['id_sala']
        id_coped = args['id_coped']
        modelo = args['modelo']

        ar_condicionado = ArCondicionado(
            status=status,
            marca=marca,
            id_sala=id_sala,
            id_coped=id_coped,
            modelo=modelo
        )

        db.session.add(ar_condicionado)
        db.session.commit()

        return ar_condicionado, 201

    def __repr__(self) -> str:
        return "<ArCondicionadosResource>"
