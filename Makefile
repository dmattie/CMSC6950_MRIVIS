report.pdf: collage.png carpet.png Report.tex
	latexmk -pdf   # [TODO] latexmk does'nt fit on my laptop!!!	

T1sample.nii:
	cp mrivis/example_datasets/3569_bl_PPMI_smoothed.nii ./T1sample.nii
	#curl https://url-to-nii.nii

4Dsample.nii:
	cp mrivis/example_datasets/epi_func.nii ./4Dsample.nii
	#curl https://url-to-nii.nii

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
	rm -f Report.f*

almost_clean:
	latexmk -c
	
