# CMSC6950_MRIVIS
Medical image visualization library for neuroscience

JOSS Paper: https://joss.theoj.org/papers/10.21105/joss.00897 

# Installation instructions

Check to see if your environment is good to go:

```
./envtest.sh
```

If not, start here: Create a virtual environment

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
python demo-collage.py {path-to-nii-file | URL-to-nii }
python demo-carpet.py [path-to-4D-nii-file]

```

In addition, Make can take a parameter for the source Nifti files:

See the following to examples:

```
make_example.sh
make_example_uri.sh
```