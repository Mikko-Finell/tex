name := test
figures := figure_1.pdf

all: $(name).pdf
	
$(name).pdf: $(name).tex $(figures) $(name).bbl
	pdflatex $(name)
	
figure_1.pdf: script_1.py
	python3 $< $@

$(name).bbl: $(name).bib
	pdflatex $(name) && bibtex $(name) && pdflatex $(name)

clean:
	rm -rf $(name).pdf
	rm -rf $(figures)
	rm -rf $(wildcard *.aux *.bbl *.blg *.log *.out *.toc)
