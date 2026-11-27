# Afton Zone map data

Public map data for a tabletop game set on Afton Mountain at Rockfish Gap, Virginia. Nothing here is secret: it is the real ground, in the game's grid.

| Path | What it is |
| --- | --- |
| `skill/SKILL.md` | The game master's rules |
| `skill/terrain.py`, `skill/terrain.bin` | Terrain lookup from USGS lidar at 10 m: `python terrain.py at F9-57` |
| `skill/features.bin` | Road, track, stream and building positions for `python terrain.py near F9-57` |
| `skill/state.py` | Run bookkeeping: clock, load, lights, status line |
| `skill/gazetteer.md` | Named places, roads, railway, tunnels and streams by grid square |
| `atlas/afton-mountain-field-atlas.pdf` | Field atlas for an e-ink tablet: index map and 36 linked sheets |
| `map/` | Zoomable web map with three base layers |

Grid: 250 m squares, A to X west to east, 1 to 24 south to north, centred on the gap (38.0315 N, 78.8578 W). A reference such as M12-37 adds tenths east and north.

Data: USGS 3DEP lidar, USGS Historical Topographic Map Collection (Waynesboro East and West, 1973), USDA NAIP imagery, all public domain; named features from OpenStreetMap contributors (ODbL). A game aid: fiction only.
