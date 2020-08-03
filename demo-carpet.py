from matplotlib import pyplot as plt
import numpy as np
import os
from mrivis import Carpet
import sys


if len(sys.argv)==2:
    path1 = sys.argv[1]
    if os.path.isfile(path1):
        func_carpet = Carpet(path1)
        ax = func_carpet.show()
        ax.figure.savefig('carpet.png')

# load a func mri volume from the repo
#epi_path = 'mrivis/example_datasets/epi_func.nii'


# let's build one from the 4D volume




# ax is the matplotlib Axis containing the Carpet image
#plt.show() # this command brings up the figure


