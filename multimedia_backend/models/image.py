from models.config import db
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ImageClass(db.Model, Base):
    __tablename__ = 'image'
    image_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(70))
    url = db.Column(db.String(2000))
    offline_location = db.Column(db.String(2000))
    percent = db.Column(db.Float)
    object_in_pic = db.Column(db.String(70)) 
    author = db.Column(db.String(80))
    histogram = db.Column(db.JSON)
    mean = db.Column(db.JSON)
    description = db.Column(db.String(2000))
    gabor = db.Column(db.JSON)

    def serialize(self):
        return {
            "image_id":self.image_id,
            "title": self.title,
            "url":self.url,
            "offline_location": self.offline_location,
            "percent":self.percent,
            "object_in_pic": self.object_in_pic,
            "author":self.author,
            "histogram":self.histogram,
            "mean":self.mean,
            "description":self.description,
            "gabor":self.gabor 
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