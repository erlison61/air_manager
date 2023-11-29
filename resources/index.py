from flask_restful import Resource

class IndexResource(Resource):
    def get(self):
        return {'message': 'Hello World'}

    