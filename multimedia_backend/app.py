from views.send import Send
from flask import Flask
from flask_restful import Resource,Api,reqparse

from views.video import *
from views.image import *

from models.config import app_setup

app = Flask(__name__, static_url_path='')
api = Api(app)
app_setup(app)
app.app_context().push()

api.add_resource(VideoSearch,'/Video')
api.add_resource(ImageSearch,'/Image')
api.add_resource(ImageUpload,'/uploadImage')
api.add_resource(BinaryImageUpload,'/uploadBinaryImage')
api.add_resource(VideoUpload,'/uploadVideo')
api.add_resource(Send, '/static/images/<image>')

from models.config import host
if __name__ == '__main__':
    app.run(debug=True, host=host)
    # TODO: Load the Image Database 
    # TODO: Fix the Object Detector