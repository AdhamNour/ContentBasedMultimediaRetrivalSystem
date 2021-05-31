from errors import ErrorHandler
from flask_restful import Resource,reqparse
from controllers.VideoController import retrive_Video, save_video
from flask import jsonify

class VideoSearch(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('link')
    def post(self):
        return {"result_links": retrive_Video(self.reqparse.parse_args()['link'])}
    
class VideoUpload(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('url')
        self.reqparse.add_argument('author')
    
    def post(self):
        args = self.reqparse.parse_args()
        try:
            save_video(args)
        except ErrorHandler as e:
            return e.error
        return {
            'message': 'Video uploaded successfully',
            'status code': 200
        }