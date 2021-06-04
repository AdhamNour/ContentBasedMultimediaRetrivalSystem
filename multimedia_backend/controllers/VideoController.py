from errors import ErrorHandler
from models.video import VideoClass
from numpy.testing._private.utils import temppath
import pytube
from models.video import VideoClass
from sqlalchemy.exc import SQLAlchemyError
from multimedia_algorithms.vedio_keyframes import *

path = "/media/dj/DJ/Senior College/2nd Term/Multimedia/Project/ContentBasedMultimediaRetrivalSystem/multimedia_backend/static/videos/"
keyPath = '/media/dj/DJ/Senior College/2nd Term/Multimedia/Project/ContentBasedMultimediaRetrivalSystem/multimedia_backend/static/keyframes/'

def retrive_Video(VideoUrl):
    retrived_videos =[]
    Videos = VideoClass.query.with_entities(VideoClass.keyFrame_location, VideoClass.url)
    DB_videos=[ video for video in Videos ]
    Keyframes_to_Compare = save_temp_video(VideoUrl)
    for i in DB_videos:
        if compare_keyframes(Keyframes_to_Compare, i[0]) is not None:           
            retrived_videos.append(i[1])
    return retrived_videos

def save_video(Video):
    # TODO: Check if Video already Exists
    # Add Video to Database
    video = pytube.YouTube(Video['url'])
    Video['title'] = video.title
    Video['length'] = video.length
    Video['no_of_keyframes'] = 15 
    download = video.streams.first()
    download.download(path)
    Video['offline_location'] = f"{download.default_filename}"
    # Add Keyframes
    key_frame_extraction(f"{path}{Video['offline_location']}", f"{keyPath}{video.title}")
    Video['keyFrame_location'] = f"{video.title}"
    v = VideoClass(**Video)
    try:
        v.insert()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise ErrorHandler({
            'description': error,
            'status_code': 404
        })
    
    
tempPath = "/media/dj/DJ/Senior College/2nd Term/Multimedia/Project/ContentBasedMultimediaRetrivalSystem/multimedia_backend/static/temp/"
tempKeyPath = "/media/dj/DJ/Senior College/2nd Term/Multimedia/Project/ContentBasedMultimediaRetrivalSystem/multimedia_backend/static/tempKey/"

def save_temp_video(url):
    video = pytube.YouTube(url)
    download = video.streams.first()
    download.download(tempPath)
    offline_location = f"{path}{download.default_filename}"
    # Add Keyframes
    key_frame_extraction(offline_location, tempKeyPath)
    keyFrame_location = tempKeyPath
    return keyFrame_location