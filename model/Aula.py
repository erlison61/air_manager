from flask_restful import fields

from helper.database import db
from datetime import datetime
from model.professor import Professor
from model.Sala import Sala

aula_fields = {
    'id': fields.Integer,
    'inicio': fields.DateTime(dt_format='iso8601'),
    'fim': fields.DateTime(dt_format='iso8601'),
    'professor_id': fields.Integer,
    'sala_id': fields.Integer,

}


class Aula(db.Model):
    __tablename__ = "tb_aula"
    id = db.Column(db.Integer, primary_key=True)
    inicio = db.Column(db.DateTime, nullable=False)
    fim = db.Column(db.DateTime, nullable=False)

    professor_id = db.Column(db.Integer, db.ForeignKey(
        'tb_professor.id'), nullable=False)
    sala_id = db.Column(db.Integer, db.ForeignKey('tb_sala.id'))

    professor = db.relationship(Professor)
    sala = db.relationship(Sala)

    def __init__(self, inicio: datetime, fim: datetime, professor: object, sala: object, disciplina_id: int):
        self.inicio = inicio
        self.fim = fim
        self.professor = professor
        self.sala = sala
        self.disciplina_id = disciplina_id

    def __repr__(self) -> str:
        return f"<Aula id={self.id}, inicio={self.inicio}, fim={self.fim}>"
