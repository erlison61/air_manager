from flask_restful import fields

from helper.database import db

pessoa_fields = {
    'id':   fields.Integer,
    'nome':   fields.String,
    'sobrenome': fields.String,
    'email':   fields.String
}


class Pessoa(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), unique=False, nullable=False)
    sobrenome = db.Column(db.String(255), unique=False, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)

    def __init__(self, id: int, nome: str, sobrenome: str, email: str):
        self.id = id
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email

    def __init__(self, nome: str, sobrenome: str, email: str):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email

    def __repr__(self) -> str:
        return f"""<Pessoa 
                        id={self.id},
                        nome={self.nome},
                        sobrenome={self.sobrenome}
                        email={self.email}>"""
