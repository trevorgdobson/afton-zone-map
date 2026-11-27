# Lac de Mantasoa gazetteer

Real ground for the game master, in the atlas grid (500 m squares, A to P west to east, 1 to 28 south to north;
a reference such as H14-37 adds tenths east and north, each tenth being 50 m; the centre, the corner of H, I, 14 and 15, is a knoll on the shore about 100 m from the water: only the middle of the lake's bounding box, of no importance on the ground).
Sheet numbers are those of the player's atlas: 28 sheets of 4 by 4 squares, sheet 1 at the north-west, reading across.
This file holds no game secrets. It describes the real place as mapped today: in the fiction, anything inside the
Zone has had decades of neglect. Use it so that shores, slopes, roads, tracks, streams and buildings are where the
player's atlas shows them. It is not a list of what is in the Zone. All heights and distances are in metres.
Names are exactly as the player's atlas prints them: Malagasy and French as mapped in OpenStreetMap.
The shore, and so the edge of the Zone, is the waterline as mapped: the real one moves with the lake level (see zone.md).

Sources: terrain from Copernicus GLO-30 DEM (30 m, 1 arc-second, a radar surface model), cubic-resampled to 20 m; shore, named places and lines from OpenStreetMap contributors (ODbL); land cover from ESA WorldCover 10 m 2021 v200 with mapped rice fields and marsh from OpenStreetMap over it.
The elevation model's true resolution is 30 m: slopes are averaged over that distance, so short steps, crags and gullies are smoothed away and real slopes are locally steeper than the table says.

## The lake

Lac de Mantasoa as mapped in OpenStreetMap (relation 1154835; its Malagasy name there is Tobindranon’i Mantasoa).
The Zone is this water, its islands, and the shore band: dry land within 100 m of the mapped waterline.

- **Extent:** 7.3 km west to east (A10-64 to P10-37) by 12.2 km south to north (I2-07 to K27-12).
- **Area:** water 15.8 km2, islands 0.65 km2, shore band 18.2 km2: the Zone is 34.7 km2 in all.
- **Shoreline:** 209 km of mainland shore and 9.6 km round the islands, as mapped.
- **Surface:** 1385 m above sea level in the elevation model, flat to within 0.1 m. That is the level on the day the radar flew, not a fixed one.
- **Depths:** none. There is no bathymetry in any of the data. Do not quote a depth from this file or from the tool.
- **Open water:** the point farthest from any shore is E12-14, 360 m from land. Nowhere on the lake is farther from a shore than that.
- **Names:** OpenStreetMap names no arm, bay or point of the lake and none of its islands. Refer to them by grid reference.

### Islands

All of each island is inside the Zone. Top is the highest reading of the elevation model on the island: it includes trees.
Gap is the narrowest mapped water between the island and the mainland shore.

| Island (unnamed) | Centre | Sheet | Size | Area | Top, model m | Gap |
|---|---|---|---|---|---|---|
| island | E9-68 | 18 | 810 x 1200 m | 39.6 ha | 1428 | 20 m |
| island | J19-82 | 11 | 450 x 300 m | 10.0 ha | 1418 | 60 m |
| island | H11-51 | 18 | 450 x 460 m | 7.6 ha | 1401 | 90 m |
| island | J14-24 | 15 | 400 x 300 m | 5.3 ha | 1400 | 20 m |
| island | I13-83 | 15 | 180 x 140 m | 1.0 ha | 1392 | 10 m |

Separate waters mapped inside the shore band (ponds and cut-off arms; not part of the lake as mapped, but ground of the Zone where they lie within the band): G23-70 (6.9 ha), F21-61 (2.0 ha), G26-92 (1.6 ha), H26-75 (0.5 ha), H22-16 (0.1 ha), H25-92 (0.1 ha).

### Dams

As mapped (`waterway=dam`); none is named in OpenStreetMap. Length is the longer side of the mapped structure; crest is the elevation model along it.

| Dam | Centre | Sheet | Length | Crest, model m | Ground below, model m |
|---|---|---|---|---|---|
| dam | B13-80 | 13 | 160 m | 1386 | 1383 |
| dam | M14-97 | 16 | 80 m | 1386 | 1385 |
| dam | J27-20 | 3 | 190 m | 1386 | 1378 |

Named rivers on or beside the grid: Anjozoro, Varahina Nord.

### Landing places

Where a mapped road or track comes to within 15 m of the mapped waterline: 37 places. A boat can be put in or taken out
at any of them without crossing open country; so can a patrol. Footpaths are not listed one by one: 42 mapped paths also reach the water.
OpenStreetMap marks 7 landing stages (`amenity=ferry_terminal`); they are listed first.

| Ref | Sheet | Way | What |
|---|---|---|---|
| D17-61 | 9 | landing stage | mapped landing stage |
| G17-02 | 10 | landing stage | mapped landing stage |
| G17-23 | 10 | landing stage | mapped landing stage |
| G18-77 | 10 | landing stage | mapped landing stage |
| H19-44 | 10 | landing stage | mapped landing stage |
| I19-44 | 11 | landing stage | mapped landing stage |
| J19-42 | 11 | landing stage | mapped landing stage |
| H25-78 | 2 | minor road | touches the water in passing |
| K25-12 | 3 | minor road | ends at the water |
| H22-27 | 6 | minor road | ends at the water |
| H23-90 | 6 | track | ends at the water |
| H24-32 | 6 | track | ends at the water |
| H24-60 | 6 | track | ends at the water |
| I21-14 | 7 | minor road | touches the water in passing |
| I24-15 | 7 | minor road | touches the water in passing |
| I24-95 | 7 | minor road | runs along the water for about 300 m, I24-56 to I24-93 |
| F20-76 | 10 | service road | ends at the water |
| H17-84 | 10 | track | ends at the water |
| H19-89 | 10 | service road | touches the water in passing |
| I18-02 | 11 | service road | touches the water in passing |
| I19-44 | 11 | minor road | ends at the water |
| K19-64 | 11 | track | ends at the water |
| B13-92 | 13 | minor road | is mapped across 55 m of water (bridge, causeway or dam) |
| D13-05 | 13 | minor road | touches the water in passing |
| F16-07 | 14 | minor road | ends at the water |
| F16-50 | 14 | minor road | touches the water in passing |
| F16-73 | 14 | minor road | touches the water in passing |
| O14-26 | 16 | track | ends at the water |
| O15-37 | 16 | track | ends at the water |
| C11-82 | 17 | track | ends at the water |
| D9-47 | 17 | track | touches the water in passing |
| E10-62 | 18 | minor road | touches the water in passing |
| E11-78 | 18 | minor road | touches the water in passing |
| E9-04 | 18 | minor road | is mapped across 40 m of water (bridge, causeway or dam) |
| N11-87 | 20 | track | ends at the water |
| P10-28 | 20 | track | ends at the water |
| I5-91 | 23 | track | ends at the water |
| K6-70 | 23 | track | touches the water in passing |
| K7-83 | 23 | track | ends at the water |
| K7-96 | 23 | track | ends at the water |
| K8-52 | 23 | track | ends at the water |
| L6-17 | 23 | track | is mapped across 20 m of water (bridge, causeway or dam) |
| I2-07 | 27 | track | ends at the water |
| I3-64 | 27 | track | ends at the water |

## Off the grid

Named places within 1300 m outside the grid edge. They have no grid reference and are on no numbered sheet; the index map shows those to the west.
`terrain.py near` lists them from a reference near the edge with a wide radius.

- Fanantenana (hotel): 110 m W of A14
- Mantasoa Market (market): 120 m W of A14
- Mantasoa Post Office (post office): 150 m W of A14
- Ambohipeno (hamlet): 170 m W of A1
- Ampamaha (hamlet): 190 m W of A11
- Mantasoa (village): 220 m W of A14
- Mairie Mantasoa (town hall): 220 m W of A14
- Andranobe (hamlet): 230 m E of P21
- Ancienne résidence de Jean Laborde à Mantasoa (historic house): 270 m W of A15
- OTIV Fivoarana (bank): 380 m W of A15
- Jesosy Mamonjy (shelter): 410 m W of A15
- Tomate Lucie (shelter): 420 m W of A15
- Atsinanan'Lazaina (hamlet): 420 m W of A12
- Tsarahonenana (hamlet): 440 m E of P25
- Ambohimahatakatra (quarter): 450 m W of A14
- Villa Filadelfia - Centre (building): 500 m W of A11
- Ampanataovana (hamlet): 560 m N of D28
- Mahitsitady (hamlet): 570 m N of G28
- Ambohiborimanga (hamlet): 580 m W of A28
- FJKM Masombahiny (church): 630 m W of A13
- Masombahiny (village): 650 m W of A13
- Domaine Jean-Laborde (attraction): 760 m W of A14
- Andobo (hamlet): 760 m W of A19
- Ambohimanjaka (hamlet): 780 m S of E1
- CSB2 Mantasoa (health post): 810 m W of A14
- Ancienne fabrique de canons (ruins): 840 m W of A14
- Amboarakely (hamlet): 860 m N of J28
- Mantasoa Lycee Technique (quarter): 880 m W of A14
- Jean-Laborde Foundry (ruins): 940 m W of A14
- Ancien haut fourneau de Jean Laborde (ruins): 940 m W of A14
- Ankatsaka (hamlet): 970 m S of G1
- Mahafandriana (hamlet): 1230 m W of A10
- Ambohidronono (hamlet): 1240 m N of D28

## Named places

- Amboarapoitra (place=hamlet): C21-73
- Ambohibato (place=hamlet): D28-98
- Ambohidrahazo (place=hamlet): C15-71
- Ampasipotsy (place=hamlet): J26-56
- Ampiasanomby (place=neighbourhood): B14-06
- Andrefanivorona (place=hamlet): A6-97
- Anjozoro (place=village): C19-82
- Ankadirano (place=hamlet): E1-18
- Antsahamaina (place=village): C25-64
- Borne fontaine (man made=water well): A14-56
- Brigade Gendarmerie Mantasoa (amenity=police): C14-92
- Fanongoavana (historic=archaeological site): C3-07
- Hôtel L'Ermitage Mantasoa (amenity=restaurant): D17-57
- la Pointe (point of land): I25-26
- Lac de Mantasoa (lake): H14-55
- Madera (place=hamlet): B17-77
- Mantasoa Lodge (tourism=hotel): H17-13
- Marotanora (place=hamlet): C26-74
- US PEACE-CORPS Training Center Mantasoa (amenity=school): D13-12

## Roads, trails, streams and lines

Each entry lists every square the feature touches, sorted west to east then south to north (not in running order):
follow it from square to adjoining square. Lengths count only the part on the grid. Almost nothing here is named: use `terrain.py near` and the atlas sheet for the roads, tracks and paths at a given spot. Also mapped but unnamed: path 244.3 km, minor road 150.1 km, track 116.7 km, stream 18.3 km, service road 16.9 km, road 12.5 km, river 6.1 km, dam 0.7 km.

- Anjozoro (river, 8670 m on the grid): A14 A15 A16 A17 B17 B18 B21 C18 C19 C20 C21 C22 C23 C24 D24 D25 D26 D27 D28 E27

## Terrain by square

One row per square, north row first. Columns: square; per cent of the square that is water, shore band (with islands) and land outside the Zone;
mean elevation m; relief within the square m; mean slope degrees; the way the ground faces (downhill direction); buildings mapped today;
land cover (the commonest, plus a second if it fills a quarter of the square: wood, scrub, grass, crop, rice, built, rock, marsh, water; - is unmapped);
and features: R road, r minor or service road, t track or trail, w stream or river, l lake shore, d dam, s mapped landing stage.
A square that is all water reads the lake surface, no relief and no slope: that is the top of the water, not the bottom.
Buildings: 4474 are mapped on the grid. `terrain.py near` lists singly those within 400 m of the waterline and only counts the other 2819.
Slopes: under 8 easy walking, 8 to 20 steep, over 20 hands-and-feet in places. 
Cover over the whole grid: wood 45%, grass 18%, water 15%, scrub 12%, rice 8%, crop 2%, marsh 1%.

```
A28 0 0 100 1400 60 14 SW 31 rice+scrub t
B28 0 0 100 1450 120 16 SW 0 wood+scrub t
C28 0 0 100 1460 130 17 E 0 wood t
D28 0 0 100 1400 50 11 SE 43 rice+wood rtw
E28 0 0 100 1410 60 12 flat 38 scrub rt
F28 0 0 100 1390 40 8 S 2 rice rtw
G28 0 0 100 1400 40 11 W 45 rice rtw
H28 0 0 100 1410 50 13 E 0 wood+scrub rt
I28 0 0 100 1390 40 10 flat 0 wood t
J28 0 0 100 1390 50 7 W 24 grass+wood Rlrtw
K28 0 0 100 1410 70 11 S 0 grass+scrub rt
L28 0 0 100 1410 60 11 flat 0 grass+wood rt
M28 0 0 100 1410 80 12 flat 2 wood+grass rt
N28 0 0 100 1370 130 18 NE 0 wood+scrub t
O28 0 0 100 1330 130 20 NW 4 wood+scrub t
P28 0 0 100 1330 120 21 NE 0 scrub+wood t
A27 0 0 100 1410 60 13 N 3 wood+scrub rt
B27 0 0 100 1430 80 15 NW 6 wood+scrub lrt
C27 0 0 100 1410 70 13 SE 4 wood+rice rt
D27 0 0 100 1390 40 8 E 88 rice rtw
E27 0 0 100 1390 40 8 flat 83 rice+scrub rtw
F27 0 0 100 1390 30 8 N 17 wood+rice tw
G27 0 0 100 1400 50 10 W 0 wood Rt
H27 0 0 100 1420 60 13 NW 9 wood+grass Rrt
I27 0 0 100 1400 70 9 E 4 wood Rlrtw
J27 0 10 90 1390 40 7 W 4 wood+grass Rdrtw
K27 7 28 65 1400 40 10 flat 0 wood+scrub lrt
L27 0 2 98 1410 60 12 flat 0 wood rt
M27 0 0 100 1400 70 10 S 5 wood+grass rt
N27 0 0 100 1380 80 14 E 3 wood+scrub rt
O27 0 0 100 1370 90 16 N 0 wood+scrub rt
P27 0 0 100 1350 100 18 E 3 scrub+wood rt
A26 0 0 100 1420 70 15 flat 0 wood+grass t
B26 0 0 100 1420 80 16 S 4 wood+scrub lt
C26 0 0 100 1400 60 9 SE 92 rice rt
D26 0 0 100 1390 20 5 flat 69 rice rtw
E26 0 0 100 1390 30 7 flat 63 rice rtw
F26 0 0 100 1400 50 10 flat 28 wood+rice rt
G26 0 6 94 1400 40 12 flat 2 wood Rlr
H26 26 52 22 1390 40 9 S 30 wood+water lrt
I26 4 35 61 1410 50 9 SE 7 wood Rdlrtw
J26 59 29 12 1390 30 3 flat 12 water+grass Rdlrtw
K26 29 49 22 1400 50 8 W 0 wood+water lrt
L26 9 25 66 1400 50 9 flat 0 wood lrt
M26 0 0 100 1400 60 9 N 1 grass+wood rt
N26 0 0 100 1390 50 11 NE 0 grass+wood rt
O26 0 0 100 1380 80 15 S 1 wood rt
P26 0 0 100 1350 120 19 E 1 wood+scrub rt
A25 0 0 100 1400 50 13 N 0 scrub+wood t
B25 0 0 100 1410 60 15 flat 55 scrub rt
C25 0 0 100 1400 50 11 E 180 rice rt
D25 0 0 100 1380 30 4 flat 49 rice rtw
E25 0 0 100 1400 50 12 W 115 scrub rtw
F25 0 0 100 1420 60 14 flat 0 grass+wood rt
G25 0 0 100 1410 50 12 NW 0 scrub+wood Rlrt
H25 15 49 36 1400 40 9 NE 26 wood+grass lrt
I25 38 46 16 1390 40 7 N 17 water+wood lrt
J25 84 16 0 1390 10 1 flat 0 water lrt
K25 22 68 10 1390 30 9 flat 7 wood lrt
L25 35 35 30 1390 40 6 W 0 grass+water lt
M25 0 0 100 1420 70 12 flat 7 wood+grass t
N25 0 0 100 1400 70 12 E 2 wood rt
O25 0 0 100 1370 80 15 E 0 wood rt
P25 0 0 100 1340 90 17 E 6 wood rt
A24 0 0 100 1420 50 13 flat 0 scrub+wood rt
B24 0 0 100 1410 60 16 flat 21 scrub+wood rt
C24 0 0 100 1390 60 9 E 11 rice+scrub tw
D24 0 0 100 1400 60 10 NW 74 rice+scrub rtw
E24 0 0 100 1400 60 12 NW 8 rice+wood tw
F24 0 0 100 1410 50 12 flat 9 wood t
G24 0 0 100 1420 60 12 flat 0 grass+wood Rrt
H24 9 36 55 1400 40 10 S 43 grass lrt
I24 15 43 42 1410 50 11 NE 8 grass lrt
J24 45 39 16 1400 40 7 N 12 water+wood lrt
K24 73 26 1 1390 30 2 flat 2 water lt
L24 17 46 37 1400 50 9 flat 3 grass lt
M24 0 0 100 1410 40 9 flat 0 wood t
N24 0 0 100 1390 110 17 SE 0 wood t
O24 0 0 100 1340 80 16 SE 1 wood t
P24 0 0 100 1330 80 19 SW 0 wood rt
A23 0 0 100 1410 40 12 flat 10 wood rt
B23 0 0 100 1400 50 12 E 102 rice rt
C23 0 0 100 1390 40 7 flat 17 rice tw
D23 0 0 100 1400 50 12 flat 1 scrub+wood rt
E23 0 0 100 1410 60 13 N 0 scrub+wood t
F23 0 0 100 1400 40 12 flat 4 wood Rlt
G23 0 0 100 1400 60 11 S 15 grass Rlrt
H23 14 39 47 1400 40 10 flat 4 grass lrt
I23 4 37 59 1410 50 11 SW 44 grass+wood lrt
J23 32 43 25 1400 50 9 E 56 wood+water lrt
K23 79 20 1 1390 30 2 flat 1 water l
L23 18 30 52 1400 40 11 NW 4 wood lt
M23 2 17 81 1400 60 11 SE 0 wood lt
N23 0 0 100 1360 100 18 SE 0 wood+scrub t
O23 0 0 100 1340 90 16 NW 0 wood+scrub t
P23 0 0 100 1320 80 14 SE 11 scrub+wood rtw
A22 0 0 100 1410 60 12 E 6 scrub+wood t
B22 0 0 100 1400 50 13 flat 70 rice+scrub rt
C22 0 0 100 1390 40 7 flat 33 rice rtw
D22 0 0 100 1400 50 11 flat 13 wood rtw
E22 0 0 100 1400 40 11 flat 0 wood+scrub Rrt
F22 0 0 100 1410 60 10 NE 22 wood+grass Rlrt
G22 0 0 100 1410 60 10 N 16 grass+wood lrt
H22 35 41 24 1400 50 9 NE 38 water+wood lrt
I22 15 51 34 1410 50 10 flat 27 wood+grass lrt
J22 56 27 17 1390 40 5 S 45 water+wood lrt
K22 83 17 0 1390 20 2 flat 2 water l
L22 20 50 30 1400 50 11 flat 2 wood l
M22 4 15 81 1390 80 13 NE 1 wood lt
N22 0 0 100 1360 70 17 NE 1 scrub+wood t
O22 0 0 100 1370 70 17 NE 5 wood t
P22 0 0 100 1330 100 20 NE 5 wood rt
A21 0 0 100 1420 70 13 N 1 wood+scrub rt
B21 0 0 100 1400 70 12 E 29 scrub+rice rtw
C21 0 0 100 1390 40 8 W 59 rice+scrub rtw
D21 0 0 100 1400 60 12 flat 0 wood rt
E21 0 0 100 1410 50 12 SW 34 scrub+wood Rrt
F21 0 2 98 1410 60 12 SE 26 grass+wood Rlrt
G21 0 2 98 1410 50 13 flat 26 wood r
H21 26 49 25 1400 50 9 flat 14 wood+water lrt
I21 15 37 48 1400 50 8 S 52 wood lrt
J21 88 12 0 1390 10 1 flat 1 water lrt
K21 31 46 23 1400 40 9 flat 4 water+wood lt
L21 0 7 93 1420 70 13 NW 0 wood+grass lt
M21 0 0 100 1400 100 15 E 1 wood t
N21 0 0 100 1390 90 15 NW 2 wood+scrub t
O21 0 0 100 1370 80 17 E 7 wood t
P21 0 0 100 1340 100 21 E 3 wood t
A20 0 0 100 1420 90 15 W 26 scrub+wood rt
B20 0 0 100 1410 90 13 SE 12 wood+scrub rt
C20 0 0 100 1380 40 5 flat 20 rice rtw
D20 0 0 100 1400 40 10 flat 16 scrub rt
E20 0 0 100 1390 40 8 SW 63 grass Rrt
F20 10 44 46 1400 40 9 NE 44 wood+grass Rlrt
G20 12 29 59 1400 50 11 SW 14 grass+wood lrt
H20 0 9 91 1410 50 7 E 2 wood lrt
I20 40 29 31 1390 30 4 E 3 water+grass lr
J20 82 17 1 1390 30 2 flat 2 water lt
K20 16 52 32 1400 50 12 flat 3 grass+wood lt
L20 1 11 88 1410 70 13 S 0 wood lt
M20 0 0 100 1400 70 15 flat 3 wood t
N20 0 0 100 1410 70 13 S 2 wood+grass t
O20 0 0 100 1380 90 18 E 0 wood t
P20 0 0 100 1340 100 19 E 11 wood+scrub tw
A19 0 0 100 1430 100 16 E 0 wood+scrub rt
B19 0 0 100 1400 50 11 SE 36 scrub rt
C19 0 0 100 1380 20 4 flat 60 rice rtw
D19 0 0 100 1400 40 11 NW 41 scrub rt
E19 0 0 100 1400 40 11 flat 15 wood+scrub rt
F19 0 2 98 1400 50 11 NE 15 wood Rrt
G19 6 39 55 1400 40 9 N 28 wood+grass lrt
H19 32 60 8 1390 20 6 flat 39 water+wood lrs
I19 71 27 2 1390 30 4 flat 5 water lrs
J19 67 33 0 1390 40 4 flat 5 water+scrub lst
K19 36 54 10 1390 40 7 S 4 grass+water lt
L19 1 16 83 1400 50 12 NW 5 wood+grass lt
M19 0 0 100 1410 70 12 N 4 wood+grass t
N19 0 0 100 1400 70 14 NE 1 wood t
O19 0 0 100 1380 80 18 E 0 wood t
P19 0 0 100 1330 80 20 N 15 wood+scrub tw
A18 0 0 100 1410 90 15 E 0 scrub+wood rt
B18 0 0 100 1390 50 11 E 0 scrub+rice tw
C18 0 0 100 1380 30 6 flat 56 rice rtw
D18 0 0 100 1390 40 9 flat 31 rice rt
E18 1 8 91 1400 60 11 N 22 scrub Rlrt
F18 3 25 72 1410 60 12 S 26 wood+grass Rlrt
G18 29 58 13 1400 50 10 E 30 wood+water lrs
H18 8 54 38 1400 30 8 flat 47 grass lr
I18 92 8 0 1390 20 1 flat 0 water lr
J18 51 31 18 1390 30 5 NW 0 water+grass lt
K18 10 46 44 1410 70 14 NW 0 wood+grass l
L18 0 2 98 1420 70 13 W 3 grass+wood t
M18 0 0 100 1430 90 16 E 0 wood t
N18 0 0 100 1410 60 13 SW 2 wood t
O18 0 0 100 1400 90 16 E 5 wood t
P18 0 0 100 1360 110 21 N 6 wood tw
A17 0 0 100 1400 50 11 E 7 wood+scrub rtw
B17 0 0 100 1390 40 9 NW 22 rice rtw
C17 1 10 89 1400 50 13 NE 61 scrub+wood Rlrt
D17 17 33 50 1400 40 10 flat 67 wood Rlrst
E17 7 34 59 1410 60 11 SW 49 wood Rlrt
F17 24 45 31 1400 60 9 NE 49 wood+water lrt
G17 40 41 19 1400 50 7 S 32 water+wood lrs
H17 33 50 17 1390 20 4 flat 40 grass+water lrt
I17 85 14 1 1390 30 2 flat 0 water l
J17 31 56 13 1390 30 9 flat 2 grass+water lt
K17 5 35 60 1410 60 13 SW 1 wood+grass lt
L17 0 0 100 1420 70 13 W 0 wood+grass t
M17 0 0 100 1420 90 16 NE 0 wood t
N17 0 0 100 1400 60 12 flat 0 wood tw
O17 0 0 100 1380 100 15 E 1 wood tw
P17 0 0 100 1390 100 16 NW 9 wood tw
A16 0 0 100 1390 50 11 W 41 rice+wood Rlrtw
B16 0 0 100 1400 50 12 flat 0 wood+scrub Rrt
C16 0 3 97 1400 40 11 flat 20 scrub+wood Rrt
D16 40 44 16 1400 40 9 E 19 wood+water lrt
E16 17 59 24 1410 60 13 flat 43 wood lrt
F16 46 36 18 1390 40 7 S 31 water+wood lrt
G16 37 37 26 1390 30 6 flat 37 water+grass lr
H16 69 23 8 1390 20 3 E 12 water lr
I16 56 35 9 1390 30 5 flat 0 water l
J16 32 61 7 1390 30 7 flat 0 grass+water l
K16 10 37 53 1400 60 11 NW 0 grass lt
L16 0 0 100 1410 70 11 W 1 wood t
M16 0 0 100 1430 90 15 E 2 wood t
N16 0 0 100 1390 60 12 flat 0 wood+grass tw
O16 0 0 100 1390 60 12 flat 1 wood+grass t
P16 0 0 100 1410 70 12 W 0 wood+grass t
A15 0 0 100 1380 60 7 W 10 rice Rlrtw
B15 0 0 100 1390 60 13 flat 19 rice+wood Rrt
C15 0 1 99 1390 50 12 flat 52 wood+rice rt
D15 43 40 17 1390 40 8 flat 52 water+wood lrt
E15 44 39 17 1400 60 9 S 16 wood+water lrt
F15 81 19 0 1390 20 1 flat 7 water lrt
G15 53 44 3 1390 30 8 flat 16 water+wood lr
H15 85 14 1 1390 30 2 flat 1 water l
I15 41 45 14 1390 30 8 flat 0 water+grass l
J15 39 40 21 1400 50 8 NE 0 grass+water l
K15 6 26 68 1410 60 13 SW 0 grass+wood l
L15 0 2 98 1410 60 12 S 4 wood+grass t
M15 0 0 100 1420 70 13 SE 1 wood+grass t
N15 0 5 95 1390 50 11 flat 7 grass+wood tw
O15 13 38 49 1390 40 10 flat 0 wood+grass ltw
P15 0 0 100 1410 40 9 NW 0 wood tw
A14 0 0 100 1380 20 2 flat 148 rice rtw
B14 0 0 100 1400 60 11 NW 159 scrub rt
C14 10 43 47 1400 60 12 NE 65 wood lrt
D14 46 50 4 1400 40 10 N 11 water+wood lr
E14 98 2 0 1390 30 1 flat 0 water l
F14 62 38 0 1390 30 7 flat 0 water+wood l
G14 59 38 3 1390 30 5 flat 0 water+wood l
H14 66 31 3 1390 30 3 flat 0 water l
I14 73 26 1 1390 30 4 flat 1 water l
J14 38 58 4 1390 30 7 flat 0 water+grass l
K14 19 61 20 1390 40 10 flat 0 grass l
L14 8 50 42 1410 50 11 flat 0 wood+grass l
M14 24 53 23 1390 50 8 SE 0 grass+water dltw
N14 31 52 17 1390 30 6 flat 0 wood+water ltw
O14 17 30 53 1390 40 6 N 1 wood ltw
P14 0 0 100 1400 40 9 flat 0 wood tw
A13 0 0 100 1380 40 5 NE 3 rice rtw
B13 3 10 87 1400 70 13 W 24 wood dlrtw
C13 61 35 4 1390 60 7 SE 13 water+wood lrtw
D13 22 41 37 1410 70 12 SW 20 wood lrt
E13 84 16 0 1390 60 4 E 0 water lr
F13 69 30 1 1390 30 4 flat 0 water l
G13 26 43 31 1400 50 8 W 0 wood+water l
H13 19 30 51 1410 50 9 SE 0 wood l
I13 61 37 2 1390 40 6 E 0 water+wood l
J13 68 29 3 1390 40 5 flat 1 water l
K13 32 39 29 1400 40 8 S 1 grass+water l
L13 59 36 5 1390 30 4 flat 0 water l
M13 47 43 10 1390 20 5 flat 0 water+grass lt
N13 13 53 34 1400 40 10 S 0 wood+grass lt
O13 12 44 44 1400 50 10 SW 0 wood lt
P13 0 0 100 1410 40 9 flat 0 wood+grass t
A12 0 0 100 1400 50 13 NW 5 scrub+wood rt
B12 6 36 58 1410 50 14 NE 2 wood dlrt
C12 90 10 0 1390 20 1 flat 0 water ltw
D12 99 1 0 1390 10 0 flat 0 water l
E12 98 2 0 1390 10 0 flat 0 water l
F12 53 43 4 1390 30 7 flat 0 water+wood l
G12 55 33 12 1390 30 5 NE 0 water+wood l
H12 85 15 0 1390 20 2 flat 0 water l
I12 50 49 1 1390 40 7 NW 0 water+wood l
J12 7 43 50 1410 70 15 flat 0 wood+grass l
K12 22 57 21 1400 50 12 N 0 grass l
L12 39 55 6 1390 30 7 N 3 grass+water lrt
M12 14 54 32 1400 40 9 NW 0 grass+wood lt
N12 46 44 10 1390 40 7 NE 1 water+grass l
O12 10 26 64 1400 60 11 N 1 wood lrt
P12 0 0 100 1390 40 10 flat 1 wood rt
A11 1 14 85 1390 50 13 SW 0 wood lrt
B11 59 40 1 1390 50 8 flat 0 water lrt
C11 54 42 4 1390 30 5 flat 0 water+wood ltw
D11 42 57 1 1390 30 6 N 0 wood+water lw
E11 69 31 0 1390 30 3 flat 12 water lr
F11 51 43 6 1390 40 7 NW 0 water+wood l
G11 18 59 23 1400 40 9 NE 0 wood l
H11 73 27 0 1390 20 3 flat 0 water l
I11 72 19 9 1390 50 4 SW 0 water+wood l
J11 5 22 73 1420 70 13 W 1 wood+grass l
K11 0 9 91 1420 80 13 E 0 wood+grass lt
L11 16 49 35 1400 40 10 S 0 grass lrt
M11 2 33 65 1410 40 12 flat 0 wood lrt
N11 26 58 16 1400 40 11 flat 0 wood+water lt
O11 15 42 43 1400 50 10 S 5 wood lrt
P11 3 12 85 1410 50 10 N 1 wood lrt
A10 4 30 66 1410 80 16 N 0 wood lrt
B10 33 53 14 1400 70 12 W 0 wood+water lt
C10 20 48 32 1410 80 12 NE 0 wood ltw
D10 26 61 13 1400 40 9 SW 0 water lw
E10 38 61 1 1390 30 8 flat 5 wood+water lr
F10 56 36 8 1390 40 6 SW 0 water+wood lt
G10 9 51 40 1410 50 12 flat 0 wood l
H10 45 46 9 1390 50 8 N 0 water+wood l
I10 69 28 3 1390 50 6 N 0 water+wood l
J10 40 38 22 1400 70 9 W 0 water+wood l
K10 1 17 82 1420 80 12 SE 0 grass+wood lt
L10 13 51 36 1400 40 11 N 0 grass lt
M10 0 7 93 1410 50 13 N 0 wood lrt
N10 0 12 88 1410 50 13 flat 5 wood lt
O10 0 4 96 1410 60 11 NE 0 wood+grass rt
P10 2 17 81 1400 30 10 flat 1 wood lrt
A9 0 1 99 1440 80 13 flat 2 wood rt
B9 2 12 86 1410 60 10 flat 0 wood ltw
C9 0 2 98 1420 90 15 SE 0 wood tw
D9 27 57 16 1390 30 8 flat 3 water lrtw
E9 31 68 1 1400 50 8 flat 1 grass+water lrt
F9 53 46 1 1390 30 7 flat 1 water+wood lt
G9 19 46 35 1410 50 12 SW 0 wood l
H9 33 54 13 1400 50 10 flat 0 wood+water l
I9 1 17 82 1420 70 17 flat 0 wood l
J9 38 52 10 1400 60 11 E 0 wood+water l
K9 27 48 25 1400 60 12 W 0 grass+water lt
L9 1 14 85 1410 50 12 NE 0 wood+grass lt
M9 0 0 100 1400 50 11 W 9 wood rt
N9 0 0 100 1420 50 12 N 0 wood rt
O9 0 0 100 1420 60 11 N 2 wood r
P9 0 0 100 1410 90 15 SE 0 wood rt
A8 0 0 100 1430 50 11 SE 0 wood+scrub rtw
B8 0 0 100 1410 60 12 N 4 wood rtw
C8 0 0 100 1420 80 14 N 2 wood+scrub rt
D8 13 48 39 1400 60 11 NE 4 wood lrt
E8 37 51 12 1400 60 10 NE 0 water lt
F8 35 64 1 1390 30 11 flat 0 wood+water l
G8 46 43 11 1400 50 9 flat 0 water+wood l
H8 31 63 6 1400 40 12 flat 0 wood+water l
I8 13 50 37 1410 60 15 flat 0 wood lt
J8 64 33 3 1390 50 7 NE 0 water+wood l
K8 38 48 14 1400 50 10 S 0 water+grass lt
L8 2 20 78 1410 60 13 W 0 grass+wood lrt
M8 0 0 100 1420 60 13 N 4 wood rt
N8 0 0 100 1430 50 11 flat 2 wood rt
O8 0 0 100 1400 90 16 SE 0 wood rt
P8 0 0 100 1370 100 17 SE 0 wood -
A7 0 0 100 1420 60 12 NW 6 crop rtw
B7 0 0 100 1460 130 18 NW 13 wood rt
C7 0 0 100 1450 140 17 NE 9 wood rt
D7 0 0 100 1410 70 15 flat 16 wood t
E7 15 42 43 1400 50 13 E 0 wood lt
F7 31 63 6 1400 50 12 flat 0 wood+water l
G7 48 40 12 1390 50 7 SW 0 water+wood l
H7 9 49 42 1410 60 15 NW 2 wood lt
I7 14 28 58 1410 70 14 SE 1 wood lt
J7 60 37 3 1390 40 8 flat 0 water+wood l
K7 36 48 16 1400 40 8 NE 0 water+wood lt
L7 2 20 78 1420 60 10 SW 0 wood lrt
M7 0 0 100 1420 40 11 flat 4 wood rt
N7 0 0 100 1410 70 13 E 1 wood rt
O7 0 0 100 1400 70 15 flat 1 wood t
P7 0 0 100 1380 80 18 NE 4 wood t
A6 0 0 100 1430 90 14 E 27 wood rtw
B6 0 0 100 1490 150 18 W 0 wood+scrub rt
C6 0 0 100 1500 110 15 NE 1 wood+scrub rt
D6 0 0 100 1480 170 20 NE 2 wood rt
E6 15 40 45 1410 80 16 E 0 wood l
F6 21 63 16 1400 50 13 NW 0 wood lt
G6 43 45 12 1400 50 9 flat 0 water+wood l
H6 11 53 36 1410 70 16 SW 0 wood+grass lt
I6 9 28 63 1410 60 15 E 0 wood lt
J6 37 45 18 1400 60 10 flat 0 water+grass lt
K6 17 51 32 1410 70 12 E 0 grass lt
L6 7 27 66 1410 60 10 W 3 wood lt
M6 0 0 100 1430 50 12 W 0 wood t
N6 0 0 100 1440 60 12 E 0 wood rt
O6 0 0 100 1420 60 13 flat 0 wood t
P6 0 0 100 1400 110 17 E 1 wood tw
A5 0 0 100 1440 110 16 NW 8 wood+scrub rtw
B5 0 0 100 1490 80 12 NW 7 wood rt
C5 0 0 100 1490 80 13 NW 6 wood t
D5 0 0 100 1470 160 19 E 0 wood -
E5 1 18 81 1400 60 16 NE 0 wood lt
F5 13 38 49 1410 60 14 flat 0 wood lt
G5 32 56 12 1400 60 13 NW 1 wood+water lt
H5 5 25 70 1420 70 16 NW 0 wood lt
I5 30 44 26 1400 70 12 E 1 wood+water lt
J5 24 42 34 1400 60 12 W 0 wood+grass lt
K5 0 7 93 1410 60 12 flat 0 grass+wood lt
L5 0 8 92 1410 50 12 flat 0 wood+grass lt
M5 0 0 100 1420 60 11 W 4 wood t
N5 0 0 100 1430 60 10 E 2 wood rt
O5 0 0 100 1410 60 14 E 0 wood tw
P5 0 0 100 1390 80 18 NE 0 wood tw
A4 0 0 100 1490 140 16 NW 6 wood+scrub rt
B4 0 0 100 1540 110 14 N 0 wood rt
C4 0 0 100 1550 130 17 N 0 wood rt
D4 0 0 100 1520 150 20 NE 0 wood rt
E4 1 13 86 1420 90 17 SE 0 wood lt
F4 37 53 10 1400 50 13 flat 0 wood+water lt
G4 9 45 46 1420 80 15 NW 0 wood lt
H4 3 24 73 1420 80 15 N 0 wood lt
I4 33 52 15 1400 50 11 flat 0 wood+water l
J4 4 33 63 1410 60 14 NW 0 wood+grass lt
K4 0 0 100 1410 50 14 flat 4 grass+wood t
L4 0 0 100 1420 50 12 NE 2 wood+grass t
M4 0 0 100 1420 60 11 W 4 wood rt
N4 0 0 100 1420 60 13 E 3 wood rt
O4 0 0 100 1420 70 14 E 1 wood t
P4 0 0 100 1380 90 18 SE 0 wood+scrub tw
A3 0 0 100 1490 130 15 SW 0 wood+scrub rt
B3 0 0 100 1560 130 16 SW 1 wood rt
C3 0 0 100 1550 120 15 SE 3 wood rt
D3 0 0 100 1510 170 23 E 3 wood lrt
E3 0 0 100 1430 80 17 NE 0 wood t
F3 1 16 83 1400 60 15 flat 2 wood lt
G3 2 19 79 1410 70 16 flat 0 wood lt
H3 2 20 78 1420 70 17 SE 4 wood+grass lt
I3 47 52 1 1390 40 10 flat 0 water+wood lt
J3 2 22 76 1410 50 14 flat 4 wood+grass lt
K3 0 0 100 1410 50 12 flat 19 wood+grass rt
L3 0 0 100 1430 50 11 flat 1 grass+wood rt
M3 0 0 100 1430 60 11 N 4 grass+wood rt
N3 0 0 100 1420 60 11 NE 7 wood+grass rt
O3 0 0 100 1410 60 14 SE 0 wood tw
P3 0 0 100 1370 80 18 NE 0 wood tw
A2 0 0 100 1460 90 14 SW 2 wood+scrub t
B2 0 0 100 1530 90 15 W 2 wood t
C2 0 0 100 1540 90 14 N 2 wood t
D2 0 0 100 1470 150 21 SE 0 wood t
E2 0 0 100 1430 80 17 E 17 wood t
F2 0 0 100 1400 50 17 flat 12 wood lt
G2 0 0 100 1430 70 18 flat 1 wood t
H2 4 11 85 1400 60 13 NE 0 wood+rice lt
I2 4 17 79 1400 50 10 NW 0 wood+rice ltw
J2 0 5 95 1410 50 14 flat 1 wood+grass t
K2 0 0 100 1410 50 12 flat 11 wood rt
L2 0 0 100 1430 70 10 NW 2 wood+grass rt
M2 0 0 100 1450 50 10 flat 0 grass+wood rt
N2 0 0 100 1430 70 13 E 0 wood rtw
O2 0 0 100 1400 70 12 NW 2 wood tw
P2 0 0 100 1410 80 14 N 0 wood t
A1 0 0 100 1450 70 13 W 6 wood lt
B1 0 0 100 1520 90 15 SW 0 wood t
C1 0 0 100 1550 130 18 S 0 wood t
D1 0 0 100 1480 130 19 NE 0 wood rt
E1 0 0 100 1430 90 17 E 23 wood+scrub rt
F1 0 0 100 1420 70 17 W 10 wood lrt
G1 0 0 100 1420 70 16 S 1 wood rt
H1 0 0 100 1410 50 14 flat 0 wood rt
I1 0 0 100 1410 60 14 W 0 wood+grass tw
J1 0 0 100 1430 60 13 N 0 wood+grass t
K1 0 0 100 1420 70 13 N 3 grass+wood rt
L1 0 0 100 1440 60 9 W 2 wood+grass rt
M1 0 0 100 1440 70 12 SE 0 wood+grass rtw
N1 0 0 100 1420 50 12 flat 7 wood+grass rtw
O1 0 0 100 1420 60 12 NW 6 wood rt
P1 0 0 100 1430 80 12 E 0 wood rt
```
