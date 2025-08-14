
update:
	git add .
	git commit -m "update"
	git push origin gh-pages

pdf:
	sudo apt install -y wkhtmltopdf
	pip install pdfkit pyyaml
	python3 create_pdf.py

ats_pdf:
	sudo apt-get install pandoc
	pip install pypandoc
	sudo apt install texlive-xetex
	sudo apt install ttf-mscorefonts-installer fontconfig
	python3 create_pdf_from_md.py
