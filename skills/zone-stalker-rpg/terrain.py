#!/usr/bin/env python3
"""Real ground for a Zone, from packed elevation data (10 m cells; 20 m in mantasoa). No secrets here.

Usage (standard-library Python only). Zone data is read from zones/<zone>/ beside this file (terrain.bin,
features.bin, zone.json). Choose the zone with --zone NAME first on the line, or the ZONE environment variable;
the default is afton:   python terrain.py --zone rila at M12-55
  python terrain.py at F9-57               elevation, slope, which way is downhill, landform
  python terrain.py line F9-21 F10-99      profile between two references, every 25 m
  python terrain.py line F9-21 021 480     profile from a reference along a true bearing for 480 m
  python terrain.py water F9-57            where water runs from here: the downhill path, 600 m
  python terrain.py square F9              3 x 3 spot heights (m) across one square, north at the top
  python terrain.py near F9-57 [radius]    mapped roads, tracks, railway, streams, power lines and buildings
                                           within radius metres (default 300), with distance and bearing;
                                           the 40 nearest are listed (mantasoa: then every named one in the radius)

A reference names one cell, a tenth of a square each way; positions are taken at the centre of that cell.

Grid: squares lettered west to east and numbered south to north; M12-37 = 3 tenths east, 7 tenths north
of the south-west corner of M12. afton and rila: 250 m squares A-X, 1-24, so a tenth is 25 m.
mantasoa: 500 m squares A-P, 1-28, so a tenth is 50 m. Bearings are true. Elevations in metres and feet.
ALWAYS check a position here before describing slope, crest, hollow, draw or creek at it.

Where the Zone is a lake and its shore (mantasoa), `at` ends with where the point lies and how far the mapped
waterline is, and `line` marks every step and totals the stretches:
  WATER       on the lake as mapped: inside the Zone. The height is the lake surface; no depths are known.
  SHORE BAND  dry land within 100 m of the mapped waterline: inside the Zone.
  ISLAND      on one of the lake's islands: inside the Zone, all of it.
  LAND        more than 100 m from the mapped waterline: outside the Zone.
The waterline is the shore as mapped; the real one moves with the lake level (see that zone's zone.md).
`near` lists the lake shore once for each compass direction it lies in, so both sides of a point or an arm show.
"""
import os, sys, zlib, math, array
NX = NY = 600; PX = 10.0; E0 = -3000.0; N0 = -3000.0; SQ = 250.0; NSX = NSY = 24
MASK = None                                 # zone.json zone.mask when the Zone is a lake and its shore, else None
NEAR_B = None                               # zone.json near.buildings: list this many buildings singly, then count the rest
CODES = ('LAND', 'SHORE BAND', 'WATER', 'ISLAND')
HERE = os.path.dirname(os.path.abspath(__file__))
ZONE = os.environ.get('ZONE', 'afton')
ZDIR = HERE
_d = None; _m = None; _f = None


def use_zone(name):
    """Point the tool at zones/<name>/ (beside this file, or two levels up in the repository)."""
    global ZONE, ZDIR, NX, NY, PX, E0, N0, SQ, NSX, NSY, MASK, NEAR_B, _d, _m, _f
    import json
    ZONE = name; _d = _m = _f = None; MASK = NEAR_B = None
    for base in (HERE, os.path.join(HERE, '..', '..')):
        d = os.path.join(base, 'zones', name)
        if os.path.exists(os.path.join(d, 'terrain.bin')):
            ZDIR = d; break
    else:
        if os.path.exists(os.path.join(HERE, 'terrain.bin')): ZDIR = HERE          # old flat layout: data beside the script
        else: sys.exit('zone "%s" not found: no zones/%s/terrain.bin beside terrain.py' % (name, name))
    zj = os.path.join(ZDIR, 'zone.json')
    if os.path.exists(zj):
        z = json.load(open(zj, encoding='utf-8')); g = z['grid']; t = z['terrain']
        SQ = float(g['size']); NSX = int(g.get('nx', g.get('n'))); NSY = int(g.get('ny', g.get('n')))
        NX = int(t.get('nx', t.get('n'))); NY = int(t.get('ny', t.get('n'))); PX = float(t['px'])
        MASK = (z.get('zone') or {}).get('mask'); NEAR_B = (z.get('near') or {}).get('buildings')
    E0 = -SQ * NSX / 2; N0 = -SQ * NSY / 2


