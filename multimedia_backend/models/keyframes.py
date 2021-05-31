from models.config import db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import ForeignKey

Base = declarative_base()


class keyframeClass(db.Model, Base):
    __tablename__ = 'keyframe'
    keyframe_id = db.Column(db.Integer, primary_key=True)
    video_id = db.Column(db.Integer, ForeignKey(
        'video.video_id', ondelete='CASCADE', onupdate="CASCADE"))
    offline_location = db.Column(db.String(2000))
    percent = db.Column(db.Float)
    object_in_pic = db.Column(db.String(70))
    histogram = db.Column(db.Float)
    mean = db.Column(db.Float)

    def serialize(self):
        return {
            "keyframe_id": self.keyframe_id,
            "video_id": self.video_id,
            "offline_location": self.offline_location,
            "percent": self.percent,
            "object_in_pic": self.object_in_pic,
            "histogram": self.histogram,
            "mean": self.mean,
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
