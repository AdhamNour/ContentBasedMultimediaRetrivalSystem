from flask_restful import Resource,reqparse
from controllers.VideoController import retrive_Video
from flask import jsonify

class Video(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('link')
    def post(self):
        return {"result_links": retrive_Video(self.reqparse.parse_args()['link'])}