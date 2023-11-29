from flask_restful import fields
from helper.database import db
from model.Pessoa import Pessoa


professor_fields = {
    'id':   fields.Integer,
    'numero_matricula': fields.Integer,
    'nome':   fields.String,
    'sobrenome':   fields.String,
    'email':   fields.String,
    'telefone':   fields.String,
    'titulacao':   fields.String,
}


class Professor(Pessoa):
    __tablename__ = "tb_professor"
    id = db.Column(db.Integer, primary_key=True)
    numero_matricula = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    sobrenome = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    telefone = db.Column(db.String(255), nullable=False)
    titulacao = db.Column(db.String(255), nullable=False)

    # cursos = db.relationship(
    #     "Curso", back_populates="professor")  # TODO Remover ✅

    __mapper_args__ = {'polymorphic_identity': "professor", 'concrete': True}

    def __init__(self, id:int, nome: str, sobrenome: str, email: str, telefone: str, numero_matricula: int, titulacao: str):
        super().__init__(nome,sobrenome,email)
        self.id = id
        self.telefone = telefone
        self.numero_matricula = numero_matricula
        self.titulacao = titulacao

    def __repr__(self) -> str:
        return f"<Professor numero_matricula={self.numero_matricula}>"
