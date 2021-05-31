from flask import Flask
from flask_restful import Resource,Api,reqparse

from views.video import Video
from views.image import *

from models.config import app_setup
from models.image import ImageClass
from models.video import VideoClass

app = Flask(__name__)
api = Api(app)
app_setup(app)
app.app_context().push()

api.add_resource(Video,'/Video')
api.add_resource(ImageSearch,'/Image')
api.add_resource(ImageUpload,'/uploadImage')

from models.config import host
if __name__ == '__main__':
    app.run(debug=True, host=host)