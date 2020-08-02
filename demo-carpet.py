from matplotlib import pyplot as plt
import numpy as np
import os
from mrivis import Collage
import sys


# load a func mri volume from the repo
epi_path = 'mrivis/example_datasets/epi_func.nii'
from mrivis import Carpet

# let's build one from the 4D volume
func_carpet = Carpet(epi_path)


ax = func_carpet.show()
# ax is the matplotlib Axis containing the Carpet image
#plt.show() # this command brings up the figure

ax.figure.savefig('carpet.png')
