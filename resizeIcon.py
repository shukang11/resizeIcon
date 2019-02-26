# -*- coding: utf-8 -*-
import os
import sys
from PIL import Image, ImageFilter

class IconLoader:
    sourcePath = ""
    image = None
    extensionName = ""
    fileName = ""

    def __init__(self, source):
        self.sourcePath = source
        self.image = Image.open(source)
        f_list = os.path.splitext(source)
        self.fileName = f_list[0]
        self.extensionName = f_list[1]
        print(self.fileName, self.extensionName)

    def convertNameWithSize(self, name, size):
        return name \
              + "{}".format(size[0]) \
              + "x{}".format(size[1])+self.extensionName

    def saveImages(self, sizes=sizeMap):
        tardir = "source/"
        if os.path.exists(tardir) == False:
            os.mkdir(tardir)
        for size in sizes:
            outName = self.convertNameWithSize(self.fileName, size)
            print(outName)
            dir = tardir + outName
            self.image.resize(size).save(dir)

    def close(self):
        self.image.close()


filename = sys.argv[1]

assert filename != None

image = IconLoader(filename)
image.saveImages()
image.close()
