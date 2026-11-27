#!/usr/bin/env python3
"""Bookkeeping for a Zone Stalker run, so the status line is printed from a record and never from memory.
Standard-library Python only. State lives in zone-state.json in the current folder (or the path in ZONE_STATE).

  python state.py new --bolts 20 --flags 10 --lights 3 --cash 200       start a character's kit
  python state.py run 17:00 --turn 03:00 --dawn 06:42 --date "29 Nov"    declare a run (entry time, turn time, dawn)
  python state.py clock 17:26                 set the clock (24 h; it may pass midnight, never run backwards)
  python state.py bolts -3   | flags -1 | flags +20 | cash +650 | debt +200 | heat +2 | harm +1
  python state.py lamp 45                     burn 45 minutes of the lamp in use (each light lasts 360)
  python state.py carry "black sparks" [slots] [--who Dunn]    something takes a slot (default 1; two-handed = 2)
  python state.py drop "rope"                 stop carrying something
  python state.py worn "bracelet"             worn items are listed but take no slot
  python state.py rested                      a proper 10-minute rest: resets the unrested timer
  python state.py out                         the run is over (back outside the wire)
  python state.py status                      print the status line and any penalties now in force
  python state.py show                        print the whole record

Load: six slots. Bolts and flags share the belt (1 slot while you hold any), spare lights the chest (1 slot).
Harm takes one slot per point. Over four filled: movement takes twice as long and strain rolls are forced.
"""
import json, os, sys
P = os.environ.get('ZONE_STATE', 'zone-state.json')
LAMP_LIFE = 360


def load():
    return json.load(open(P)) if os.path.exists(P) else {}


def save(s):
    json.dump(s, open(P, 'w'), indent=1)


def mins(t):
    h, m = t.split(':'); return int(h) * 60 + int(m)


def slots(s, who='me'):
    n = sum(v['slots'] for v in s.get('carried', {}).values() if v['who'] == who)
    if who == 'me':
        n += (1 if s.get('bolts', 0) or s.get('flags', 0) else 0) + (1 if s.get('lights') else 0) + s.get('harm', 0)
    return n


def elapsed(s, key):
    """Minutes from s[key] to the clock, allowing one midnight."""
    if not s.get(key) or not s.get('clock'): return 0
    d = mins(s['clock']) - mins(s[key])
    return d + 1440 if d < 0 else d


def status(s):
    lights = s.get('lights', [])
    good = sum(1 for m in lights if m > 0)
    out = []
    if s.get('in_run'):
        line = '%s, in since %s, turn time %s, dawn %s | Load %d/6 | Bolts %d | Flags %d | Light %d of %d' % (
            s['clock'], s['entry'], s['turn'], s['dawn'], slots(s), s.get('bolts', 0), s.get('flags', 0), good, len(lights))
    else:
        line = '%s | Cash %d | Debt %d | Heat %d, Wanted %d' % (s.get('date', ''), s.get('cash', 0), s.get('debt', 0), s.get('heat', 0), s.get('wanted', 0))
    out.append(line)
    if s.get('in_run'):
        pen = []
        over = elapsed(s, 'turn') if mins(s['clock']) != mins(s['turn']) and elapsed(s, 'turn') < 720 else 0
        if over > 0: pen.append('past turn time by %d min: -%d on every roll' % (over, 1 + over // 60))
        un = elapsed(s, 'rested_at')
        if un > 40: pen.append('no proper rest for %d min: -1 Hands and Eyes' % un)
        if slots(s) > 4: pen.append('loaded (%d slots): movement takes twice as long; strain is a roll' % slots(s))
        if lights and lights[0] <= 30 and lights[0] > 0: pen.append('lamp in use has %d min left' % lights[0])
        if good == 0 and lights: pen.append('NO LIGHT LEFT')
        for w in sorted({v['who'] for v in s.get('carried', {}).values()} - {'me'}):
            if slots(s, w) > 4: pen.append('%s is loaded (%d slots)' % (w, slots(s, w)))
        if pen: out.append('IN FORCE (apply these; do not just mention them): ' + '; '.join(pen))
    c = s.get('carried', {})
    if c: out.append('Carried: ' + ', '.join('%s (%s, %d)' % (k, v['who'], v['slots']) for k, v in c.items()))
    if s.get('worn'): out.append('Worn: ' + ', '.join(s['worn']))
    return '\n'.join(out)


def main(a):
    s = load()
    if not a or a[0] in ('-h', '--help'): print(__doc__); return
    c = a[0]
    opt = lambda k, d=None: a[a.index(k) + 1] if k in a else d
    if c == 'new':
        s = {'bolts': int(opt('--bolts', 20)), 'flags': int(opt('--flags', 10)), 'lights': [LAMP_LIFE] * int(opt('--lights', 3)),
             'cash': int(opt('--cash', 200)), 'debt': 0, 'heat': 0, 'wanted': 0, 'harm': 0, 'carried': {}, 'worn': [], 'in_run': False, 'date': opt('--date', '')}
    elif c == 'run':
        s.update(in_run=True, entry=a[1], clock=a[1], turn=opt('--turn'), dawn=opt('--dawn'), rested_at=a[1], date=opt('--date', s.get('date', '')))
    elif c == 'clock':
        if s.get('in_run') and elapsed(dict(s, clock=a[1]), 'entry') < elapsed(s, 'entry'): sys.exit('refused: the clock cannot run backwards')
        s['clock'] = a[1]
    elif c in ('bolts', 'flags', 'cash', 'debt', 'heat', 'harm', 'wanted'):
        s[c] = s.get(c, 0) + int(a[1]) if a[1][0] in '+-' else int(a[1])
        if s[c] < 0: sys.exit('refused: %s would go below zero' % c)
    elif c == 'lamp':
        left = int(a[1])
        while left > 0 and any(m > 0 for m in s['lights']):
            i = next(i for i, m in enumerate(s['lights']) if m > 0)
            use = min(left, s['lights'][i]); s['lights'][i] -= use; left -= use
        s['lights'].sort(key=lambda m: (m == 0, m))            # the part-used lamp is the one in use
    elif c == 'carry':
        n = int(a[2]) if len(a) > 2 and a[2].isdigit() else 1
        s.setdefault('carried', {})[a[1]] = {'slots': n, 'who': opt('--who', 'me')}
    elif c == 'drop': s.get('carried', {}).pop(a[1], None)
    elif c == 'worn': s.setdefault('worn', []).append(a[1]); s.get('carried', {}).pop(a[1], None)
    elif c == 'rested': s['rested_at'] = s.get('clock')
    elif c == 'out': s['in_run'] = False
    elif c == 'show': print(json.dumps(s, indent=1)); return
    elif c != 'status': print(__doc__); return
    save(s); print(status(s))


if __name__ == '__main__':
    main(sys.argv[1:])
