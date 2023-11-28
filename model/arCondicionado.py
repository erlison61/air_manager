from flask_restful import fields
from helper.database import db
from model.sala import Sala  
from model.coped import Coped  

ar_condicionado_fields = {
    'numero_serie': fields.Integer,
    'status': fields.Boolean,
    'marca': fields.String,
    'id_sala': fields.Integer,
    'id_coped': fields.Integer,
    'modelo': fields.String,
}

class ArCondicionado(db.Model):
    __tablename__ = "tb_ar_condicionado"
    numero_serie = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(255), nullable=False)
    marca = db.Column(db.String(255), nullable=False)
    id_sala = db.Column(db.Integer, db.ForeignKey('tb_sala.id'))
    id_coped = db.Column(db.Integer, db.ForeignKey('tb_coped.id'))
    modelo = db.Column(db.String(255), nullable=False)

    sala = db.relationship(Sala, backref=db.backref('ar_condicionados', lazy=True))
    coped = db.relationship(Coped, backref=db.backref('ar_condicionados', lazy=True))

    def __init__(self, numero_serie: int, status: bool, marca: str, id_sala: int, id_coped: int, modelo: str):
        self.numero_serie = numero_serie
        self.status = status
        self.marca = marca
        self.id_sala = id_sala
        self.id_coped = id_coped
        self.modelo = modelo

    def __repr__(self) -> str:
        return f"<ArCondicionado numero_serie={self.numero_serie}, status={self.status}, marca={self.marca}, modelo={self.modelo}>"
