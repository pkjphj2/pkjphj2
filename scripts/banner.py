"""One-off generator for assets/banner.svg: two Kaplan-Meier curves, drawn in on load."""
import random, sys

W, H, L, R, T, B = 840, 150, 40, 40, 18, 28  # size and margins
TMAX = 10.0


def km(times, events):
    """Kaplan-Meier steps -> [(t, S)] plus censor points."""
    data = sorted(zip(times, events))
    n, s, steps, cens = len(data), 1.0, [(0.0, 1.0)], []
    for t, e in data:
        if t > TMAX:
            break
        if e:
            s *= (n - 1) / n
            steps.append((t, s))
        else:
            cens.append((t, s))
        n -= 1
    return steps, cens


def xy(t, s):
    return L + (W - L - R) * t / TMAX, T + (H - T - B) * (1 - s)


def path(steps):
    d, prev = [], None
    for t, s in steps:
        x, y = xy(t, s)
        d.append(f"M{x:.1f} {y:.1f}" if prev is None else f"H{x:.1f} V{y:.1f}")
        prev = y
    return " ".join(d) + f" H{W - R}"


def group(rate, n, seed):
    rnd = random.Random(seed)
    times = [rnd.expovariate(rate) for _ in range(n)]
    cens = [rnd.uniform(0, 14) for _ in range(n)]
    return km([min(a, c) for a, c in zip(times, cens)], [a <= c for a, c in zip(times, cens)])


def svg():
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="100%" '
           f'font-family="Segoe UI,Helvetica,Arial,sans-serif" font-size="12" fill="none">',
           '<style>.c{stroke-dasharray:2000;stroke-dashoffset:2000;animation:d 2.4s ease-out forwards}'
           '@keyframes d{to{stroke-dashoffset:0}}.k{opacity:0;animation:f .6s 2s forwards}@keyframes f{to{opacity:1}}</style>',
           f'<path d="M{L} {T} V{H - B} H{W - R}" stroke="#8b949e" stroke-opacity=".6"/>',
           f'<text x="{L - 8}" y="{T + 4}" fill="#8b949e" text-anchor="end">1</text>',
           f'<text x="{L - 8}" y="{H - B + 4}" fill="#8b949e" text-anchor="end">0</text>',
           f'<text x="{W - R}" y="{H - 8}" fill="#8b949e" text-anchor="end">time</text>']
    for (steps, cens), col in ((group(0.08, 60, 7), "#198CE7"), (group(0.22, 60, 11), "#e8a24a")):
        out.append(f'<path class="c" d="{path(steps)}" stroke="{col}" stroke-width="2.2"/>')
        for t, s in cens:
            x, y = xy(t, s)
            out.append(f'<path class="k" d="M{x:.1f} {y - 4:.1f} V{y + 4:.1f}" stroke="{col}" stroke-width="1.4"/>')
    out.append("</svg>")
    return "\n".join(out)


if __name__ == "__main__":
    steps, _ = km([1, 2, 3, 4], [1, 0, 1, 1])
    assert [round(s, 3) for _, s in steps] == [1, 0.75, 0.375, 0.0], steps
    with open(sys.argv[1], "w", encoding="utf-8") as f:
        f.write(svg())
    print("ok")
