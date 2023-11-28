from flask_restful import fields
from helper.database import db
from model.tecnicoAdministrativo import TecnicoAdministrativo 

coped_fields = {
    'id_tecnicoAdministrativo': fields.Integer,
    'id': fields.Integer,
}

class Coped(db.Model):
    __tablename__ = "tb_coped"
    id = db.Column(db.Integer, primary_key=True)
    id_tecnicoAdministrativo = db.Column(db.Integer, db.ForeignKey('tb_tecnico_administrativo.id'), nullable=False)

    tecnico_Administrativo = db.relationship(TecnicoAdministrativo, backref=db.backref('coped', lazy=True))

    def __init__(self, id_tecnicoAdministrativo: int):
        self.id_tecnicoAdministrativo = id_tecnicoAdministrativo

    def __repr__(self) -> str:
        return f"<Coped id={self.id}>"
