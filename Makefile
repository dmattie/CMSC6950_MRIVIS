report.pdf: collage.png carpet.png Report.tex
    python demo-carpet.py nifti

T1sample.nii
    cp mrivis/example_datasets/3569_bl_PPMI_smoothed.nii ./T1sample.nii

4Dsample.nii
    cp mrivis/example_datasets/epi_func.nii ./4Dsample.nii

collage.png:T1sample.nii demo-collage.py
    python demo-collage.py T1sample.nii

carpet.png:4Dsample.nii demo-carpet.py
    python demo-carpet.py 4Dsample.nii

.PHONE: clean almost_clean

clean: %almost_clean
    rm report.pdf
    rm T1sample.nii
    rm 4Dsample.nii
    rm collage.png
    rm carpet.png

almost_clean:
    latexmk -c
