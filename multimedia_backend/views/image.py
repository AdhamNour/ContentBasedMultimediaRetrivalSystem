from flask_restful import Resource,reqparse, request
from controllers.ImageController import *
from errors import *
import werkzeug


class ImageSearch(Resource):
    
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('link')
        self.reqparse.add_argument('retreival_algorithms')
    
    def post(self):
        images = retrive_Image(self.reqparse.parse_args())
        print(images)
        return {"result_links": images}
    
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
        
class BinaryImageUpload(Resource):
    
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('content', type=werkzeug.datastructures.FileStorage,location='files')
        self.reqparse.add_argument('author')
        self.reqparse.add_argument('description')
        
    def post(self):
        
        #print(request.values)
        args = self.reqparse.parse_args()
        print(args)
        try:
            save_binary_image(args)
        except ErrorHandler as e:
            return e.error
        return {
            'message': 'Image uploaded successfully',
            'status code': 200
        }