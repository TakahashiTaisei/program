import os

path = "/home/takahashi/dataset/ColumbiaUncompressedImageSplicingDetection/4cam_splc"
write_path = "./test.txt"

files = os.listdir(path)

f = open(write_path,mode="w")

for i in files:
    if i != "Thumbs.db" and i != ".DS_Store" and  i != "edgemask":
        f.write(i+"\n")


