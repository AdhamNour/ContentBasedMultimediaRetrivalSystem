from models.config import db
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class VideoClass(db.Model, Base):
    __tablename__ = 'video'
    video_id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(70))
    title = db.Column(db.String(80))
    author = db.Column(db.String(80))
    description = db.Column(db.String(2000))
    no_of_keyframes = db.Column(db.Integer)
    length = db.Column(db.Integer)
    offline_location = db.Column(db.String(2000))
    keyFrame_location = db.Column(db.String(2000))

    def serialize(self):
        return {
            "video_id": self.video_id,
            "url": self.url,
            "author": self.author,
            "description": self.description,
            "no_of_keyframes": self.no_of_keyframes,
            "length": self.length
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
