from models.config import db
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class VideoClass(db.Model, Base):
    __tablename__ = 'video'
    video_id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(70))
    percent = db.Column(db.Float)
    author = db.Column(db.String(80))
    histogram = db.Column(db.Float)
    mean = db.Column(db.Float)
    description = db.Column(db.String(2000))

    def serialize(self):
        return {
            "video_id":self.video_id,
            "url":self.url,
            "percent":self.percent,
            "author":self.author,
            "histogram":self.histogram,
            "mean":self.mean,
            "description":self.description
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