from flask_restful import fields
from helper.database import db


ar_condicionado_fields = {
    'id': fields.Integer,
    'fabricante': fields.String,
    'marca': fields.String,
    'modelo': fields.String,
    'numero_serie': fields.String,
    'potencia': fields.Integer,
    'consumo': fields.Float,
    'voltagem': fields.Integer,
    'status': fields.Boolean,

}


class ArCondicionado(db.Model):
    __tablename__ = "tb_arcondicionado"

    id = db.Column(db.Integer, primary_key=True)
    fabricante = db.Column(db.String(255), nullable=False)
    marca = db.Column(db.String(255), nullable=False)
    modelo = db.Column(db.String(255), nullable=False)
    numero_serie = db.Column(db.String(255), nullable=False)
    potencia = db.Column(db.Integer, nullable=False)
    consumo = db.Column(db.Float, nullable=False)
    voltagem = db.Column(db.Integer, nullable=False)

    status = db.Column(db.Boolean, nullable=False)

    # TODO Verificar construtor
    def __init__(self, numero_serie: int, status: bool, marca: str, modelo: str):
        self.numero_serie = numero_serie
        self.status = status
        self.marca = marca
        self.id_sala = id_sala
        self.id_coped = id_coped
        self.modelo = modelo

    def __repr__(self) -> str:
        return f"<ArCondicionado numero_serie={self.numero_serie}, status={self.status}, marca={self.marca}, modelo={self.modelo}>"
