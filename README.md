# Zone Stalker: maps and rules

Public files for *Zone Stalker*, a one-player tabletop RPG run by an AI game master, after *Roadside Picnic*. Each Zone sits on a real mountain, and the game master answers from real ground. Nothing here is secret: the hidden rules are not in this repository.

**Want to play?** Read [PLAY.md](PLAY.md). You need a starter message or a guest pack from whoever invited you.

| Zone | Where | Field atlas | Web map |
| --- | --- | --- | --- |
| `afton` | Afton Mountain at Rockfish Gap, Virginia | [PDF](https://trevorgdobson.github.io/afton-zone-map/zones/afton/atlas/afton-mountain-field-atlas.pdf) | [open](https://trevorgdobson.github.io/afton-zone-map/zones/afton/map/) |
| `rila` | The Seven Rila Lakes, Bulgaria | [PDF, in Bulgarian](https://trevorgdobson.github.io/afton-zone-map/zones/rila/atlas/rila-seven-lakes-field-atlas.pdf) | not yet |
| `mantasoa` | Lac de Mantasoa, Madagascar. The Zone is the lake and its shore | [PDF, in French](https://trevorgdobson.github.io/afton-zone-map/zones/mantasoa/atlas/lac-de-mantasoa-atlas-de-terrain.pdf) | not yet |

| Path | What it is |
| --- | --- |
| `skills/zone-stalker-rpg/` | The game master's rules (`SKILL.md`), terrain lookup (`terrain.py`), run bookkeeping (`state.py`) |
| `zones/<zone>/` | `zone.md` (the place), `gazetteer.md`, `terrain.bin` and `features.bin` for the terrain tool, the atlas and the web map |
| `skill/` | An older flat copy of the Afton files, kept so earlier instructions still work |

Afton and Rila use a grid of 250 m squares, A to X west to east and 1 to 24 south to north, centred on a named point; Mantasoa uses 500 m squares, A to P and 1 to 28. A reference such as M12-37 adds tenths east and north.

Data: USGS 3DEP lidar, USGS Historical Topographic Map Collection and USDA NAIP imagery (public domain); Copernicus GLO-30 elevation; ESA WorldCover land cover (CC BY 4.0); named features from OpenStreetMap contributors (ODbL). A game about real places: fiction only, and nobody should enter real derelict or private property because of it.
