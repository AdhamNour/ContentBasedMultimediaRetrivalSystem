from flask import Flask
from flask_restful import Resource,Api,reqparse

from views.video import Video
from views.image import Image

from models.config import app_setup
from models.image import ImageClass

app = Flask(__name__)
api = Api(app)
app_setup(app)
app.app_context().push()

api.add_resource(Video,'/Video')
api.add_resource(Image,'/Image')
app_setup(app)
app.app_context().push()

if __name__ == '__main__':
    app.run(debug=True)