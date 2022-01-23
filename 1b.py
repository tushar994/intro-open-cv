import cv2
import glob
 
img_array = []
filenames = []

directory = input("please give path to directory (without the ending '/') : \n")
fps = input("please give the desired :\n")
if(not fps.isdigit()):
    print("invalid")
    exit()
fps = int(fps)
if(fps==0):
    print("invalid")
    exit()

for filename in glob.glob(directory + '/*.jpg'):
    filenames.append(filename)

filenames.sort()

for filename in filenames:
    # print(filename)
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)
 
 
out = cv2.VideoWriter('project.mp4',cv2.VideoWriter_fourcc(*'mp4v'), fps, size)

print("done")

for i in range(len(img_array)):
    out.write(img_array[i])
out.release()