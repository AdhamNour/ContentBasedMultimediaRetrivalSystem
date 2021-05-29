from flask import Flask
from flask_restful import Resource,Api,reqparse

from views.video import Video
from views.image import Image

app = Flask(__name__)
api = Api(app)


api.add_resource(Video,'/Video')
api.add_resource(Image,'/Image')

if __name__ == '__main__':
    app.run(debug=True,host='192.168.1.9')