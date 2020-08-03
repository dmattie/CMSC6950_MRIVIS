# CMSC6950_MRIVIS
Medical image visualization library for neuroscience

JOSS Paper: https://joss.theoj.org/papers/10.21105/joss.00897 

# Installation instructions

Create a virtual environment

```
python -m venv ~/environments/CMSC6950_mrivis  
source ~/environments/CMSC6950_mrivis/bin/activate
```
The dependencies to execute the code can be found in requirements.txt.  
Install them as follows:

```
pip install -r requirements.txt
```

# Make and run

To create the report, simply type ```make``` in the installation directory.

To exeriment with the demo, use the following commands:

```
python demo-collage.py [path-to-nii-file]
python demo-carpet.py [path-to-4D-nii-file]

```