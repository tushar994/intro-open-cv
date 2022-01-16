# import the opencv library
import cv2
import os
import shutil
# define a video capture object
vid = cv2.VideoCapture(0)

if not os.path.exists('./camera_video_frames'):
    os.mkdir("./camera_video_frames")
else:
    shutil.rmtree("./camera_video_frames") 
    os.mkdir("./camera_video_frames")
i=0
while(True):
      
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
  
    # Display the resulting frame
    cv2.imshow('frame', frame)
    cv2.imwrite('./camera_video_frames/frame'+str(i)+'.jpg',frame)
    i+=1
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()