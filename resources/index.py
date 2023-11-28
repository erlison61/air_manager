from flask_restful import Resource

class Index(Resource):
    def get(self):
        return {'versao': '1.0'}

    