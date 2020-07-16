import sys
import os



data_path = "/Users/taisei/Academic/reiwa02研究/program/image_manipulation/dataset_ManTra/CASIA/test"
data_path1 = data_path + "/tam"
data_path2 = data_path + "/mask"

data1 = [f for f in os.listdir(data_path1) if not f.startswith('.')]
data2 = [f for f in os.listdir(data_path2) if not f.startswith('.')]



data1_new=[]
data2_new=[]

for i in range(len(data1)):
    data1_new.append(data1[i].split('_',8)[7].split('.',1)[0])
for i in range(len(data2)):
    data2_new.append(data2[i].split('_',8)[7].split('.',1)[0])

for i in range(len(data1)):
    print(data1_new[i],":",data1_new[i] in data2_new)


data1_new.sort()
data2_new.sort()
