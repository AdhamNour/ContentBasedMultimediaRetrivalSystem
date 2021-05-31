from flask_restful import Resource,reqparse
from controllers.ImageController import *
from errors import *
class ImageSearch(Resource):
    
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('link')
        self.reqparse.add_argument('retreival_algorithms')
    
    def post(self):
        print('[AdhamNour]',self.reqparse.parse_args())
        return {"result_links": retrive_Image(self.reqparse.parse_args())}
    
class ImageUpload(Resource):
    
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('url')
        self.reqparse.add_argument('author')
        self.reqparse.add_argument('title')
        self.reqparse.add_argument('description')
        
    def post(self):
        args = self.reqparse.parse_args()
        try:
            save_image(args)
        except ErrorHandler as e:
            return e.error
        return {
            'message': 'Image uploaded successfully',
            'status code': 200
        }
        