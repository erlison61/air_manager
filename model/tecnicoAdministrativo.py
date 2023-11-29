from flask_restful import fields
from helper.database import db
from model.Coped import Coped

tecnico_administrativo_fields = {
    'id_coped': fields.Integer,
    'id': fields.Integer,
    'nome': fields.String,
    'telefone': fields.String,
    'cargo': fields.String,
    'email': fields.String,
}

class TecnicoAdministrativo(db.Model):
    __tablename__ = "tb_tecnico_administrativo"
    id = db.Column(db.Integer, primary_key=True)
    id_coped = db.Column(db.Integer, db.ForeignKey('tb_coped.id'))
    nome = db.Column(db.String(255), nullable=False)
    telefone = db.Column(db.String(255), nullable=False)
    cargo = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255))

    coped = db.relationship(Coped, backref=db.backref('tecnico_administrativo', lazy=True))

    def __init__(self, id_coped: int, nome: str, telefone: str, cargo: str, email: str):
        self.id_coped = id_coped
        self.nome = nome
        self.telefone = telefone
        self.cargo = cargo
        self.email = email

    def __repr__(self) -> str:
        return f"<TecnicoAdministrativo id={self.id}, nome={self.nome}, cargo={self.cargo}>"
