# convert videoo to its frames.

import cv2
import os
import shutil

# Opens the Video file
video = input("please give path to video : \n")

cap= cv2.VideoCapture(video)
i=0
if not os.path.exists('./output_video_frames'):
    os.mkdir("./output_video_frames")
else:
    shutil.rmtree("./output_video_frames") 
    os.mkdir("./output_video_frames")
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        print("done")
        break
    cv2.imwrite('./output_video_frames/frame'+str(i).zfill(6)+'.jpg',frame)
    i+=1
 
cap.release()
cv2.destroyAllWindows()