import os
import cv2

path = 'D:\\@fausto\\Downloads\\c113\\pasta117\\imagens'

Images = []

count = 0



for i in os.listdir(path):
    nome,ext = os.path.splitext(i)
    if ext in ['.gif','.jpg','.jpeg','png','jfif']:
        file_name=path+'/'+i
        print(i)
        Images.append(file_name)   
count = len(Images)
frame = cv2.imread(Images[0])
w = cv2.CAP_PROP_FRAME_WIDTH
h = cv2.CAP_PROP_FRAME_HEIGHT
size = (w,h)
print(size)
out = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVX'),0.8,size)

for i in range(0, count-1):
    frame = cv2.imread(Images[i])
    out.write(frame)