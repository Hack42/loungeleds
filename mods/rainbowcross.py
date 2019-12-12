#!/bin/bash

from PIL import Image,ImageDraw
from colortable import colortable
from pixmap import pixmap
import base64

def run():
    kleuren = colortable(122)
    pixels = pixmap()
    while True:
       leddata = ""
       img = Image.new("RGB", (70,50), "#FFFFFF")
       draw = ImageDraw.Draw(img)
       i=0
       for i in range(122):
           draw.line((0,i,i,0), fill=(int(kleuren[i][0]),int(kleuren[i][1]),int(kleuren[i][2])))
       imgbytes = img.tobytes()
       for i in range(max(pixels.keys())):
           (myx,myy) = pixels[i]
           pixpos = (myy*70+myx)*3
           leddata += imgbytes[pixpos:pixpos+3]
       x = kleuren[0]
       kleuren = kleuren[1:] + [x]
       yield (0.2,leddata)


