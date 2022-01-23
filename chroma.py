import cv2
import glob
import numpy as np
 
# video = input("please give path to video1 : \n")
video = "./videos/chick.mp4"
cap= cv2.VideoCapture(video)

# video2 = input("please give path to video2 : \n")
video2 = "./videos/exp.mp4"
cap2 = cv2.VideoCapture(video2)

# fps = input("please give the desired :\n")
fps = "15"
if(not fps.isdigit()):
    print("invalid")
    exit()
fps = int(fps)
if(fps==0):
    print("invalid")
    exit()

filenames = []
img_array = []

lower_blue = np.array([0, 155, 20])     ##[R value, G value, B value]
upper_blue = np.array([70, 255, 120])

i =0

while(cap.isOpened() and cap2.isOpened() and i<1000):
    ret, frame = cap.read()
    ret2, frame2 = cap2.read()

    if(ret == False):
        break
    if(ret2 == False):
        break

    # cropped_fore = frame[0:720, 0:608]
    cropped_fore = frame

    height, width, layers = cropped_fore.shape
    size = (width,height)

    if ret == False or ret2 == False:
        print("done")
        break
    
    mask = cv2.inRange(cropped_fore, lower_blue, upper_blue)
    masked_image = np.copy(cropped_fore)
    masked_image[mask != 0] = [0, 0, 0]
    crop_background = frame2
    # crop_background = frame2[0:720, 0:608]

    # crop_background[mask == 0] = [0, 0, 0]
    # mask2 = cv2.inRange(frame2, lower_blue, upper_blue)
    crop_background[mask == 0] = [0, 0, 0]

    final_image = crop_background + masked_image
    img_array.append(final_image)
    i+=1
    # print(i)

 
cap.release()
cap2.release()
cv2.destroyAllWindows()

for filename in filenames:
    img = cv2.imread(filename)
    
    img_array.append(img)

height, width, layers = img_array[0].shape
size = (width,height)
 
out = cv2.VideoWriter('project1.mp4',cv2.VideoWriter_fourcc(*'mp4v'), fps, size)

print("done")

for i in range(len(img_array)):
    out.write(img_array[i])
out.release()