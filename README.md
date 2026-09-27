# Harsha Vardhini S — Portfolio

A single-page, zero-dependency portfolio site. No build step, no framework, no npm install.

**Live:** <https://harshavardhini255.github.io/portfolio/>

## Run it

Double-click `index.html`, or serve it locally (recommended, so scroll behaviour and fonts behave normally):

```bash
python -m http.server 8000
```

Then open <http://localhost:8000>.

## Deploy

Edit anything you like, then run one command. It stages, commits, pushes, waits for the GitHub Actions run, and prints the live URL:

```powershell
.\deploy.ps1                      # commit message: "Update portfolio"
.\deploy.ps1 "Tweak hero copy"     # or supply your own
```

To see what will be published first:

```bash
git status
git diff
```

Deploys run automatically on every push to `main` via `.github/workflows/pages.yml` — you can also trigger one by hand from the Actions tab. The workflow publishes only `index.html` and `assets/`, so this README and the workflow file stay out of the site.

> Note: `deploy.ps1` is deliberately ASCII-only. Windows PowerShell 5.1 reads BOM-less `.ps1` files as ANSI, so a UTF-8 em-dash silently corrupts parsing and the script exits early. Keep the file ASCII, or add a UTF-8 BOM if you add non-ASCII text.

## Deploy

Static files only — push the folder to GitHub Pages, Netlify, Vercel, Cloudflare Pages or any static host. There is nothing to compile.

## Structure

```
index.html          all markup and copy
work/*.html         one detail page per project (generated)
assets/styles.css   design tokens, layout, responsive rules, animations
assets/script.js    reveals, filters, accordion, counters, nav, mobile menu
assets/work.css     detail-page styles
assets/work.js      detail-page reveals, progress bar, prev/next
assets/portrait.jpg hero portrait
tools/site_data.py              project content for the detail pages
tools/build_work_pages.py      regenerates work/*.html from that data
deploy.ps1          one-command commit + push + deploy
```

## Project detail pages

Every card in **Work** opens its own page under `work/`, so each project has a URL you can share or put on a résumé. Each page has the overview, what was built, a results row, the stack and tags, a GitHub link where a public repo exists, and previous/next navigation.

Those pages are generated, so edit the data rather than the HTML:

```bash
python tools/build_work_pages.py
```

Change a title, a bullet, a metric or a repo URL in `tools/site_data.py`, re-run the command, then `.\deploy.ps1`. The generator writes the HTML into `work/`, which is committed to the repo — GitHub Pages just publishes the committed files, so nothing runs on GitHub's side.

To add a project, append a dict to `PROJECTS` in `tools/site_data.py` and re-run. Add the matching card to the `#workGrid` block in `index.html` by hand, and keep its `data-kind` equal to one of the filter ids.

## Editing content

Everything you will want to change lives in `index.html` as plain text:

| What | Where |
| --- | --- |
| Name, email, phone, GitHub, LinkedIn | hero aside, contact section, `menu` footer |
| Hero intro and the Focus/Method/Also-into rows | `section.hero` |
| Stat numbers (03 / 07 / 50K+ / 200+) | `section.hero .hero__stats` — `data-count`, `data-pad`, `data-suffix` |
| Marquee keywords | `words` array in `assets/script.js` |
| Projects | `section.work #workGrid` — `data-kind` must match a filter id |
| Filter tabs and their counts | `ul.filters` in `section.work` (update the `<sup>` counts by hand) |
| Capability accordion | `div#acc` |
| Experience | `div.tl` |
| Profile copy | `section.about` |
| Education, toolkit, certifications, interests | `section.cred` |
| Year in the footer | auto-filled from the current date by script |

## Colours

All colour lives in `:root` at the top of `assets/styles.css`:

```css
--paper:   #f4f2ed   page background
--paper-2: #ebe8e1   alternating section background
--ink:     #14110f   text, dark sections
--accent:  #b4552d   terracotta accent
--line:    #ded9d0   hairlines
```

Change `--accent` to re-tint the whole site.

## Notes

- Fonts load from Google Fonts (Instrument Serif, Inter, JetBrains Mono) and fall back to system serif/sans/mono if offline.
- `assets/portrait.jpg` is displayed in greyscale and goes full colour on hover.
- Honours `prefers-reduced-motion`: reveals, morphing portrait, marquee and counters all stand down.
- Project cards without a live link show a dimmed arrow and are not clickable.