def _load():
    global _d
    if _d is None:
        a = array.array('h')
        a.frombytes(zlib.decompress(open(os.path.join(ZDIR, 'terrain.bin'), 'rb').read()))
        if sys.byteorder != 'little': a.byteswap()
        _d = a
    return _d


def h(e, n):
    """Elevation in metres at e, n (metres east and north of the gap), bilinear. Row 0 is the south edge."""
    d = _load(); x = min(max((e - E0) / PX - .5, 0), NX - 1.001); y = min(max((n - N0) / PX - .5, 0), NY - 1.001)
    x0 = int(x); y0 = int(y); fx = x - x0; fy = y - y0
    g = lambda i, j: d[j * NX + i] / 10.0
    return (g(x0, y0) * (1 - fx) + g(x0 + 1, y0) * fx) * (1 - fy) + (g(x0, y0 + 1) * (1 - fx) + g(x0 + 1, y0 + 1) * fx) * fy


def pos(ref):
    ref = ref.strip().upper(); sq, _, t = ref.partition('-')
    c = ord(sq[0]) - 65; r = int(sq[1:]) - 1
    fe, fn = (int(t[0]) + .5, int(t[1]) + .5) if len(t) == 2 else (5.0, 5.0)
    return E0 + (c + fe / 10) * SQ, N0 + (r + fn / 10) * SQ


