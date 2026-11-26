#!/usr/bin/env python3
"""Real ground for the Afton Mountain Zone, from USGS 1 m lidar resampled to 10 m. No secrets here.

Usage (standard-library Python only; terrain.bin must sit beside this file):
  python terrain.py at F9-57               elevation, slope, which way is downhill, landform
  python terrain.py line F9-21 F10-99      profile between two references, every 25 m
  python terrain.py line F9-21 021 480     profile from a reference along a true bearing for 480 m
  python terrain.py water F9-57            where water runs from here: the downhill path, 600 m
  python terrain.py square F9              3 x 3 spot heights (m) across one square, north at the top
  python terrain.py near F9-57 [radius]    mapped roads, tracks, railway, streams, power lines and buildings
                                           within radius metres (default 300), with distance and bearing

A reference names a 25 m cell; positions are taken at the centre of that cell.

Grid: 250 m squares A-X west to east, 1-24 south to north; M12-37 = 3 tenths east, 7 tenths north
of the south-west corner of M12. Bearings are true. Elevations in metres and feet.
ALWAYS check a position here before describing slope, crest, hollow, draw or creek at it.
"""
import os, sys, zlib, math, array
N = 600; PX = 10.0; E0 = -3000.0; N0 = -3000.0
_d = None


def _load():
    global _d
    if _d is None:
        a = array.array('h')
        a.frombytes(zlib.decompress(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'terrain.bin'), 'rb').read()))
        if sys.byteorder != 'little': a.byteswap()
        _d = a
    return _d


def h(e, n):
    """Elevation in metres at e, n (metres east and north of the gap), bilinear. Row 0 is the south edge."""
    d = _load(); x = min(max((e - E0) / PX - .5, 0), N - 1.001); y = min(max((n - N0) / PX - .5, 0), N - 1.001)
    x0 = int(x); y0 = int(y); fx = x - x0; fy = y - y0
    g = lambda i, j: d[j * N + i] / 10.0
    return (g(x0, y0) * (1 - fx) + g(x0 + 1, y0) * fx) * (1 - fy) + (g(x0, y0 + 1) * (1 - fx) + g(x0 + 1, y0 + 1) * fx) * fy


def pos(ref):
    ref = ref.strip().upper(); sq, _, t = ref.partition('-')
    c = ord(sq[0]) - 65; r = int(sq[1:]) - 1
    fe, fn = (int(t[0]) + .5, int(t[1]) + .5) if len(t) == 2 else (5.0, 5.0)
    return E0 + (c + fe / 10) * 250, N0 + (r + fn / 10) * 250


