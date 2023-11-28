from flask_restful import fields
from helper.database import db
from model.pessoa import Pessoa


professor_fields = {
    'id':   fields.Integer,
    'nome':   fields.String,
    'sobrenome':   fields.String,
    'email':   fields.String,
    'telefone':   fields.String,
    'numero_matricula': fields.Integer,
    'titulacao':   fields.String,
}


class Professor(Pessoa):
    __tablename__ = "tb_professor"
    professor_id  = db.Column(db.Integer, db.ForeignKey('pessoa.id'), nullable=False)
    numero_matricula = db.Column(db.Integer, primary_key=True)
    titulacao = db.Column(db.String(255), nullable=False)

    cursos = db.relationship("Curso", back_populates="professor")

    __mapper_args__ = {'polymorphic_identity': "professor", 'concrete': True}

    def __init__(self, nome: str, sobrenome: str, email: str, telefone: str, numero_matricula: int, titulacao: str):
        super().__init__(nome, email)
        self.sobrenome = sobrenome
        self.telefone = telefone
        self.numero_matricula = numero_matricula
        self.titulacao = titulacao

    def __repr__(self) -> str:
        return f"<Professor numero_matricula={self.numero_matricula}>"
