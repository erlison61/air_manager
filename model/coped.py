from flask_restful import fields
from helper.database import db
from model.TecnicoAdministrativo import TecnicoAdministrativo 

coped_fields = {
    'tecnicoAdministrativo_id': fields.Integer,
    'id': fields.Integer,
}

class Coped(db.Model):
    __tablename__ = "tb_coped"
    id = db.Column(db.Integer, primary_key=True)
    tecnicoAdministrativo_id = db.Column(db.Integer, db.ForeignKey('tb_tecnico_administrativo.id'), nullable=False)

    tecnico_Administrativo = db.relationship(TecnicoAdministrativo)

    def __init__(self, tecnicoAdministrativo_id: int):
        self.tecnicoAdministrativo_id = tecnicoAdministrativo_id

    def __repr__(self) -> str:
        return f"<Coped id={self.id}>"
