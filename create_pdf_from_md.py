import yaml
import pypandoc

# Load config and markdown content
with open("_config.yml") as config_file, open("index.md") as md_file:
    configs = yaml.load(config_file, Loader=yaml.FullLoader)
    body = md_file.read()

# Build header
header = f"# {configs['full_name']}\n\n"
header += "**Senior Backend Engineer | Tech Lead**\n\n"

links = []
if configs["gmail"]:
    links.append(f"[**Email**: {configs['gmail_url']}](mailto:{configs['gmail_url']})")
if configs["phone"]:
    phone_digits = "".join(c for c in configs['phone_number'].split()[0] if c.isdigit())
    wa_url = f"https://wa.me/{phone_digits}"
    links.append(
        f"[**WhatsApp**: {configs['phone_number'].split()[0]}]({wa_url})"
    )
if configs["linkedin"]:
    links.append(
        f"[**LinkedIn**: {configs['linkedin_url'].removeprefix('https://www.').removeprefix('https://')}]({configs['linkedin_url']})"
    )
if configs["github"]:
    links.append(f"[**Github**: {configs['github_url'].removeprefix('https://')}]({configs['github_url']})")

header += " | ".join(links)

# PDF conversion options
extra_args = [
    "--pdf-engine=xelatex",
    # Heading hierarchy: company names must stand out from project names.
    "--include-in-header=header.tex",
    "-V", "geometry:a4paper",
    "-V", "geometry:top=1.5cm,bottom=1.5cm,left=1.5cm,right=1.5cm",
    "-V", "mainfont=Liberation Sans",
    "-V", "fontsize=10pt",
    "-V", "pagestyle=empty",
    "-V", "documentclass=article",
    # Link colours are set to the accent colour in header.tex.
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
