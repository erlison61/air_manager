from flask_restful import fields
from helper.database import db
from model.aula import Aula

sala_fields = {
    'id': fields.Integer,
    'numero_bloco': fields.Integer,
    'capacidade': fields.Integer,
    'tipo_sala': fields.String,
    'id_aula': fields.Integer,
}


class Sala(db.Model):
    __tablename__ = "tb_sala"
    id = db.Column(db.Integer, primary_key=True)
    numero_bloco = db.Column(db.Integer, nullable=False)
    capacidade = db.Column(db.Integer, nullable=False)
    tipo_sala = db.Column(db.String(255), nullable=False)

    def __init__(self, numero_bloco: int, capacidade: int, tipo_sala: str, id_aula: int):
        self.numero_bloco = numero_bloco
        self.capacidade = capacidade
        self.tipo_sala = tipo_sala

    def __repr__(self) -> str:
        return f"<Sala id={self.id}, numero_bloco={self.numero_bloco}, capacidade={self.capacidade}, tipo_sala={self.tipo_sala}>"
