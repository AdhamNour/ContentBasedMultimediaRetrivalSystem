from Katna.video import Video
from Katna.writer import KeyFrameDiskWriter
import os
from multimedia_algorithms.image_alg import * 
from controllers.ImageController import *

# input vedio path , destination folder , no of key frames 
def key_frame_extraction(video_path, destination, no_of_frames_to_returned=15):
    vd = Video()
    no_of_frames_to_returned = int(no_of_frames_to_returned)
    if not os.path.exists(destination):
        os.makedirs(destination)
    diskwriter = KeyFrameDiskWriter(location=destination)
    video_file_path = os.path.join(video_path)
    vd.extract_video_keyframes(
        no_of_frames=no_of_frames_to_returned, file_path=video_file_path,
        writer=diskwriter
    )
  
def compare_keyframes(query_video_path, database_video_path):
    key_frames1 = os.listdir(query_video_path)
    key_frames2 = os.listdir(database_video_path)
    score = 0
    for query_key_frame in key_frames1:
        file_name1 = query_key_frame.split('.')[0]
        query_image_path = (query_video_path)+str(file_name1)+'.jpeg'
        query_image = Load_from_Local(query_image_path)
        query_image = Get_image_histogram(query_image)
        for database_key_frame in key_frames2:
            file_name2 = database_key_frame.split('.')[0]
            database_image_path = (database_video_path) + '/' + str(file_name2) + '.jpeg'
            database_image = Load_from_Local(database_image_path)
            database_image = Get_image_histogram(database_image)
            if compare_image_histgram(query_image, database_image,"CORREL")>2:
                 score += 1
                 break
    result = score / len(key_frames1)
    return result


# if __name__ == "__main__" :
#     key_frame_extraction("/media/dj/DJ/Senior College/2nd Term/Multimedia/Project/ContentBasedMultimediaRetrivalSystem/multimedia_backend/static/videos/Milo Murphys Law -  How Do I Do It SONG.mp4" ,"/media/dj/DJ/Senior College/2nd Term/Multimedia/Project/ContentBasedMultimediaRetrivalSystem/multimedia_backend/static/keyframes/Milo Murphy's Law -  How Do I Do It SONG")
    #key_frame_extraction("C:/Users/ibrahim shoukry/Desktop/mm project/alg/vedio_1.mp4" ,"C:/Users/ibrahim shoukry/Desktop/mm project/alg/vedio3", 15)
    #compare_keyframes("C:/Users/ibrahim shoukry/Desktop/mm project/alg/vedio3","C:/Users/ibrahim shoukry/Desktop/mm project/alg/vedio2")
