from models.config import db
from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Image(db.Model, Base):
    __tablename__ = 'image'
    image_id = db.Column(db.Integer,primary_key=True)
    url=db.Column(db.String)
    percent=db.Column(db.Float)
    author=db.Column(db.String)
    histogram=db.Column(db.Float)
    mean=db.Column(db.Float)
    description=db.Column(db.String)
    

    def serialize(self):
        return {
            'id': self.user_id,
            'degree': self.scientific_degree,
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