import os
import cv2

path = "Images"
images = []

for i in os.listdir(path):
    name, ext = os.path.splitext(i)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+i

        print(file_name)
               
        images.append(file_name)
        
count = len(images)

frame = cv2.imread(images[0])
height, width, channel = frame.shape
size = (width, height)
print(size)

output = cv2.VideoWriter("Project.mp4",cv2.VideoWriter_fourcc(*'DIVX'),3,size)

for i in range(0,count-1):
    img = cv2.imread(images[i])
    output.write(img)
        
print("Done")