from flask_restful import fields

from helper.database import db
from model.TecnicoAdministrativo import TecnicoAdministrativo, tecnico_administrativo_fields

coped_fields = {
    'id': fields.Integer,
    'tecnicoAdministrativo': fields.Nested(tecnico_administrativo_fields)
}

'''
{
    id: 1,
    tecnicoAdministrativo: {id: 1}
}
'''


class Coped(db.Model):
    __tablename__ = "tb_coped"
    id = db.Column(db.Integer, primary_key=True)

    tecnicoAdministrativo_id = db.Column(db.Integer, db.ForeignKey(
        'tb_tecnico_administrativo.id'), nullable=False)

    tecnicoAdministrativo = db.relationship(TecnicoAdministrativo)

    def __init__(self, tecnicoAdministrativo: object):
        self.tecnicoAdministrativo = tecnicoAdministrativo

    def __repr__(self) -> str:
        return f"<Coped id={self.id}>"


