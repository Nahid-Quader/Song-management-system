

# This programme will organize all songs from the input folder by artist name and saves all folders into the destination path....

import os
from termcolor import colored
import shutil
import eyed3
path = raw_input("please enter the path :")
FileName = []
SingerName = []
Match = []
Artist = None


koma = None
dpath =raw_input("please give the destination path :")
for name in os.listdir(path):
    try:
        FilePath = path + path[2] + name
        file = eyed3.load(FilePath)

        if (file.tag.artist is not None):
            print ("Title ",name)
            print ("Artist ",file.tag.artist)
            Artist = file.tag.artist
            newpath = dpath + path[2] + Artist
            if not os.path.exists(newpath):
                os.makedirs(newpath)
            CurrentPath = path + path[2] + name
            Destination = newpath + path[2] + name
            shutil.move(CurrentPath, Destination)
    except Exception as x:
        print x
        pass
