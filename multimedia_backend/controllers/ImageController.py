import PIL
from errors import *
import requests
import os
from models.image import ImageClass
from sqlalchemy.exc import SQLAlchemyError
from multimedia_algorithms.image_alg import * 
from models.config import host
import json

# path="D:\\Projects\\ContentBasedMultimediaRetrivalSystem\\multimedia_backend"
path="/media/dj/DJ/Senior College/2nd Term/Multimedia/Project/ContentBasedMultimediaRetrivalSystem/multimedia_backend"
# innerPath='\\static\\images\\'
innerPath='/static/images/'

def retrive_Image(imageUrl):
    #get all images
    All_Images = ImageClass.query.with_entities(ImageClass.offline_location,ImageClass.image_id,\
        ImageClass.url, ImageClass.mean, ImageClass.histogram, ImageClass.gabor,\
            ImageClass.object_in_pic, ImageClass.percent)
    images = [image for image in All_Images]  
    retrieved_images =[] 
    save_image({"url":imageUrl['link'], "title":"Untitled"})
    Image_to_compare = np.asarray(bytearray(requests.get(imageUrl['link']).content), dtype="uint8")
    Image_to_compare = imageLoad(Image_to_compare)
    algorithms=json.loads(imageUrl['retreival_algorithms'])
    for alg in ['Histogram','Mean','GaborFilter','RESNET']:    
        if algorithms[alg]:
            for i in images:
                print(i[0])
                Image_in_db = Load_from_Local(f"{path}{innerPath}{i[0]}")
                if alg=='Histogram' and compare_image_histgram(Image_to_compare, Image_in_db) is not None:
                    retrieved_images.append(f"http://{host}:5000/static/images/{i[0]}")
                elif alg=='Mean' and image_comapare_mean(Image_to_compare, MeanDeSerial(i[3]))<=50:
                    retrieved_images.append(f"http://{host}:5000/static/images/{i[0]}")
                elif alg=='GaborFilter' and Gabor_Method(Image_to_compare, GaborDeSerial(i[5]))>=50:
                    retrieved_images.append(f"http://{host}:5000/static/images/{i[0]}")
                # TODO: Integrate the RESNET
                elif alg=='RESNET':
                    DL = DeepLearning()
                    object_in_pic, percent = DL.predict_image(Image_to_compare)
                    if object_in_pic==i[6] and abs(percent-i[7])<20:
                        retrieved_images.append(f"http://{host}:5000/static/images/{i[0]}")
    return retrieved_images

def save_image(Image):
    All_Images = ImageClass.query.with_entities(ImageClass.url)
    images = [url for image in All_Images for url in image]
    if Image['url'] not in images: 
        file_count=0
        for base, dirs, files in os.walk(f"{path}{innerPath}"):
            for Files in files:
                file_count += 1
        response = requests.get(Image['url'])
        name = f"{Image['title']}_{file_count+1}"
        # TODO:Image Preprocessing
        im = np.asarray(bytearray(response.content), dtype="uint8")
        print(im.size)
        print(imageLoad(im).size)
        # First: Get the Histogram
        hist = Get_image_histogram(imageLoad(im))
        Image['histogram']=HistoSerial(hist)
        # Second: Get the mean
        mean = Get_image_mean_color(imageLoad(im))
        Image['mean'] = MeanSerial(mean)
        # Third: Get the Object
        DL = DeepLearning()
        object_in_image, percent = DL.predict_image(imageLoad(im))
        Image['object_in_pic'] = object_in_image
        print(object_in_image, float(percent))
        Image['percent'] = float(percent)
        # Forth: Get the Gabor
        G = Gabor()
        gabor = G.gabor_histogram(imageLoad(im))
        Image['gabor'] = GaborSerial(gabor)
        # check if url is duplicate, then add to database
        Image['offline_location']=f"{name}.png"
        newImage = ImageClass(**Image)
        try:
            newImage.insert()
        except SQLAlchemyError as e:
                error = str(e.__dict__['orig'])
                raise ErrorHandler({
                    'description': error,
                    'status_code': 404
                })
        file = open(f"{path}{innerPath}{name}.png", "wb")
        file.write(im)
        file.close()

def save_binary_image(I2): 
    file_count=0
    for base, dirs, files in os.walk(f"{path}{innerPath}"):
        for Files in files:
            file_count += 1
    print(file_count, file_count+1)
    filename=I2['content'].filename.split('.')[0]
    name = f"{filename}_{file_count+1}"
    # TODO:Image Preprocessing
    Image={}
    Image['url']=''
    Image['title']=filename
    Image['author']=I2['author']
    Image['description']=I2['description']
    im = np.asarray(bytearray(I2['content'].read()), dtype="uint8")
    print(im.size)
    print(imageLoad(im).size)
    # First: Get the Histogram
    hist = Get_image_histogram(imageLoad(im))
    Image['histogram']=HistoSerial(hist)
    # Second: Get the mean
    mean = Get_image_mean_color(imageLoad(im))
    Image['mean'] = MeanSerial(mean)
    # Third: Get the Object
    DL = DeepLearning()
    object_in_image, percent = DL.predict_image(imageLoad(im))
    Image['object_in_pic'] = object_in_image
    print(object_in_image, float(percent))
    Image['percent'] = float(percent)
    # Forth: Get the Gabor
    G = Gabor()
    gabor = G.gabor_histogram(imageLoad(im))
    Image['gabor'] = GaborSerial(gabor)
    # check if url is duplicate, then add to database
    Image['offline_location']=f"{name}.png"
    newImage = ImageClass(**Image)
    print("saving")
    try:
        newImage.insert()
        print("Saved")
    except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            raise ErrorHandler({
                'description': error,
                'status_code': 404
            })
    file = open(f"{path}{innerPath}{name}.png", "wb")
    file.write(im)
    file.close()

def Load_from_Local(URL):
    Image_in_db = open(URL,'rb')
    Image_in_db = Image_in_db.read()
    Image_in_db = np.asarray(bytearray(Image_in_db), dtype='uint8')
    Image_in_db = imageLoad(Image_in_db)
    return Image_in_db

# save_image({"url":"https://i.ytimg.com/vi/sC-dEuejKHk/maxresdefault.jpg", "title":"Spider-Man"})