#!/usr/bin/env python3
"""Fetch the player's atlas pen marks, as published to the private mailbox by his own machine.
Standard-library Python only.

  python mailbox.py notes            download the current marked pages into ./notes/ and list them
  python mailbox.py notes --changed  only pages whose marks changed at the last sync

Needs the access key: the environment variable ZONE_KEY, or a file .zone-key beside this script
(the seed skill writes it). Without a key this prints NO KEY and exits; the game runs without it.
Never print the key. The pages are the player's own handwriting on his map: read them, do not correct them.
"""
import json, os, sys, urllib.request
HERE = os.path.dirname(os.path.abspath(__file__))
BASE = 'https://raw.githubusercontent.com/trevorgdobson/zone-stalker-rpg/mailbox/'


def key():
    k = os.environ.get('ZONE_KEY', '').strip()
    p = os.path.join(HERE, '.zone-key')
    if not k and os.path.exists(p): k = open(p).read().strip()
    return k if k and 'PASTE' not in k else ''


def get(path):
    r = urllib.request.Request(BASE + path, headers={'Authorization': 'token ' + key()})
    return urllib.request.urlopen(r, timeout=60).read()


def notes(changed_only=False):
    if not key(): print('NO KEY: atlas notes are not available in this chat. Ask the player to attach a marked page instead.'); return
    try: idx = json.loads(get('notes/index.json'))
    except Exception as e: print('NOTES UNAVAILABLE (%s). Ask the player to attach a marked page instead.' % e); return
    os.makedirs('notes', exist_ok=True)
    print('Atlas marks as last synced at %s (the atlas was last changed on the tablet at %s).' % (idx.get('synced', '?'), idx.get('atlas_modified', '?')))
    print('If the player has written since then, these are stale: say so and ask.')
    for p in idx.get('pages', []):
        if changed_only and not p.get('changed'): continue
        out = os.path.join('notes', p['file']); open(out, 'wb').write(get('notes/' + p['file']))
        print('PAGE %s  %s  %s  -> %s' % (p['page'], p['what'], 'changed' if p.get('changed') else 'same', out))
    print('Open each image to read it. Red strokes are the pen marks; the rest is the printed sheet.')


if __name__ == '__main__':
    a = sys.argv[1:]
    if a and a[0] == 'notes': notes('--changed' in a)
    else: print(__doc__)
