
## Template for creating resume with GitHub pages


### What is GitHub Pages?

GitHub Pages is a simple service to publish a website directly on GitHub from a Git repository. You add some files and folders to a repository and GitHub Pages turns it into a website. See [GitHub Pages Documentation](https://docs.github.com/en/pages/quickstart)


Example resume created by this template (my resume): [onionj.github.io](https://onionj.github.io)
### content and configs:
Edit `_config.yml` and `index.md` and `cv/index.html` file.

### publish in github:
Run `make update` or run:\
`git add .` \
`git commit -m "update"` \
`git push origin gh-pages` \


### create pdf:
Run `make pd` or run:\
`pip3 install pdfkit pyyaml` \
`python3 create_pdf.py`

