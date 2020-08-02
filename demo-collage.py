from os.path import join as pjoin, abspath, realpath, basename, dirname, exists as pexists
from mrivis.utils import read_image, scale_0to1
from matplotlib import pyplot as plt
import numpy as np
import os
from mrivis import Collage
import sys
#import mrivis

if len(sys.argv)==2:
    path1 = sys.argv[1]
    if os.path.isfile(path1):
        img_one = read_image(path1, None)
        scaled_img_one = scale_0to1(img_one)
        collage = Collage()
        collage.attach(scaled_img_one)
        collage.fig.savefig('collage.png')
    else:
        print(f"File not found:  {path1}")
else:
    print("Usage: python demo-collage.py full-path-to-nii-file")

