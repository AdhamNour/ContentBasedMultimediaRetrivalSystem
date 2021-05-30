from flask_restful import Resource,reqparse
from controllers.ImageController import retrive_Image
class Image(Resource):
    
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('link', type=str, location='json')
        self.reqparse.add_argument('retreival_algorithms', type=str, location='json')
    
    def post(self):
        print(self.reqparse.parse_args())
        return {"result_links": retrive_Image(self.reqparse.parse_args())}