def ref(e, n):
    c = int((e - E0) // 250); r = int((n - N0) // 250)
    if not (0 <= c < 24 and 0 <= r < 24): return 'off grid'
    return '%s%d-%d%d' % (chr(65 + c), r + 1, int(((e - E0) / 250 - c) * 10), int(((n - N0) / 250 - r) * 10))


COMPASS = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']


def grad(e, n, s=20.0):
    dx = (h(e + s, n) - h(e - s, n)) / (2 * s); dy = (h(e, n + s) - h(e, n - s)) / (2 * s)
    return math.degrees(math.atan(math.hypot(dx, dy))), (math.degrees(math.atan2(-dx, -dy)) + 360) % 360


def landform(e, n):
    z = h(e, n)
    ring = [h(e + 60 * math.sin(math.radians(a)), n + 60 * math.cos(math.radians(a))) for a in range(0, 360, 30)]
    hi = sum(1 for v in ring if v > z + 1.5); lo = sum(1 for v in ring if v < z - 1.5); sl, _ = grad(e, n)
    opp = max(min(ring[i], ring[i + 6]) - z for i in range(6)); opn = max(z - max(ring[i], ring[i + 6]) for i in range(6))
    if lo >= 10: return 'summit or knoll'
    if hi >= 10: return 'hollow or pit'
    if opn > 2.5: return 'on a ridge or spur crest (ground falls away on two opposite sides)'
    if opp > 2.5: return 'in a draw or valley floor (ground rises on two opposite sides)'
    return 'flat ground' if sl < 3 else 'open slope (no crest or draw within 60 m)'


def at(e, n):
    z = h(e, n); sl, dn = grad(e, n)
    return '%s  %d m (%d ft)  slope %d deg  downhill toward %03d (%s)  uphill toward %03d  %s' % (
        ref(e, n), round(z), round(z * 3.28084), round(sl), round(dn) % 360, COMPASS[int((dn + 11.25) % 360 // 22.5)], round(dn + 180) % 360, landform(e, n))


def line(e, n, e2, n2):
    L = math.hypot(e2 - e, n2 - n); b = (math.degrees(math.atan2(e2 - e, n2 - n)) + 360) % 360; k = max(1, int(round(L / 25)))
    out = ['%s to %s: %d m on bearing %03d' % (ref(e, n), ref(e2, n2), round(L), round(b) % 360)]
    up = dn = 0.0; prev = None
    for i in range(k + 1):
        x = e + (e2 - e) * i / k; y = n + (n2 - n) * i / k; z = h(x, y); sl, d = grad(x, y)
        rel = (d - b + 540) % 360 - 180          # downhill direction relative to travel: + right, - left
        side = 'downhill ahead' if abs(rel) < 45 else 'downhill behind' if abs(rel) > 135 else 'downhill to the RIGHT' if rel > 0 else 'downhill to the LEFT'
        if prev is not None: up += max(z - prev, 0); dn += max(prev - z, 0)
        prev = z; lf = landform(x, y)
        out.append('  %4d m  %-7s %4d m  slope %2d  %s%s' % (round(L * i / k), ref(x, y), round(z), round(sl), side if sl >= 3 else 'near level', '' if lf.startswith(('open', 'flat')) else '  [' + lf.split(' (')[0] + ']'))
    out.append('  total climb %d m, total descent %d m' % (round(up), round(dn)))
    return '\n'.join(out)


def water(e, n, dist=600):
    out = ['Downhill path from %s (where water, or anything that pools, would run):' % ref(e, n)]; z0 = h(e, n); t = 0
    while t < dist:
        sl, d = grad(e, n, 10)
        if sl < 0.6:
            out.append('  %4d m  %-7s %4d m  levels out (pond, flat or sink)' % (t, ref(e, n), round(h(e, n)))); break
        e += 10 * math.sin(math.radians(d)); n += 10 * math.cos(math.radians(d)); t += 10
        if not (E0 < e < E0 + 6000 and N0 < n < N0 + 6000):
            out.append('  leaves the grid'); break
        if t % 50 == 0: out.append('  %4d m  %-7s %4d m  heading %03d  %s' % (t, ref(e, n), round(h(e, n)), round(d) % 360, landform(e, n).split(' (')[0]))
    out.append('  drop %d m' % round(z0 - h(e, n)))
    return '\n'.join(out)


def square(sq):
    sq = sq.upper(); out = [sq + ' spot heights in metres (north at top; west, middle, east):']
    for fn in (8, 5, 1):
        out.append('  ' + '  '.join('%4d' % round(h(*pos('%s-%d%d' % (sq, fe, fn)))) for fe in (1, 5, 8)))
    return '\n'.join(out)


def near(e, n, radius=300.0):
    """Mapped roads, tracks, railways, streams, power lines and buildings within radius metres (features.bin)."""
    import json
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'features.bin')
    if not os.path.exists(p): return 'features.bin not found beside terrain.py'
    f = json.loads(zlib.decompress(open(p, 'rb').read()).decode())
    best = {}
    for name, kind, g in f['lines']:
        for (x0, y0), (x1, y1) in zip(g, g[1:]):
            dx, dy = x1 - x0, y1 - y0; L2 = dx * dx + dy * dy
            t = 0.0 if L2 == 0 else max(0.0, min(1.0, ((e - x0) * dx + (n - y0) * dy) / L2))
            px, py = x0 + t * dx, y0 + t * dy; d = math.hypot(px - e, py - n)
            run = (math.degrees(math.atan2(dx, dy)) + 360) % 180
            key = (name, kind.split(' (')[0]) if name else ('', kind.split(' (')[0], round(px / 60), round(py / 60))
            if d <= radius and (key not in best or d < best[key][0]): best[key] = (d, px, py, name, kind, run)
    rows = [(d, '%4d m on %03d  %-7s %s%s, running %03d-%03d' % (round(d), round((math.degrees(math.atan2(px - e, py - n)) + 360) % 360) % 360, ref(px, py), name or 'unnamed', ' (' + kind + ')', round(run) % 180, (round(run) + 180) % 360))
            for d, px, py, name, kind, run in best.values()]
    for name, kind, x, y in f['points']:
        d = math.hypot(x - e, y - n)
        if d <= radius: rows.append((d, '%4d m on %03d  %-7s %s' % (round(d), round((math.degrees(math.atan2(x - e, y - n)) + 360) % 360) % 360, ref(x, y), (name + ' (building)') if name else 'building')))
    rows.sort()
    head = 'Mapped features within %d m of %s (distance, true bearing to the nearest point, its reference). As mapped today; unmapped paths may exist.' % (radius, ref(e, n))
    return head + '\n' + ('\n'.join('  ' + r for _, r in rows[:40]) if rows else '  none')


if __name__ == '__main__':
    a = sys.argv[1:]
    if not a or a[0] in ('-h', '--help'): print(__doc__)
    elif a[0] == 'at': print('\n'.join(at(*pos(r)) for r in a[1:]))
    elif a[0] == 'line':
        e, n = pos(a[1])
        if len(a) == 4:
            b = math.radians(float(a[2])); e2, n2 = e + float(a[3]) * math.sin(b), n + float(a[3]) * math.cos(b)
        else: e2, n2 = pos(a[2])
        print(line(e, n, e2, n2))
    elif a[0] == 'water': print(water(*pos(a[1])))
    elif a[0] == 'square': print(square(a[1]))
    elif a[0] == 'near': print(near(*pos(a[1]), radius=float(a[2]) if len(a) > 2 else 300.0))
    else: print(__doc__)
