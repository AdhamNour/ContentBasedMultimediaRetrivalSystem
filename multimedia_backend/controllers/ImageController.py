from errors import *
import requests
import os
from models.image import ImageClass
from sqlalchemy.exc import SQLAlchemyError
from multimedia_algorithms.image_alg import * 

path="/media/dj/DJ/Senior College/2nd Term/Multimedia/Project/ContentBasedMultimediaRetrivalSystem/multimedia_backend/static/images/"


def retrive_Image(imageUrl):
    #get all images
    All_Images = ImageClass.query.with_entities(ImageClass.offline_location,ImageClass.image_id, ImageClass.url, ImageClass.mean)
    images = [image for image in All_Images]  
    retrieved_images =[] 
    save_image({"url":imageUrl['link'], "title":"Untitled"})
    Image_to_compare = np.asarray(bytearray(requests.get(imageUrl['link']).content), dtype="uint8")
    Image_to_compare = imageLoad(Image_to_compare)
    print(imageUrl['retreival_algorithms'])
    # algorithms = json.load(imageUrl['retreival_algorithms'])
    # for alg in ['Histogram','Mean','GaborFilter','RESNET']:    
    #     if algorithms[alg]:
    #         for i in images:
    #             image = imageLoad(open(i[0]))
    #             if alg=='Histogram' and compare_image_histgram(Image_to_compare, image):
    #                 retrieved_images.append(i[2])
    #             elif alg=='Mean' and image_comapare_mean(Image_to_compare, MeanDeSerial(i[3]))<50:
    #                 retrieved_images.append(i[2])
    #             elif alg=='GaborFilter':
                    
    #                 retrieved_images.append(i[2])
    return retrieved_images

def save_image(Image):
    All_Images = ImageClass.query.with_entities(ImageClass.url)
    images = [url for image in All_Images for url in image]
    if Image['url'] not in images: 
        paths, dirs, files = next(os.walk(path))
        file_count = len(files)
        response = requests.get(Image['url'])
        name = f"{Image['title']}_{file_count+1}"
        # TODO:Image Preprocessing
        im = np.asarray(bytearray(response.content), dtype="uint8")
        # First: Get the Histogram
        hist = Get_image_histogram(imageLoad(im))
        Image['histogram']=HistoSerial(hist)
        # Second: Get the mean
        mean = Get_image_mean_color(imageLoad(im))
        Image['mean'] = MeanSerial(mean)
        # TODO: Third: Get the Object
        # check if url is duplicate, then add to database
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
        file.write(im)
        file.close()

    
# save_image({"url":"https://i.ytimg.com/vi/sC-dEuejKHk/maxresdefault.jpg", "title":"Spider-Man"})