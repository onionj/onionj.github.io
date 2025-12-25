import pdfkit
import yaml

with open("_config.yml") as file:
    configs = yaml.load(file, Loader=yaml.FullLoader)

    URL = configs["URL"]

    options = {
        "page-height": "410",
        "page-width": "280",
        "margin-top": "0in",
        "margin-right": "0.3in",
        "margin-bottom": "0in",
        "margin-left": "0.3in",
    }
    pdfkit.from_url(URL, "cv.pdf", options=options, verbose=True)
