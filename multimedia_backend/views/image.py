from flask_restful import Resource,reqparse
from controllers.ImageController import  retrive_Image
class Image(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('link')
    def post(self):
        
        return {"yourlink": retrive_Image(self.reqparse.parse_args()['link'])}