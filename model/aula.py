from flask_restful import fields
from helper.database import db
from datetime import datetime
from model.professor import Professor  
from model.sala import Sala  

aula_fields = {
    'id': fields.Integer,
    'inicio': fields.DateTime(dt_format='iso8601'),
    'fim': fields.DateTime(dt_format='iso8601'),
    'professor_id': fields.String,
    'sala_id': fields.Integer,
  
}

class Aula(db.Model):
    __tablename__ = "tb_aula"
    id = db.Column(db.Integer, primary_key=True)
    inicio = db.Column(db.DateTime, nullable=False)
    fim = db.Column(db.DateTime, nullable=False)
    professor_id = db.Column(db.String(255), db.ForeignKey('tb_professor.professor_id'), nullable=False)
    sala_id = db.Column(db.Integer, db.ForeignKey('tb_sala.id'))

    professor = db.relationship(Professor, backref=db.backref('aulas', lazy=True))
    sala = db.relationship(Sala, backref=db.backref('aulas', lazy=True))

    def __init__(self, inicio: datetime, fim: datetime, professor_id: str, sala_id: int, disciplina_id: int):
        self.inicio = inicio
        self.fim = fim
        self.professor_id = professor_id
        self.sala_id = sala_id
        self.disciplina_id = disciplina_id

    def __repr__(self) -> str:
        return f"<Aula id={self.id}, inicio={self.inicio}, fim={self.fim}>"
