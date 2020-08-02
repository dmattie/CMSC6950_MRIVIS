report.pdf: collage.png carpet.png Report.tex
	python demo-carpet.py nifti

T1sample.nii:
	cp mrivis/example_datasets/3569_bl_PPMI_smoothed.nii ./T1sample.nii

4Dsample.nii:
	cp mrivis/example_datasets/epi_func.nii ./4Dsample.nii

collage.png: T1sample.nii demo-collage.py
	python demo-collage.py T1sample.nii

carpet.png: 4Dsample.nii demo-carpet.py
	python demo-carpet.py 4Dsample.nii

.PHONY: clean

clean: 
	rm -f *.nii
	rm -f *.png
	rm -f *.pdf
	rm -f *.log
	rm -f *.aux

almost_clean:
	latexmk -c
