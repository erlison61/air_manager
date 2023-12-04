from flask_restful import fields

from helper.database import db
from model.Coped import Coped, coped_fields


sala_fields = {
    'id': fields.Integer,
    'numero_bloco': fields.Integer,
    'capacidade': fields.Integer,
    'tipo_sala': fields.String,
    'coped': fields.Nested(coped_fields)
}


class Sala(db.Model):
    __tablename__ = "tb_sala"

    id = db.Column(db.Integer, primary_key=True)
    numero_bloco = db.Column(db.Integer, nullable=False)
    capacidade = db.Column(db.Integer, nullable=False)
    tipo_sala = db.Column(db.String(255), nullable=False)

    coped_id = db.Column(db.Integer, db.ForeignKey('tb_coped.id'))

    coped = db.relationship(Coped)

    def __init__(self, numero_bloco: int, capacidade: int, tipo_sala: str, coped: object):
        self.numero_bloco = numero_bloco
        self.capacidade = capacidade
        self.tipo_sala = tipo_sala
        self.coped = coped

    def __repr__(self) -> str:
        return f"<Sala id={self.id}, numero_bloco={self.numero_bloco}, capacidade={self.capacidade}, tipo_sala={self.tipo_sala}>"
