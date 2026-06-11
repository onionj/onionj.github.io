import yaml
import pypandoc

# Load config and markdown content
with open("_config.yml") as config_file, open("index.md") as md_file:
    configs = yaml.load(config_file, Loader=yaml.FullLoader)
    body = md_file.read()

# Build header
header = f"# {configs['full_name']}\n"

links = []
if configs["github"]:
    links.append(f"[**Github**: {configs['github_url'].removeprefix('https://')}]({configs['github_url']})")
if configs["gmail"]:
    links.append(f"[**Email**: {configs['gmail_url']}](mailto:{configs['gmail_url']})")
if configs["linkedin"]:
    links.append(
        f"[**LinkedIn**: {configs['linkedin_url'].removeprefix('https://')}]({configs['linkedin_url']})"
    )
if configs["phone"]:
    links.append(
        f"[**Phone**: {configs['phone_number']}](tel:{configs['phone_number']})"
    )

header += " | ".join(links)

# PDF conversion options
extra_args = [
    "--pdf-engine=xelatex",
    "-V",
    "geometry:paperwidth=255mm",
    "-V",
    "geometry:paperheight=440mm",
    "-V",
    "geometry:top=.5in,bottom=.5in,left=0.6in,right=0.6in",
    "-V",
    "fontsize=14pt",
    "-V",
    "mainfont=Liberation Sans",
    "-V",
    "fontsize=11pt",
    "-V",
    "pagestyle=empty",
    "-V",
    "documentclass=article",
    "-V",
    "linkcolor=blue",
    "-V",
    "urlcolor=blue",
]

file_name = f"{configs['full_name'].replace(' ', '_').lower()}_cv.pdf"

# Convert Markdown to PDF
pypandoc.convert_text(
    header + "\n\n" + body,
    "pdf",
    outputfile=file_name,
    extra_args=extra_args,
    format="md",
)
