from models.config import db
from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ImageClass(db.Model, Base):
    __tablename__ = 'image'
    image_id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(50))
    percent = db.Column(db.Float)
    author = db.Column(db.String(50))
    histogram = db.Column(db.Float)
    mean = db.Column(db.Float)
    description = db.Column(db.String(50))

    def serialize(self):
        return {

        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.merge(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()