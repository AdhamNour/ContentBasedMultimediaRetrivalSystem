from flask_restful import Resource,reqparse
from controllers.ImageController import  retrive_Image
class Image(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('link')
        self.reqparse.add_argument('retreival_algorithms')
    def post(self):
        print(self.reqparse.parse_args())
        return {"result_links": retrive_Image(self.reqparse.parse_args())}