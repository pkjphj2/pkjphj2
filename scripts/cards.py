"""Profile cards.

python scripts/cards.py gecko   # GitHub Actions: gecko eats the contribution grid -> assets/gecko.svg
python scripts/cards.py langs   # run locally with gh (sees private repos) -> assets/langs.svg
"""
import json, os, subprocess, sys, urllib.request
from collections import Counter

USER = "pkjphj2"
OUT = os.path.join(os.path.dirname(__file__), "..", "assets")
LEVEL = {"NONE": 0, "FIRST_QUARTILE": 1, "SECOND_QUARTILE": 2, "THIRD_QUARTILE": 3, "FOURTH_QUARTILE": 4}
GREEN = ["#ebedf0", "#9be9a8", "#40c463", "#30a14e", "#216e39"]
EATEN = "#ebedf0"
CELL, GAP, PAD = 11, 3, 20
STEP = CELL + GAP


def calendar():
    q = '{user(login:"%s"){contributionsCollection{contributionCalendar{weeks{contributionDays{contributionLevel weekday}}}}}}' % USER
    req = urllib.request.Request("https://api.github.com/graphql", json.dumps({"query": q}).encode(),
                                 {"Authorization": "bearer " + os.environ["GITHUB_TOKEN"]})
    weeks = json.load(urllib.request.urlopen(req))["data"]["user"]["contributionsCollection"]["contributionCalendar"]["weeks"]
    return [[(d["weekday"], LEVEL[d["contributionLevel"]]) for d in w["contributionDays"]] for w in weeks]


def serpentine(weeks):
    """Cells in walking order: down column 0, up column 1, ... -> [(x, y, level)]."""
    out = []
    for c, days in enumerate(weeks):
        days = sorted(days, reverse=c % 2 == 1)
        out += [(PAD + c * STEP, PAD + wd * STEP, lv) for wd, lv in days]
    return out


GECKO = """<g>MOTION
 <path d="M-9 0 Q-20 -4 -24 3 Q-20 7 -9 3Z" fill="#c9762b"/>
 <g stroke="#a85f1f" stroke-width="2.2" stroke-linecap="round">
  <path d="M3 -4 L7 -10"><animate attributeName="d" values="M3 -4 L7 -10;M3 -4 L1 -10;M3 -4 L7 -10" dur="0.4s" repeatCount="indefinite"/></path>
  <path d="M3 4 L7 10"><animate attributeName="d" values="M3 4 L1 10;M3 4 L7 10;M3 4 L1 10" dur="0.4s" repeatCount="indefinite"/></path>
  <path d="M-6 -4 L-10 -10"><animate attributeName="d" values="M-6 -4 L-2 -10;M-6 -4 L-10 -10;M-6 -4 L-2 -10" dur="0.4s" repeatCount="indefinite"/></path>
  <path d="M-6 4 L-10 10"><animate attributeName="d" values="M-6 4 L-10 10;M-6 4 L-2 10;M-6 4 L-10 10" dur="0.4s" repeatCount="indefinite"/></path>
 </g>
 <ellipse cx="-1" cy="0" rx="10" ry="5.5" fill="#e8a24a"/>
 <path d="M-6 -5 V5 M-1 -5.5 V5.5" stroke="#8a4b16" stroke-width="1.6"/>
 <ellipse cx="11" cy="0" rx="5.5" ry="4.5" fill="#e8a24a"/>
 <circle cx="13" cy="-2.6" r="1.4" fill="#222"/><circle cx="13" cy="2.6" r="1.4" fill="#222"/>
</g>"""

# 두부: chubby white Maltese, top view facing +x, trotting behind 콩이
DUBU = """<g>MOTION
 <g stroke="#d6d6d6" stroke-width="1" fill="#fff">
  <circle cx="-13" cy="0" r="3.5"/>
  <ellipse cx="-1" cy="0" rx="12" ry="9"><animate attributeName="ry" values="9;8.3;9" dur="0.4s" repeatCount="indefinite"/></ellipse>
  <ellipse cx="11" cy="-6" rx="3.5" ry="4.5"/><ellipse cx="11" cy="6" rx="3.5" ry="4.5"/>
  <circle cx="13" cy="0" r="6.5"/>
 </g>
 <circle cx="15" cy="-2.6" r="1.2" fill="#222"/><circle cx="15" cy="2.6" r="1.2" fill="#222"/>
 <circle cx="19.2" cy="0" r="1.5" fill="#222"/>
</g>"""


