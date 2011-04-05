
THESIS = thesis

pdf: $(THESIS).pdf 

view: pdf
	evince $(THESIS).pdf


$(THESIS).pdf: *.tex 
	for number in 1 2 ; do \
		pdflatex $(THESIS).tex; \
	done


clean:
	@rm -f *.log *.aux *.dvi *.bbl *.blg *.ilg *.toc *.lof *.lot *.idx *.ind *.out *.brf *.html *.btmp *.itmp *.rerun *.glo *.gls

%.bbl: %.aux
	bibtex $(THESIS)

%.aux: %.tex
		pdflatex $(THESIS).tex

#%.ind: %.tex %.aux
#	makeindex $(THESIS)

