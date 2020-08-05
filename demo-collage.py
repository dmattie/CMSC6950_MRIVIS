from os.path import join as pjoin, abspath, realpath, basename, dirname, exists as pexists
from mrivis.utils import read_image, scale_0to1
from matplotlib import pyplot as plt
import numpy as np
import os
from mrivis import Collage
import sys
import validators
import requests
import shutil
#import mrivis


def render(path1,imgpath):
    img_one = read_image(path1, None)
    scaled_img_one = scale_0to1(img_one)
    collage = Collage()
    collage.attach(scaled_img_one)
    collage.fig.savefig(imgpath)
if len(sys.argv)==2:
    path1 = sys.argv[1]
    if os.path.isfile(path1):
        if(path1!='T1sample'):
            shutil.copy(path1,'T1sample.nii')
        render(path1,'collage.png')
    else:
        if not validators.url(path1):
            print(f"File not found or not a valid URL:  {path1}")
        else:
            print(f"valid URL")
            r = requests.get(path1,allow_redirects=True)
            open('T1sample.nii','wb').write(r.content)
            render('T1sample.nii','collage.png')
            


        
else:
    print("Usage: python demo-collage.py {full-path-to-nii-file|url-to-nii")

