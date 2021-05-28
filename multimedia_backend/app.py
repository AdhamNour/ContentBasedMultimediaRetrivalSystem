from flask import Flask
from flask_restful import Resource,Api,reqparse

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
# parser.add_argument('CourseCode')

class Video(Resource):
    def post(self):
        return {'hello':parser.parse_args()}

class Image(Resource):
    def get(self):
        return {"hello":'image'}

api.add_resource(Video,'/video')
api.add_resource(Image,'/image')

if __name__ == '__main__':
    app.run(debug=True)