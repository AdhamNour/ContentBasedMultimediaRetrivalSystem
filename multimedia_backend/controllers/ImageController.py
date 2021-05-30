from errors import *
import requests
import os
from models.image import ImageClass
from sqlalchemy.exc import SQLAlchemyError
path="/media/dj/DJ/Senior College/2nd Term/Multimedia/Project/ContentBasedMultimediaRetrivalSystem/multimedia_backend/static/"


def retrive_Image(imageUrl):
    #get all images
    All_Images = ImageClass.query.with_entities(ImageClass.offline_location,ImageClass.image_id)
    image = [image for image in All_Images]
    
    retrieved_images =[] 
    save_image({"url":imageUrl['link'], "title":"Untitled"})
    #TODO: here where the call of the reterival algorithm should be called in stead of the for loop
    for i in image:
        retrieved_images.append(i[0])
    return retrieved_images

def save_image(Image):
    paths, dirs, files = next(os.walk(path))
    file_count = len(files)
    response = requests.get(Image['url'])
    name = f"{Image['title']}_{file_count}"
    #TODO:Image Preprocessing
    #add to database
    Image['offline_location']=f"{path}{name}.png"
    newImage = ImageClass(**Image)
    try:
        newImage.insert()
    except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            raise ErrorHandler({
                'description': error,
                'status_code': 404
            })
    file = open(f"{path}{name}.png", "wb")
    file.write(response.content)
    file.close()
    
# save_image({"url":"https://i.ytimg.com/vi/sC-dEuejKHk/maxresdefault.jpg", "title":"Spider-Man"})