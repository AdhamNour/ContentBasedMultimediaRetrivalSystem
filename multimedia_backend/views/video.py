from flask_restful import Resource,reqparse
from controllers.VideoController import retrive_Video
class Video(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('link')
    def post(self):
        return {"yourlink": retrive_Video(self.reqparse.parse_args()['link'])}