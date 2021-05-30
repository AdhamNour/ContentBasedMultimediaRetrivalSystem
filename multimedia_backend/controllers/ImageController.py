import requests
path="D:\Projects\MultimediaProject\static"

def retrive_Image(imageUrl):
    retrived_videos =[]
    #TODO: here where the call of the reterival algorithm should be called in stead of the for loop
    for i in range(10):
        retrived_videos.append(imageUrl['link'])
    return retrived_videos

def save_image(Image):
    response = requests.get(Image['URL'])
    file = open(f"{path}{Image['name']}.png", "wb")
    file.write(response.content)
    file.close()
    
save_image({"URL":"https://i.ytimg.com/vi/sC-dEuejKHk/maxresdefault.jpg", "name":"Spider-Man"})