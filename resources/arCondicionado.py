from flask_restful import Resource, marshal_with, reqparse, marshal
from model.arCondicionado import ArCondicionado, ar_condicionado_fields
from helper.database import db

class ArCondicionadoResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('status', type=bool, required=True, help='Status é requerido')
        self.parser.add_argument('marca', type=str, required=True, help='Marca é requerida')
        self.parser.add_argument('modelo', type=str, required=True, help='Modelo é requerido')
        self.parser.add_argument('numero_serie', type=int, required=True, help='Numero de serie é requerido')
        self.parser.add_argument('potencia', type=int, required=True, help='potencia é requerido')
        self.parser.add_argument('numero_serie', type=int, required=True, help='Numero de serie é requerido')
        self.parser.add_argument('consumo', type=int, required=True, help='consumo é requerido')
        self.parser.add_argument('voltagem', type=float, required=True, help='voltagem é requerido')

    def get(self):
        ar_condicionados = ArCondicionado.query.all()
        if ar_condicionados is not None:
            return marshal(ar_condicionados, ar_condicionado_fields), 200
        return {'message': 'erro ao buscar arcondicionado'}, 404
    
    def put(self, id):
        args = self.parser.parse_args()

        arCondicionado = ArCondicionado.query.filter_by(id=id).first()

        if not arCondicionado:
            return {'message': 'Aula não encontrada'}, 404
       
        arCondicionado.fabricante = args['fabricante']
        arCondicionado.marca = args['marca']
        arCondicionado.modelo = args['modelo']
        arCondicionado.numero_serie = args['numero_serie']
        arCondicionado.potencia = args['potencia']
        arCondicionado.consumo = args['consumo']
        arCondicionado.voltagem = args['voltagem']
        arCondicionado.status = args['status']

        db.session.commit()

        return marshal(arCondicionado, ar_condicionado_fields), 200

    def delete(self, id):
        arCondicionado = ArCondicionado.query.filter_by(id=id).first()

        if not arCondicionado:
            return {'message': 'Aula não encontrada'}, 404

        db.session.delete(arCondicionado)
        db.session.commit()

        return {'message': 'Aula deletada com sucesso'}, 200

    def __repr__(self) -> str:
        return "<ArCondicionadoResource>"

class ArCondicionadosResource(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('status', type=bool, required=True, help='Status é requerido')
        self.parser.add_argument('marca', type=str, required=True, help='Marca é requerida')
        self.parser.add_argument('modelo', type=str, required=True, help='Modelo é requerido')
        self.parser.add_argument('numero_serie', type=int, required=True, help='Numero de serie é requerido')
        self.parser.add_argument('potencia', type=int, required=True, help='potencia é requerido')
        self.parser.add_argument('numero_serie', type=int, required=True, help='Numero de serie é requerido')
        self.parser.add_argument('consumo', type=int, required=True, help='consumo é requerido')
        self.parser.add_argument('voltagem', type=float, required=True, help='voltagem é requerido')



    def get(self, id):
        ar_condicionado = ArCondicionado.query.filter_by(id=id).first()
        if ar_condicionado is not None:
            return marshal(ar_condicionado, ar_condicionado_fields), 200
   
        return {'message': 'erro ao buscar arcondicionado'}, 404
    


    @marshal_with(ar_condicionado_fields)
    def post(self):
        args = self.parser.parse_args()

        status = args['status']
        marca = args['marca']
        fabricante = args['fabricante']
        modelo = args['modelo']
        numero_serie = args['numero_serie']
        potencia = args['potencia']
        consumo = args['consumo']
        voltagem = args['voltagem']

        ar_condicionado = ArCondicionado(
            fabricante, 
            marca, 
            modelo, 
            numero_serie, 
            potencia, 
            consumo, 
            voltagem, 
            status
        )

        db.session.add(ar_condicionado)
        db.session.commit()

        return ar_condicionado, 201

    def __repr__(self) -> str:
        return "<ArCondicionadosResource>"
