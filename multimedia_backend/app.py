from flask import Flask
from flask_restful import Resource,Api,reqparse

from views.video import Video
from views.image import Image

from models.config import app_setup

app = Flask(__name__)
api = Api(app)


api.add_resource(Video,'/Video')
api.add_resource(Image,'/Image')
app_setup(app)
app.app_context().push()

if __name__ == '__main__':
    app.run(debug=True,host='192.168.1.9')