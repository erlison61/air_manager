from helper.database import db
from model.Sala import Sala
from model.arCondicionado import ArCondicionado


class ArCondicionadoSala(db.Model):

    __tablename__ = "tb_arcondicionado_sala"

    id = db.Column(db.Integer, primary_key=True)
    arcondicionado_id = db.Column(
        db.Integer, db.ForeignKey('tb_arcondicionado.id'))
    sala_id = db.Column(db.Integer, db.ForeignKey('tb_sala.id'))

    sala = db.relationship(Sala, lazy=True)

    arCondicionado = db.relationship(ArCondicionado, lazy=True)

    def __init__(self, sala, arCondicionado) -> None:
        self.sala = sala
        self.arCondicionado = arCondicionado
