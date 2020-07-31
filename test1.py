from mrivis import checkerboard
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# REPLACE the paths with actual existing paths on your system
# If you don't have any data, some example data are provided in example_datasets folder of the mrivis repo
path1 = 'mrivis/example_datasets/3569_bl_PPMI.nii'
path2 = 'mrivis/example_datasets/3569_bl_PPMI_smoothed.nii'

#fig=checkerboard(path1, path2) # square patches
#fig.savefig('test.png')
checkerboard(path1, path2,output_path="test.png") # square patches
