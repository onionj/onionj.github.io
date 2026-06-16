
update:
	git add .
	git commit -m "update"
	git push origin gh-pages

setup:
	sudo apt-get update
	sudo apt-get install -y pandoc texlive-xetex fonts-liberation fontconfig
	sudo fc-cache -f
	pip install pypandoc pyyaml python-docx

pdf:
	python3 create_pdf_from_website.py

ats_pdf:
	python3 create_pdf_from_md.py

docx:
	python3 build_docx.py

all: ats_pdf docx
