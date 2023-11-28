from flask_restful import fields

from helper.database import db

pessoa_fields = {
    'id':   fields.Integer,
    'nome':   fields.String,
    'email':   fields.String,
}

class Pessoa(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    nome= db.Column(db.String(100), unique=False, nullable=False)
    email= db.Column(db.String(120), unique=True, nullable= False)
    discriminator = db.Column('type', db.String(50))
    tipo = db.Column(db.String, nullable=False)


    __mapper_args__ = {
        'polymorphic_on': discriminator,
        'polymorphic_identity':tipo
    }

    def __init__(self, nome: str, email: str):
        self.nome = nome
        self.email = email

    def __repr__(self) -> str:
        return "<Pessoa id={0}, nome={1}>".format(self.id, self.nome)

