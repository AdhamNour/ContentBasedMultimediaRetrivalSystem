from Katna.video import Video
from Katna.writer import KeyFrameDiskWriter
import os
from multimedia_algorithms import image_alg 
# input vedio path , destination folderr , no of key frames 
def key_frame_extraction(video_path, destination, no_of_frames_to_returned=10):
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
        query_image_path = (query_video_path)+'/'+str(file_name1)+'.jpeg'
        for database_key_frame in key_frames2:
            file_name2 = database_key_frame.split('.')[0]
            database_image_path = (database_video_path) + '/' + str(file_name2) + '.jpeg'
            if image_alg.compare_image_histgram(query_image_path, database_image_path,"CORREL"):
                 score += 1
                 break
    if (score / len(key_frames1)) > 0.5: # 0.5 deh bal habad
        print("hema win")
        return database_video_path
    else:
         print("hema lose")
         return False


if __name__ == "__main__" :
    #key_frame_extraction("C:/Users/ibrahim shoukry/Desktop/mm project/alg/vedio_1.mp4" ,"C:/Users/ibrahim shoukry/Desktop/mm project/alg/vedio", 15)
    #key_frame_extraction("C:/Users/ibrahim shoukry/Desktop/mm project/alg/vedio_1.mp4" ,"C:/Users/ibrahim shoukry/Desktop/mm project/alg/vedio3", 15)
    #compare_keyframes("C:/Users/ibrahim shoukry/Desktop/mm project/alg/vedio3","C:/Users/ibrahim shoukry/Desktop/mm project/alg/vedio2")
