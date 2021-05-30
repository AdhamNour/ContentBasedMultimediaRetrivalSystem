from os import sep
from typing import Counter
import cv2 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from numpy.lib.polynomial import RankWarning
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.resnet import preprocess_input ,decode_predictions
from keras.applications.resnet import ResNet152
from numpy.lib.utils import source
from skimage.filters import gabor_kernel
from skimage import color
import scipy.ndimage as ndi
from multiprocessing.pool import ThreadPool

# first fun to get histogeam from image Input : image , Output : histogram   (1)
def Get_image_histogram(image_path):
    hist = []
    image = mpimg.imread(image_path,cv2.IMREAD_COLOR)
    #image = cv2.cvtColor(image)
    for i in range(3):
      hist.append(cv2.calcHist([image],[i],None,[256],[0,256]))
    #plt.hist(image.ravel(),255,[0,256])
    return hist

# second fun to get different histogram input 2 image path , output : value of  similarity 
def compare_image_histgram(image_path1 , image_path2 , type_of_compare):
    scoure = 0
    diffs = []
     # return number from 0 to 1 
    if (type_of_compare == "CORREL" or type_of_compare == "correl"):
        compare_method = cv2.HISTCMP_CORREL
    # return number from 0 to 1 inversive    
    elif (type_of_compare == "distance" or type_of_compare == "DISTANCE"):
       compare_method = cv2.HISTCMP_BHATTACHARYYA
    diffs.append(cv2.compareHist(Get_image_histogram(image_path1)[0],Get_image_histogram(image_path2)[0],compare_method))
    diffs.append(cv2.compareHist(Get_image_histogram(image_path1)[1],Get_image_histogram(image_path2)[1],compare_method))
    diffs.append(cv2.compareHist(Get_image_histogram(image_path1)[2],Get_image_histogram(image_path2)[3],compare_method))
    for diff in diffs :
      if (compare_method == cv2.HISTCMP_CORREL):
          if diff * 100 > 20 :
            scoure += 1

      elif (compare_method == cv2.HISTCMP_BHATTACHARYYA):
          diff =  diff * 100
          diff = 100 - diff
          if diff  > 20 :
            scoure += 1
      #print(diff)
    if scoure > 2 :
      return image_path2
    scoure = 0


# function get string and return how many words are similarity 
def comapare_image_text(string_input , string_database):
    test = string_input.split(sep = " ")
    test2 = string_database.split(sep = " ")
    Rank = 0
    for i in test :
        for j in test2: 
            found = i in j
            if (found == True):
                Rank += 1
    return Rank

# function get image path , output : mean color of rgb  (2)
def Get_image_mean_color (image_path) :
    image = mpimg.imread(image_path,cv2.IMREAD_COLOR)
    #channels = cv2.mean(image)
    #observation = np.array([(channels[2], channels[1], channels[0])])
    #same as mean
    red_channel = image[:,:,2]
    green_channel = image[:,:,1]
    blue_channel = image[:,:,0]
    img_size = len(image[:,0]) * len(image[0,:])
    R_mean = sum(map(sum , red_channel)) / img_size 
    B_mean = sum(map(sum , blue_channel)) / img_size 
    G_mean = sum(map(sum , green_channel)) / img_size 
    observation = [R_mean, G_mean, B_mean]
    return observation

# function input  image path , mean color in database , output : average of color in image  
def image_comapare_mean (image_path , mean_color_in_db):
    diff = []
    similar = Get_image_mean_color(image_path)
    for i in range(3):
        diff[i] = abs(similar[i] - mean_color_in_db[i])
    average = sum(diff) / 3 
    return average  

# khald section (3) , (4) 

class DeepLearning(object):
    """docstring for DeepLearning"""
    def __init__(self):
        super(DeepLearning, self).__init__()
        self.model = ResNet152(weights='imagenet')

    def predict_image(self,image):
        if image.shape != (224,224,3):
            image =  cv2.resize(image, dsize=(224, 224), interpolation=cv2.INTER_CUBIC)
            print(image.shape)      

        # convert the image pixels to a numpy array
        image = img_to_array(image)
        # reshape data for the model
        image = np.expand_dims(image, axis=0)
        # prepare the image for the VGG model
        image = preprocess_input(image)
        # predict the probability across all output classes
        yhat = self.model.predict(image)
        # convert the probabilities to class labels
        label = decode_predictions(yhat)

        label_name =label[0][0][1]
        label_percentage =label[0][0][2]*100

        return label_name,label_percentage


class Gabor(object):

  def __init__(self):
    self.gabor_kernels = self.make_gabor_kernel()

  def make_gabor_kernel(self):
    filters = []
    ksize = 31
    for theta in np.arange(0, np.pi, np.pi / 16):
        kern = cv2.getGaborKernel((ksize, ksize), 4.0, theta, 10.0, 0.5, 0, ktype=cv2.CV_32F)
        kern /= 1.5*kern.sum()
        filters.append(kern)
    return filters

  def gabor_histogram(self, input, type ='global', n_slice= 2):
    ''' count img histogram
  
      arguments
        input    : a path to a image or a numpy.ndarray
        type     : 'global' means count the histogram for whole image
                   'region' means count the histogram for regions in images, then concatanate all of them
        n_slice  : work when type equals to 'region', height & width will equally sliced into N slices
        normalize: normalize output histogram
  
      return
        type == 'global'
          a numpy array with size len(gabor_kernels)
        type == 'region'
          a numpy array with size len(gabor_kernels) * n_slice * n_slice
    '''
    if isinstance(input, np.ndarray):  # examinate input type
      img = input.copy()
    else:
      img = scipy.misc.imread(input, mode='RGB')
    height, width, channel = img.shape
  
    if type == 'global':
      hist = self._gabor(img, kernels=self.gabor_kernels)
  
    elif type == 'region':
      hist = np.zeros((n_slice, n_slice, len(self.gabor_kernels)))
      h_silce = np.around(np.linspace(0, height, n_slice+1, endpoint=True)).astype(int)
      w_slice = np.around(np.linspace(0, width, n_slice+1, endpoint=True)).astype(int)
  
      for hs in range(len(h_silce)-1):
        for ws in range(len(w_slice)-1):
          img_r = img[h_silce[hs]:h_silce[hs+1], w_slice[ws]:w_slice[ws+1]]  # slice img to regions
          hist[hs][ws] = self._gabor(img_r, kernels=self.gabor_kernels)


    hist = cv2.calcHist([hist],[0],None,[256],[0,256]) 
  
    return hist
  
  def compareHist(self,image1,image2):
    
    hist1 =self.gabor_histogram(image1)
    hist2 =self.gabor_histogram(image2)

    return cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL )

  def _gabor(self, image, kernels):
    accum = np.zeros_like(image)
    for kern in kernels:
        fimg = cv2.filter2D(image, cv2.CV_8UC3, kern)
        np.maximum(accum, fimg, accum)
  
    return accum
  
# how to use it  
if __name__ == "__main__":
  G = Gabor()
  img = cv2.imread('test.png')
  img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

  img2 = cv2.imread('test2.png')
  img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

  hist = G.gabor_histogram(img)
  print(G.compareHist(img,img2))
  plt.plot(hist)
  plt.show()