def ref(e, n):
    c = int((e - E0) // SQ); r = int((n - N0) // SQ)
    if not (0 <= c < NSX and 0 <= r < NSY): return 'off grid'
    return '%s%d-%d%d' % (chr(65 + c), r + 1, int(((e - E0) / SQ - c) * 10), int(((n - N0) / SQ - r) * 10))


def _feat():
    global _f
    if _f is None:
        import json
        p = os.path.join(ZDIR, 'features.bin')
        _f = json.loads(zlib.decompress(open(p, 'rb').read()).decode()) if os.path.exists(p) else {}
    return _f


def code(e, n):
    """0 land, 1 shore band, 2 water, 3 island at e, n, from the zone's mask file; None where the zone has no mask or off it."""
    global _m
    if not MASK: return None
    if _m is None: _m = zlib.decompress(open(os.path.join(ZDIR, MASK['file']), 'rb').read())
    i = int((e - E0) // MASK['px']); j = int((n - N0) // MASK['px'])
    return _m[j * MASK['nx'] + i] if 0 <= i < MASK['nx'] and 0 <= j < MASK['ny'] else None


def shore(e, n):
    """(metres, bearing) to the nearest point of the mapped waterline of the lake (its shore or an island's), or None."""
    best = None
    for name, kind, g in _feat().get('lines', []):
        if kind not in ('lake shore', 'island shore'): continue
        for (x0, y0), (x1, y1) in zip(g, g[1:]):
            dx, dy = x1 - x0, y1 - y0; L2 = dx * dx + dy * dy
            t = 0.0 if L2 == 0 else max(0.0, min(1.0, ((e - x0) * dx + (n - y0) * dy) / L2))
            px, py = x0 + t * dx, y0 + t * dy; d = (px - e) ** 2 + (py - n) ** 2
            if best is None or d < best[0]: best = (d, px, py)
    if best is None: return None
    return math.sqrt(best[0]), (math.degrees(math.atan2(best[1] - e, best[2] - n)) + 360) % 360


def where(e, n):
    """For a lake zone: which of water, shore band, island or land the point is, and how far the mapped waterline lies."""
    c = code(e, n)
    if c is None: return ''
    s = shore(e, n); what = CODES[c] + (' (outside the Zone)' if c == 0 else ' (in the Zone)')
    if s is None: return what
    return '%s: %s %d m away on %03d' % (what, 'nearest shore' if c == 2 else 'waterline', round(s[0]), round(s[1]) % 360)


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
    if code(e, n) == 2: return '%s  %d m (%d ft)  the lake surface  %s' % (ref(e, n), round(z), round(z * 3.28084), where(e, n))
    return '%s  %d m (%d ft)  slope %d deg  downhill toward %03d (%s)  uphill toward %03d  %s' % (
        ref(e, n), round(z), round(z * 3.28084), round(sl), round(dn) % 360, COMPASS[int((dn + 11.25) % 360 // 22.5)], round(dn + 180) % 360, landform(e, n)) + \
        ('  ' + where(e, n) if MASK else '')


def line(e, n, e2, n2):
    L = math.hypot(e2 - e, n2 - n); b = (math.degrees(math.atan2(e2 - e, n2 - n)) + 360) % 360; k = max(1, int(round(L / 25)))
    out = ['%s to %s: %d m on bearing %03d' % (ref(e, n), ref(e2, n2), round(L), round(b) % 360)]
    up = dn = 0.0; prev = None; runs = []
    for i in range(k + 1):
        x = e + (e2 - e) * i / k; y = n + (n2 - n) * i / k; z = h(x, y); sl, d = grad(x, y)
        rel = (d - b + 540) % 360 - 180          # downhill direction relative to travel: + right, - left
        side = 'downhill ahead' if abs(rel) < 45 else 'downhill behind' if abs(rel) > 135 else 'downhill to the RIGHT' if rel > 0 else 'downhill to the LEFT'
        if prev is not None: up += max(z - prev, 0); dn += max(prev - z, 0)
        prev = z; lf = landform(x, y)
        if MASK:
            c = code(x, y); c = 0 if c is None else c
            if runs and runs[-1][0] == c: runs[-1][2] = L * i / k
            else: runs.append([c, L * i / k, L * i / k])
            out.append('  %4d m  %-7s %4d m  %-10s  %s' % (round(L * i / k), ref(x, y), round(z), CODES[c].lower(), 'lake surface' if c == 2 else 'slope %2d  %s%s' % (
                round(sl), side if sl >= 3 else 'near level', '' if lf.startswith(('open', 'flat')) else '  [' + lf.split(' (')[0] + ']')))
            continue
        out.append('  %4d m  %-7s %4d m  slope %2d  %s%s' % (round(L * i / k), ref(x, y), round(z), round(sl), side if sl >= 3 else 'near level', '' if lf.startswith(('open', 'flat')) else '  [' + lf.split(' (')[0] + ']'))
    out.append('  total climb %d m, total descent %d m' % (round(up), round(dn)))
    if MASK:
        st = L / k; out.append('  along the line: ' + ', '.join('%s %d-%d m' % (CODES[c].lower(), round(max(a - st / 2, 0)), round(min(b + st / 2, L))) for c, a, b in runs))
        wet = sum(min(b + st / 2, L) - max(a - st / 2, 0) for c, a, b in runs if c == 2)
        out.append('  on the water %d m of %d m; in the Zone (water, shore band, island) %d m' % (round(wet), round(L), round(sum(min(b + st / 2, L) - max(a - st / 2, 0) for c, a, b in runs if c))))
    return '\n'.join(out)


def water(e, n, dist=600):
    out = ['Downhill path from %s (where water, or anything that pools, would run):' % ref(e, n)]; z0 = h(e, n); t = 0
    while t < dist:
        sl, d = grad(e, n, 10)
        if sl < 0.6:
            out.append('  %4d m  %-7s %4d m  levels out (pond, flat or sink)' % (t, ref(e, n), round(h(e, n)))); break
        e += 10 * math.sin(math.radians(d)); n += 10 * math.cos(math.radians(d)); t += 10
        if not (E0 < e < E0 + SQ * NSX and N0 < n < N0 + SQ * NSY):
            out.append('  leaves the grid'); break
        if code(e, n) == 2:
            out.append('  %4d m  %-7s %4d m  reaches the lake' % (t, ref(e, n), round(h(e, n)))); break
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
    f = _feat()
    if not f: return 'features.bin not found beside terrain.py'
    best = {}
    for name, kind, g in f['lines']:
        for (x0, y0), (x1, y1) in zip(g, g[1:]):
            dx, dy = x1 - x0, y1 - y0; L2 = dx * dx + dy * dy
            t = 0.0 if L2 == 0 else max(0.0, min(1.0, ((e - x0) * dx + (n - y0) * dy) / L2))
            px, py = x0 + t * dx, y0 + t * dy; d = math.hypot(px - e, py - n)
            run = (math.degrees(math.atan2(dx, dy)) + 360) % 180
            key = (name, kind.split(' (')[0]) if name else ('', kind.split(' (')[0], round(px / 60), round(py / 60))
            if MASK and kind.endswith('shore'): key = (name, kind, int((math.degrees(math.atan2(px - e, py - n)) + 382.5) % 360 // 45))      # once per compass octant
            if d <= radius and (key not in best or d < best[key][0]): best[key] = (d, px, py, name, kind, run)
    rows = [(d, '%4d m on %03d  %-7s %s%s, running %03d-%03d' % (round(d), round((math.degrees(math.atan2(px - e, py - n)) + 360) % 360) % 360, ref(px, py), name or 'unnamed', ' (' + kind + ')', round(run) % 180, (round(run) + 180) % 360))
            for d, px, py, name, kind, run in best.values()]
    nb = 0; more = []
    for name, kind, x, y in f['points']:
        d = math.hypot(x - e, y - n)
        if NEAR_B and d <= radius and kind == 'building' and not name: more.append((d, x, y))
        elif d <= radius: rows.append((d, '%4d m on %03d  %-7s %s' % (round(d), round((math.degrees(math.atan2(x - e, y - n)) + 360) % 360) % 360, ref(x, y), (name + ' (' + kind + ')') if name else kind)))
    more.sort()
    for d, x, y in more[:NEAR_B or 0]: rows.append((d, '%4d m on %03d  %-7s building' % (round(d), round((math.degrees(math.atan2(x - e, y - n)) + 360) % 360) % 360, ref(x, y))))
    rows.sort(); tail = ''
    if more[NEAR_B or 0:]: tail += '\n  and %d more buildings within %d m (%d listed, nearest first); see the atlas sheet for their pattern' % (len(more) - NEAR_B, radius, NEAR_B)
    far = f.get('far_buildings', {}).get(ref(e, n).split('-')[0])
    if far: tail += '\n  plus %d buildings in square %s more than %d m from the water, counted but not listed singly' % (far, ref(e, n).split('-')[0], f.get('far_m', 0))
    if MASK: tail += '\n  ' + (where(e, n) or 'off the grid')
    head = 'Mapped features within %d m of %s (distance, true bearing to the nearest point, its reference). As mapped today; unmapped paths may exist.' % (radius, ref(e, n))
    if NEAR_B and len(rows) > 40:                             # past the 40 nearest, still list every named place and line in the radius
        named = [r for r in rows[40:] if ' unnamed (' not in r[1] and not r[1].endswith(' building')][:30]
        if named: tail = '\n  farther off, named only:\n' + '\n'.join('  ' + r for _, r in named) + tail
    return head + '\n' + ('\n'.join('  ' + r for _, r in rows[:40]) if rows else '  none') + tail


if __name__ == '__main__':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except Exception: pass
    a = sys.argv[1:]
    if a[:1] == ['--zone'] and len(a) > 1: ZONE = a[1]; a = a[2:]
    if a and a[0] not in ('-h', '--help'): use_zone(ZONE)
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