def gecko_svg(cells, dur=24.0, walk=0.9, lag=0.06):
    w = max(x for x, _, _ in cells) + CELL + PAD
    h = PAD * 2 + 7 * STEP - GAP
    # gecko moves at constant speed, so a cell is reached at its share of the path length
    dist = [0.0]
    for (x0, y0, _), (x1, y1, _) in zip(cells, cells[1:]):
        dist.append(dist[-1] + ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5)
    rects = []
    for i, (x, y, lv) in enumerate(cells):
        rect = f'<rect x="{x}" y="{y}" width="{CELL}" height="{CELL}" rx="2" fill="{GREEN[lv]}"'
        if not lv:
            rects.append(rect + "/>")
            continue
        t = round(walk * dist[i] / dist[-1], 4)
        t2 = min(round(t + 0.002, 4), 0.999)
        # colour stays until the gecko reaches the cell, then it is eaten; resets each loop
        rects.append(f'{rect}><animate attributeName="fill" values="{GREEN[lv]};{GREEN[lv]};{EATEN};{EATEN}" '
                     f'keyTimes="0;{t};{t2};1" dur="{dur}s" repeatCount="indefinite"/></rect>')
    path = "M" + " L".join(f"{x + CELL / 2} {y + CELL / 2}" for x, y, _ in cells)
    # 두부 waits `lag` of the loop, then follows the same path; drawn first so 콩이 stays on top
    dubu = f'<animateMotion path="{path}" rotate="auto" keyPoints="0;0;1;1" keyTimes="0;{lag};{walk + lag};1" calcMode="linear" dur="{dur}s" repeatCount="indefinite"/>'
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">
{chr(10).join(rects)}
{DUBU.replace("MOTION", dubu)}
{GECKO.replace("MOTION", f'<animateMotion path="{path}" rotate="auto" keyPoints="0;1;1" keyTimes="0;{walk};1" calcMode="linear" dur="{dur}s" repeatCount="indefinite"/>')}
</svg>"""


LANG_COLORS = {"R": "#198CE7", "TypeScript": "#7b61ff", "Python": "#e9b949", "JavaScript": "#f1e05a",
               "HTML": "#e34c26", "Swift": "#F05138", "CSS": "#563d7c", "Shell": "#89e051"}


def langs_svg(top):
    total = sum(v for _, v in top)
    w, x, bar, legend = 360, 20, [], []
    for i, (name, v) in enumerate(top):
        pw = (w - 40) * v / total
        col = LANG_COLORS.get(name, "#8b949e")
        bar.append(f'<rect x="{x:.1f}" y="44" width="{pw:.1f}" height="10" fill="{col}"/>')
        x += pw
        lx, ly = 20 + (i % 2) * 165, 78 + (i // 2) * 22
        legend.append(f'<circle cx="{lx + 5}" cy="{ly - 4}" r="5" fill="{col}"/>'
                      f'<text x="{lx + 16}" y="{ly}">{name} {100 * v / total:.1f}%</text>')
    h = 78 + ((len(top) + 1) // 2) * 22
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" font-family="Segoe UI,Helvetica,Arial,sans-serif" font-size="12">
<rect x="0.5" y="0.5" width="{w - 1}" height="{h - 1}" rx="6" fill="#fffefe" stroke="#e4e2e2"/>
<text x="20" y="28" font-size="15" font-weight="600" fill="#2f80ed">Most Used Languages</text>
<clipPath id="r"><rect x="20" y="44" width="{w - 40}" height="10" rx="5"/></clipPath>
<g clip-path="url(#r)">{''.join(bar)}</g>
<g fill="#434d58">{''.join(legend)}</g>
</svg>"""


def repo_languages():
    """Bytes per language over all owned, non-fork repos (private included)."""
    gh = lambda *a: json.loads(subprocess.run(["gh", *a], capture_output=True, text=True, check=True).stdout)
    total = Counter()
    for r in gh("repo", "list", USER, "--limit", "200", "--source", "--json", "name"):
        total.update(gh("api", f"repos/{USER}/{r['name']}/languages"))
    return total


def write(name, svg):
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(svg)


if __name__ == "__main__":
    if sys.argv[1:] == ["gecko"]:
        write("gecko.svg", gecko_svg(serpentine(calendar())))
    elif sys.argv[1:] == ["langs"]:
        langs = repo_languages()
        for hidden in ("HTML", "CSS", "JavaScript"):  # markup bloats byte counts; JS left out by choice
            langs.pop(hidden, None)
        write("langs.svg", langs_svg(langs.most_common(6)))
    elif sys.argv[1:] == ["test"]:
        cells = serpentine([[(0, 1), (1, 0)], [(0, 0), (1, 2)]])
        assert [(c[0], c[1]) for c in cells] == [(20, 20), (20, 34), (34, 34), (34, 20)], cells
        svg = gecko_svg(cells)
        assert svg.count("<animate attributeName=\"fill\"") == 2 and svg.count("<animateMotion") == 2
        assert "100.0%" in langs_svg([("R", 5)])
        print("ok")
    else:
        sys.exit(__doc__)
