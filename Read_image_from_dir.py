import numpy as np 
import os
import cv2


data_path = "/home/takahashi/dataset/ColumbiaUncompressedImageSplicingDetection/4cam_splc"

data = os.listdir(data_path)

data_list = []

for i in data:
    if i != "Thumbs.db" and i != ".DS_Store" and i != "edgemask":
        data = cv2.imread(os.path.join(data_path,i))
        data_list.append(data)
        print(data.shape)
    

    
