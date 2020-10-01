#!/usr/bin/env python3

from PIL import Image
import os

def fix_image(img, name):
   img.rotate(-90).resize((128,128)).convert('RGB').save("/opt/icons/"+name, format="JPEG")

path = os.getcwd()+ "/images/"
files = os.listdir(path)

for f in files:

   name, _ = os.path.splitext(f)

   if name.find("ic_") != -1:
      im = Image.open(path+f)
      fix_image(im, name)
