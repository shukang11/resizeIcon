# -*- coding: utf-8 -*-
import os
import sys
from PIL import Image, ImageFilter
from docopt import docopt

from config import ios_icon_sizes, ios_launch_sizes

__ALL_SIZE_TYPE__ = [ "icon", "launch" ]
class IconLoader:
    sourcePath = ""
    image = None
    extensionName = ""
    fileName = ""
    size_type = ""

    def __init__(self, source: str, size_type: str):
        self.sourcePath = source
        self.image = Image.open(source)
        f_list = os.path.splitext(source)
        self.fileName = f_list[0]
        self.extensionName = f_list[1]
        self.size_type = size_type

    def convertNameWithSize(self, name: str, size: tuple) -> str:
        return name \
              + "{}".format(size[0]) \
              + "x{}".format(size[1])+self.extensionName

    def saveImages(self):
        sizes = self._generator_sizes()
        tardir = "source/"
        if os.path.exists(tardir) == False:
            os.mkdir(tardir)
        for size in sizes:
            outName = self.convertNameWithSize(self.fileName, size)
            dir = tardir + outName
            self.image.resize(size).save(dir)

    def close(self):
        self.image.close()

    def _generator_sizes(self) -> list:
        if self.size_type == "icon":
            return ios_icon_sizes()
        elif self.size_type == "launch":
            return ios_launch_sizes()



def cli():
    cli_docs = """resizeIcon: icon tool
    usage:
      resizeIcon <file> [--type=<type>]
      resizeIcon (-h | --help)

    options::
      -h --help         Show the screen
      --type=<type>     size config type
    
    """
    arguments = docopt(cli_docs)

    file = arguments["<file>"]
    size_type = arguments["--type"]

    if size_type not in __ALL_SIZE_TYPE__:
        print("require one of {}".format(__ALL_SIZE_TYPE__))
        exit(64)

    if not file:
        print("file option is required.")
        exit(64)

    icon = IconLoader(file, size_type)
    icon.saveImages()
    icon.close()


if __name__ == "__main__":
    cli()