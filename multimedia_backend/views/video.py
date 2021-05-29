from flask_restful import Resource,reqparse

class Video(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('link')
    def post(self):
        return {"yourlink": self.reqparse.parse_args()['link']}