from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from pydbgen import pydbgen
import os
from flask_mail import Mail,Message
from flask_cors import CORS


db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def app_setup(app):
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://u0tdgitb0rcfe4j8:1tl1B8h6jPSdbWcpTDLL@bn9trazrz4wyjqhn8rrv-mysql.services.clever-cloud.com:3306/bn9trazrz4wyjqhn8rrv"
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['STATIC_PATH'] = "/media/dj/DJ/Senior College/2nd Term/Multimedia/Project/ContentBasedMultimediaRetrivalSystem/multimedia_backend/static"
    #app.config['ALLOWED_EXTENSIONS'] = ['jpg', 'jpeg', 'png']
    app.config['DEBUG'] = True
    app.config['CORS_HEADERS'] = 'Content-Type'
     
    db.app = app
    db.init_app(app)
    db.create_all()
    # seed(db)


def db_drop_and_create_all():
    db.drop_all()
    db.create_all()
