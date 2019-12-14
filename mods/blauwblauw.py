#!/bin/bash

from PIL import Image,ImageDraw
from colortable import colortable
from pixmap import pixmap
import base64

def run():
    pixels = pixmap()
    for nothing in range(0,5):
       leddata = ""
       img = Image.new("RGB", (70,50), "#FFFFFF")
       draw = ImageDraw.Draw(img)
       for i in range(25):
           draw.line((0,i,70,i), fill=(0,0,255))
       for i in range(25,50):
           draw.line((0,i,70,i), fill=(0,0,0))
       imgbytes = img.tobytes()
       for i in range(max(pixels.keys())):
           (myx,myy) = pixels[i]
           pixpos = (myy*70+myx)*3
           leddata += imgbytes[pixpos:pixpos+3]
       leddata += "\x00\x00\xff" * (790 - max(pixels.keys()))
       yield (0.4,leddata)
   

       leddata = ""
       img = Image.new("RGB", (70,50), "#FFFFFF")
       draw = ImageDraw.Draw(img)
       for i in range(25):
           draw.line((0,i,70,i), fill=(0,0,0))
       for i in range(25,50):
           draw.line((0,i,70,i), fill=(0,0,255))
       imgbytes = img.tobytes()
       for i in range(max(pixels.keys())):
           (myx,myy) = pixels[i]
           pixpos = (myy*70+myx)*3
           leddata += imgbytes[pixpos:pixpos+3]
       leddata += "\x00\x00\x00" * (790 - max(pixels.keys()))
       yield (0.4,leddata)
