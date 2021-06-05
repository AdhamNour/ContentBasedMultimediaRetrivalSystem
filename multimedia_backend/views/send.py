from flask_restful import Resource,reqparse
from flask import send_from_directory

class Send(Resource):
    def get(self, image):
        print(image)
        return send_from_directory(f'static/images', image)
