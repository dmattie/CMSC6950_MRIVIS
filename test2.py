from mrivis import checkerboard
from mrivis import color_mix
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# REPLACE the paths with actual existing paths on your system
# If you don't have any data, some example data are provided in example_datasets folder of the mrivis repo
#path1 = 'mrivis/example_datasets/3569_bl_PPMI.nii'
#path2 = 'mrivis/example_datasets/3569_bl_PPMI_smoothed.nii'
path1='../100307_T1w_acpc_dc.nii'
path2='../101309_T1w_acpc_dc.nii'

#fig=checkerboard(path1, path2) # square patches
#fig.savefig('test.png')
#checkerboard(path1, path2,output_path="test.png") # square patches

color_mix(img_spec1=path1, img_spec2=path2,alpha_channels=[1,1],output_path="test-colorchannels.png",
    num_rows=2) 
