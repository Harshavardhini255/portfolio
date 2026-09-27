"""
Renders one detail page per project into work/.

Edit tools/site_data.py, then run:

    python tools/build_work_pages.py

Output is committed to the repo, so GitHub Pages publishes the generated
HTML. Nothing runs at build time on GitHub's side.
"""

import html
import os

from site_data import PROJECTS

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT, "work")

E = lambda s: html.escape(s, quote=True)

ARROW = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 17 17 7M9 7h8v8"/></svg>'


def chips(items, cls):
    return "\n".join('            <li>%s</li>' % E(i) for i in items)


def results_block(p):
    if not p["results"]:
        return ""
    cells = []
    for value, label in p["results"]:
        cells.append(
            '        <div class="res">\n'
            '          <span class="res__v">%s</span>\n'
            '          <span class="res__l">%s</span>\n'
            "        </div>" % (E(value), E(label))
        )
    note = (
        '\n        <p class="res__note">%s</p>' % E(p["result_note"])
        if p["result_note"]
        else ""
    )
    return (
        '      <section class="blk">\n'
        '        <h2 class="blk__h">Results</h2>\n'
        '        <div class="res__grid">\n%s\n%s\n        </div>%s\n'
        "      </section>" % ("\n".join(cells), "", note)
    )


def actions_block(p):
    if p["href"]:
        return (
            '          <a class="btn btn--solid" href="%s" target="_blank" rel="noopener">'
            "View on GitHub %s</a>" % (E(p["href"]), ARROW)
        )
    return (
        '          <span class="nolink">Source available on request</span>'
    )


def render(p, prev_p, next_p):
    others = [x for x in (prev_p, next_p) if x]

    if prev_p:
        prev_html = (
            '        <a class="pn__link pn__link--prev" href="%s.html">'
            '<span class="pn__dir">Previous</span>'
            '<span class="pn__title">%s</span></a>' % (E(prev_p["slug"]), E(prev_p["title"]))
        )
    else:
        prev_html = '        <span class="pn__link pn__link--off"></span>'

    if next_p:
        next_html = (
            '        <a class="pn__link pn__link--next" href="%s.html">'
            '<span class="pn__dir">Next</span>'
            '<span class="pn__title">%s</span></a>' % (E(next_p["slug"]), E(next_p["title"]))
        )
    else:
        next_html = '        <span class="pn__link pn__link--off"></span>'

    return """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{title} — Harsha Vardhini S</title>
<meta name="description" content="{desc}" />
<meta name="theme-color" content="#14110f" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Inter:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="../assets/styles.css" />
<link rel="stylesheet" href="../assets/work.css" />
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' fill='%2314110f'/%3E%3Ctext x='16' y='22' font-family='Georgia,serif' font-size='15' fill='%23f4f2ed' text-anchor='middle'%3EHV%3C/text%3E%3C/svg%3E" />
</head>
<body class="is-p">

<div class="grain" aria-hidden="true"></div>
<div class="progress" aria-hidden="true"><span id="progressBar"></span></div>

<header class="pnav">
  <div class="shell pnav__inner">
    <a class="pnav__back" href="../index.html#work">
      <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M15 7 8 12l7 5"/></svg>
      Work
    </a>
    <a class="pnav__brand" href="../index.html">Harsha Vardhini S</a>
  </div>
</header>

<main>

  <section class="phero">
    <div class="shell">
      <p class="phero__crumb"><span class="slash">/</span> Project {n}</p>
      <h1 class="phero__title">{title}</h1>
      <p class="phero__cat">{category} <span aria-hidden="true">&middot;</span> {year}</p>
      <ul class="chips">
{chips}
      </ul>
    </div>
  </section>

  <section class="pbody">
    <div class="shell pbody__grid">

      <aside class="pbody__side">
        <div class="pmeta">
          <p class="pmeta__h">Stack</p>
          <ul class="pmeta__list">
{stack_list}
          </ul>
        </div>
        <div class="pmeta">
          <p class="pmeta__h">Tags</p>
          <ul class="tags">
{tag_list}
          </ul>
        </div>
        <div class="pmeta pacts">
{actions}
        </div>
      </aside>

      <div class="pbody__main">

      <section class="blk">
        <h2 class="blk__h">Overview</h2>
        <p class="lede">{overview}</p>
      </section>

      <section class="blk">
        <h2 class="blk__h">What I built</h2>
        <ul class="ticks">
{built_list}
        </ul>
      </section>

{results}

      <div class="pn">
{prev}
{next}
      </div>

      </div>
    </div>
  </section>

</main>

<footer class="pfoot">
  <div class="shell pfoot__inner">
    <p>&copy; <span id="year">2026</span> Harsha Vardhini S</p>
    <a href="../index.html#contact">Get in touch {arrow}</a>
  </div>
</footer>

<script src="../assets/work.js"></script>
</body>
</html>
""".format(
        n=E(p["n"]),
        title=E(p["title"]),
        desc=E(p["overview"][:155] + ("..." if len(p["overview"]) > 155 else "")),
        category=E(p["category"]),
        year=E(p["year"]),
        chips=chips(p["stack"], "chips"),
        stack_list=chips(p["stack"], "stack"),
        tag_list=chips(p["tags"], "tags"),
        actions=actions_block(p),
        overview=E(p["overview"]),
        built_list="\n".join(
            '          <li>%s</li>' % E(b) for b in p["built"]
        ),
        results=results_block(p),
        prev=prev_html,
        next=next_html,
        arrow=ARROW,
    )


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    total = len(PROJECTS)
    for i, p in enumerate(PROJECTS):
        prev_p = PROJECTS[i - 1] if i > 0 else None
        next_p = PROJECTS[i + 1] if i < total - 1 else None
        path = os.path.join(OUT_DIR, p["slug"] + ".html")
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(render(p, prev_p, next_p))
        print("wrote", os.path.relpath(path, ROOT))


if __name__ == "__main__":
    main()
