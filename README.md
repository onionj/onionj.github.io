# Resume as code — GitHub Pages + PDF + Word

A single source of truth (`index.md` + `_config.yml`) that produces **three** outputs:

1. **Website** — published via GitHub Pages (Jekyll, Cayman theme). Live example: [onionj.github.io](https://onionj.github.io)
2. **ATS-friendly PDF** — single-column, generated from `index.md` with Pandoc + XeLaTeX.
3. **Word (.docx)** — ATS-friendly, generated from `index.md` with `python-docx`.

The PDF and Word files are regenerated **automatically by GitHub Actions** on every push that
changes the CV source, and committed back to the branch — so the download links on the site
always match the latest content.

## Edit your CV

- **Content:** edit [`index.md`](index.md).
- **Name, contact links, feature toggles:** edit [`_config.yml`](_config.yml)
  (`pdf`, `docx`, `github`, `linkedin`, `gmail`, `phone` flags and their URLs).

## Build locally

```bash
make setup    # install pandoc, xelatex, fonts, and Python deps (Debian/Ubuntu)
make all      # build both the ATS PDF and the Word file
```

Individual targets:

| Command          | Output                                   | Tooling                  |
|------------------|------------------------------------------|--------------------------|
| `make ats_pdf`   | `saman_nezafat_cv.pdf` (from `index.md`) | Pandoc + XeLaTeX         |
| `make docx`      | `saman_nezafat_cv.docx`                  | `python-docx`            |
| `make pdf`       | `cv.pdf` (rendered from the live site)   | pdfkit + wkhtmltopdf*    |
| `make update`    | commit & push everything to `gh-pages`   | git                      |

\* `make pdf` needs system `wkhtmltopdf` and is not used in CI.

## Automated build (CI)

[`.github/workflows/build-cv.yml`](.github/workflows/build-cv.yml) runs `make all` on GitHub's
runners whenever `index.md`, `_config.yml`, or the build scripts change on `gh-pages`
(or manually via *Run workflow*). It installs the toolchain, regenerates
`*_cv.pdf` and `*_cv.docx`, and commits them back. The bot commit is tagged `[skip ci]` and uses
the default token, so it does not trigger itself.

## Publish

```bash
make update
```

Or manually:

```bash
git add .
git commit -m "update"
git push origin gh-pages
```

GitHub Pages serves the site from the `gh-pages` branch.
