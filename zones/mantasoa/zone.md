# Zone: Lac de Mantasoa

The Zone is Lac de Mantasoa (Malagasy: Tobindranon'i Mantasoa), a reservoir in the central highlands of Madagascar about 60 km east of Antananarivo, at about 1,385 m. It is not a circle on a mountain. It is the lake. Something is in the water. Use the place as it really is.

- **Where:** the lake lies between about 19.064 S and 18.954 S, 47.844 E and 47.914 E: 7.3 km west to east and 12.2 km south to north. The grid's centre is 19.0093 S, 47.8751 E, the corner where squares T, U, 26 and 27 meet. That point is open water about 190 m from the nearest shore and means nothing on the ground.
- **The grid.** The usual 250 m squares, with tenths of 25 m, and references that read as in the other zones. What differs is the size and shape of the map. The frame is 10 km by 13 km: 40 columns and 52 rows, with its south-west corner 5,000 m west and 6,500 m south of the centre. It takes in the whole lake and, in the west, Mantasoa village and the Laborde works. Columns run past Z: A to Z, then AA, AB, AC and on to AN, as a spreadsheet letters them; rows run 1 to 52 south to north. AB14-37 is square AB14, 3 tenths (75 m) east and 7 tenths (175 m) north of its south-west corner. `terrain.py` reads and prints these references. Wherever SKILL.md says A to X, 1 to 24, a 6 km square or 36 sheets, use these figures here.
- **Sheets.** The field atlas has 74 sheets of 4 by 4 squares, each 1 km by 1 km at 1:7,500 as in the other zones, but they do not fill the frame. A sheet exists only if it holds water or shore band, or part of the village and Laborde works (and a sheet shut in on all four sides by others is kept). They are numbered 1 to 74 in reading order from the north-west, row by row, so a sheet's neighbours are not at fixed offsets: read them from the pad on the sheet, the index map, or the "Sheets" grid in the gazetteer. Ground off the sheets is still on the grid and the tools still answer for it. Name the sheet when the player moves onto a new one.
- **The Zone's shape.** The Zone is the water as mapped today, every island in it, and a band of shore 100 m inland from the mapped waterline: 15.8 km2 of water, 0.65 km2 of islands and 18.2 km2 of shore band. The atlas draws the inland edge of the band as a heavy dash-dot line where the other zones draw their circle. `terrain.py at` and `line` say for any point whether it is WATER, SHORE BAND, ISLAND (all three inside) or LAND (outside), and how far the mapped waterline is.
- **There is no wire.** The edge is 220 km of ragged shore and nobody has fenced it. People live inside the band: 818 buildings are mapped in it and 28 more on the islands. "Crossing the wire" in the rules means stepping into the shore band or putting off from the bank; "the fence" and "the line" mean the band line on the atlas. How the edge is watched is in the water rules below.
- **Town:** Mantasoa village, where stalkers live, drink and sell, at the west end of the lake about 1.4 km from the nearest water. Its centre is on sheet 28: the town hall (Mairie Mantasoa, E26-78), the post office (F26-08) and the market (F26-18), on the road that runs east through the quarter of Ampiasanomby (H26) to the lake. The works Jean Laborde built here from 1837 are in and west of the village: his house (Ancienne résidence de Jean Laborde à Mantasoa, E27-54, sheet 28), the cannon foundry (Ancienne fabrique de canons, C25-21, sheet 27) and the blast furnace (Ancien haut fourneau de Jean Laborde, B25-85, sheet 27), with the technical lycée beside them (C25-01). The village of Masombahiny is just south (D23-07, sheet 36). OpenStreetMap does not map Laborde's tomb; published accounts say he is buried at Mantasoa. The Institute is in Antananarivo, about 68 km by road: the RN2 east to Manjakandriana, then south.
- **Base map:** no survey sheet is used. The atlas is drawn from data (Copernicus GLO-30 elevation, OpenStreetMap, ESA WorldCover for woods) in the manner of the old Service Géographique de Madagascar and FTM sheets, and it is printed in French with Malagasy place names exactly as mapped. This file and the gazetteer are in English and give every name as the atlas prints it. The lake carries its French name, Lac de Mantasoa.
- **Lie of the land.** The lake is a drowned valley system: a ragged tree of arms, not a sheet of water. Nowhere on it is more than about 360 m from a shore. The trunk runs north to south through columns N to AB; the broadest water is in rows 19 to 28, with the most open reaches at N21-98 (360 m from land, sheet 39), O26-90 (320 m, sheet 30) and X34-16 (305 m, sheet 19). North of row 38 and south of row 16 the lake breaks into narrow fingers, most of them 100 to 300 m wide, running up every side valley, so that land and water alternate every few hundred metres along any straight line. Check a crossing with `line`: it shows the water in the middle. There are five islands, none named: the largest (O16-86, 40 ha, sheet 56) is joined to the west shore by a road across a 20 m gap; the others are at Z35-25, U19-83, Y25-08 and X23-36. Three dams are mapped, none named: one at the west end (J23-31, 160 m long, sheet 38) whose outflow runs to the village and joins the river mapped as Varahina Nord there; one in the north (Y51-10, 190 m, across sheets 2 and 3) with ground falling to about 1,377 m below it; and a short one in the east (AF26-44, 80 m, sheet 34). Published accounts put the main dam (1937-38) on the Varahina-Nord and a saddle dam on the Mandraka side; the data does not say which mapped structure is which. The shore is low and rolling: the band averages 1,398 m, 13 m above the water, and two thirds of it slopes 8 to 20 degrees. The house shore is the north-west: from Hôtel L'Ermitage Mantasoa (M32-74, sheet 23) east to Mantasoa Lodge (T31-87, sheet 24) and north along the arms on sheets 18 and 19, about 360 buildings stand inside the band (sheets 18, 19 and 22 to 25; 114 on sheet 24 alone), houses and lodges spread along the points, with seven mapped landing stages (M31-93, R31-74, S31-06, T34-04, U35-48, W35-49, Y35-45). The road from the village runs north behind that shore through Anjozoro (L35-25). A second cluster of houses lines the northern arms (sheets 6, 10, 11, 13 and 14); la Pointe is among them. The south and east of the lake are close to empty: the 36 sheets from 39 on hold about 20 buildings in the band between them, reached by a few tracks that end at the water. Away from the lake the hills are plantation and scrub: tree cover is about half of the land on the grid, grass a fifth, scrub a sixth, rice fields in the valley floors about a tenth (most of it west and north-west, around the village and Anjozoro). The high ground is in the south-west, 1,632 m at J4-64 by the mapped archaeological site Fanongoavana (J4-65), which is off the sheets. Along the east edge (columns AH to AN) the ground falls off the plateau to 1,277 m at AN10. Check, never assume.
- **The water level moves the shore.** This is a working reservoir, drawn down and refilled. The level changes through the year and from year to year, and the shoreline moves with it: a metre of level moves a shelving shore many metres. The shore on the atlas, the band, and what the tool calls WATER are the shore as mapped, on whatever day it was mapped. The elevation model's lake surface, 1,385 m, is the level on the day the radar flew. Published figures give a higher full level and a larger lake (about 20 km2) than the 15.8 km2 mapped today, and recent reports say it holds far less than it once did. Treat the mapped shore as the fixed edge of the Zone for the rules, and treat the real waterline as something the campaign's lake level sets (water rules, below).
- **Depths are unknown.** There is no bathymetry in the data, the tool, the gazetteer or the atlas. `terrain.py` reports the flat surface. Do not quote a depth as fact. When play needs one, the character finds it with a sounding line, and you fix it then and keep it.
- **Season and climate:** tropical highland. A cool dry season from May to October: days about 20 C, nights about 10 C and colder on the water, with drizzle and low mist off the eastern forest on many days. A warm wet season from November to April: days about 26 C, nights about 17 C, heavy rain and thunderstorms, usually building through the day; cyclones pass in the wet months. These temperatures are Antananarivo's (1991 to 2020 normals), which is 100 m lower and drier; no station figures for Mantasoa were found. Day length changes little: about 11 hours in June, 13 in December. Set sun and moon from the date and 19 S, 47.9 E.
- **People and languages:** Malagasy (the Merina dialect) is what people speak at home, in the market and on the water; French is the language of offices, signs, the Institute and most dealings with outsiders. Real life here is rice fields, charcoal and timber from the plantations, fishing from pirogues, and weekend visitors from the capital at the lodges. A Peace Corps training centre is mapped at L23-85 and a gendarmerie brigade at L25-44 (both sheet 38). In the fiction the band has had decades of neglect: the lakeside houses are shells, the landing stages are rotten or gone.
- **Units:** metric throughout. The tools answer in metres and feet.
- **Data limits:** the elevation model's true resolution is 30 m, resampled to 20 m: a bank, a terrace wall or a gully under ten metres does not show. It is a surface model, so on wooded ground it reads the treetops, up to 20 m or so above the soil. Almost nothing on the grid is named in OpenStreetMap: no arm, bay, point or island of the lake, and few roads. Buildings are well mapped; paths less so. Woods come from a 10 m satellite classification, not a survey. The gazetteer's per-square table lists only squares in or near the Zone and those of the village. The atlas marks one point of land by name, la Pointe (W48-02, sheet 6).
- **Check:** `python terrain.py --zone mantasoa at N21-98` should report about 1385 m, the lake surface, and end `WATER (in the Zone)`. `python terrain.py --zone mantasoa at AB14-37` should answer for a two-letter column (about 1401 m, SHORE BAND). On Windows run `near` as `python -X utf8 terrain.py --zone mantasoa near ...`: its output carries accented names.

---

## Local rules: water

These apply in this zone only. They adapt sections 3, 5 and 6 of SKILL.md to a Zone that is mostly water. Where they are silent, the general rules stand. They add no hazard and no artifact: what is in the water is in the ledger, and the ledger's placement rules decide what can sit on water, on the bed, on the shore band or on an island.

**The edge.**

- The Zone begins at the band line, 100 m inland from the mapped waterline, and at the water's edge of any boat putting off. Record the minute the character crosses the band line or leaves the bank as the minute of crossing.
- Check every position with `terrain.py at` before you say whether the character is inside. WATER, SHORE BAND and ISLAND are inside. LAND is outside.
- A run may enter on foot through the band, by boat from a landing outside the player's own choosing, or both. Each leg is one or the other: write which.

**Boats.**

- The ordinary boat is a pirogue: a narrow dugout or plank canoe, paddled or poled. It carries two people, or one person and cargo. A larger plank boat carries four and is slower, heavier to drag and easier to see.
- Paddling speed on proven water is about 4 km/h steady, 15 minutes a kilometre: a 400 m crossing takes 5 to 6 minutes. Use 3 km/h loaded or into a head wind, 2 km/h at night or loaded into wind, and 1 km/h or less when sounding and marking as you go. A hard sprint reaches 6 km/h for no more than five minutes and is a Hands roll if anything depends on it.
- Poling works only where the pole finds bottom. Whether it does is a sounding, not something you know.
- Measure every water leg with `terrain.py line` and give its length and time. At the steady speed a tenth of a square (25 m) is about 20 seconds and a square (250 m) just under 4 minutes. Nowhere on this lake is more than about 360 m from a shore.
- Getting a boat to the water is travel on land with the boat as load: two people carry a pirogue at half pace with both hands; one person drags it at a quarter pace and leaves a mark anyone can read.
- Stepping in, stepping out, changing places and hauling anything over the side each take a minute and are done one at a time.

**What replaces bolts, flags and the lane.**

- **The float.** On water a bolt sinks and tells nothing. The thrown tell is a float on a light line: a cork, a sealed gourd or a wooden block on 15 to 20 m of cord, thrown ahead and drawn back. A character carries 6 floats and one line where the sheet says bolts; bolts are still carried for the shore band and islands. A throw and a watch takes 2 minutes, as a bolt does. A float that is lost is gone, and the line with it if it is cut or let go.
- **The sounding line.** A weighted cord knotted every metre, 20 m long. It is the only source of depth in this zone. One sounding takes 2 minutes from a still boat. Fix the depth when it is first sounded, write it in the private atlas against the reference and the campaign's lake level, and never change it.
- **Buoys.** Flags become marker buoys on water: a float on a cord and a stone. The character carries 10 markers in all, flags and buoys together, and says which they are when setting them. Setting a buoy takes 3 minutes and needs a sounding first. A buoy is seen by anyone on the lake by day. Lift them coming out, as with flags.
- **The channel.** The lane on water is a channel: water proven by float and sounding, two boat-widths wide (about 2 m), between two named marks: buoys, or fixed things on the shore taken in line. A channel is paddled at normal speed. Everything off it is unknown water. Wind and current move a boat sideways: holding a channel in a cross wind or at night without marks is an Eyes roll under strain, and a failure means the boat is off the channel by a distance you state.
- **Proving a channel.** To the same standard as a probed lane, proving water costs about an hour per 30 m: it is ten times the pace of a lane on land because a float covers the width at a throw, but the boat must be held still for every throw and sounding. Faster with less certainty, as on land.
- **One boat per channel.** A second boat waits 25 m back. Two people in one pirogue are one body for this rule: what takes the boat takes both.
- **Paces** do not count on water. Distance is by time at a known speed, by a line between marks, or by the atlas.

**Load in a boat.**

- A person in a boat still has six slots. A paddle in use fills both hands for the paddler; a pole fills both. A person paddling cannot throw a float, sound, or hold a lamp: in a pirogue for two, one works the boat and one works the water.
- A pirogue takes its crew and four slots of cargo on the bottom boards. A fifth and sixth slot can go in, and then the boat rides low: half speed, and every shift of weight is a Hands roll.
- A full empty is cargo for the whole boat: it fills all the cargo room, both people board and land it together, and the boat rides low.
- Cargo on the boards is not on anyone's body. It stays with the boat if the boat is lost.

**Capsizing and going in.**

- A boat goes over only from a failed roll, a stated cost on a 7 to 9, or a ledger entry that says so. State the risk before the action that carries it.
- When it goes over, everything loose is in the water: all cargo on the boards, anything held in a hand, the lamp in use. What is strapped to the body stays. Whether anything can be found again depends on a depth nobody has sounded.
- A person in the water with a filled pack is under strain at once. Each minute, they shed a slot of their choice or roll Hands; on a failure they take 1 Harm.
- Righting and bailing a pirogue takes 10 minutes for two people from the water and a Hands roll for one alone; in the shallows it takes 5 and no roll.
- Wet clothing in the cool season is strain until the character is dry: 30 minutes by a fire, which is light and smoke, or a change of clothes that was kept dry.
- Being in the water is being in the Zone with the whole body. Apply the ledger exactly.

**Noise and light.**

- Open water hides nothing. By day a boat is seen from any shore that faces it, out to the limit of the reach. On a clear night under a moon, a boat is seen at 300 m and its wake further; with no moon, at 50 m.
- Sound carries flat over water. A paddle knocked on a gunwale, a dropped stone, a voice above a murmur is heard across any reach of this lake on a still night. Quiet paddling is three quarters speed.
- Any light on the water is seen from every shore that has a line to it, and its reflection doubles it. A lamp hooded and held below the gunwale lights the boards and nothing else. Use the raking lamp only where the player has accepted being seen.
- Mist on a cool-season night or dawn cuts sight to 30 m for everyone, patrol and player alike. Then a channel is held only by marks at that distance or by a line.

**Landing and the shore band.**

- Landing takes 3 minutes at a shelving bank or a landing place and 10 at a steep or overgrown one. The gazetteer lists the landing places where a road or track meets the water; check the bank with `terrain.py at` and `near`.
- The first metres above the waterline are unknown ground like any other. A landing is proven with a float thrown onto the bank and then with bolts, before anyone steps out.
- On the band and on the islands the land rules apply as written: bolts, flags, the one-metre lane, one body per lane.
- A boat left on a bank is evidence and a way home. Say where it is left, how it is hidden and how it is tied. A boat that is not tied is where the wind puts it.
- A token left at a landing serves as one left at a junction does.

**The lake level.**

- At the start of a campaign set the lake level for the month and write it in the private atlas. Change it only when the calendar month changes, by one step at most, and say nothing unless the character could see it.
- Use five steps. **Full:** March to May, after the rains; the water stands at or above the mapped shore and the lowest ground of the band is wet. **High:** June and July. **Middle:** August and September; this is the mapped shore. **Low:** October and November, the end of the dry season; the water has drawn back from the mapped shore, most on gently shelving ground and in the heads of the narrow arms, leaving mud, stumps and the old shoreline exposed. **Rising:** December to February, with the rains; the level climbs through the season, fast after storms. A dry year runs one step lower than the month; a wet year one step higher. Fix the year at campaign start.
- The Zone's edge does not move with the level: the band line on the atlas is the line. What moves is how much of the Zone is under water. Ground the tool calls WATER may be mud at low level; ground it calls SHORE BAND may be flooded when the lake is full.
- Exposed mud is slow and loud: half pace, a clear trail, and no cover. A boat cannot cross it; it is dragged. The narrow heads of arms may be closed to boats at low level. Decide which, arm by arm, the first time one matters, and keep the ruling.
- Anything the ledger fixes in place stays where it was fixed when the level changes. Whether it is then under water, at the surface or on dry mud follows from the level and from soundings already recorded. Work it out; do not move it.
- Soundings are recorded against the level of the day. Add or subtract the step when the level changes: use half a metre a step unless play has fixed a different figure.

**Patrol.**

- There is no fence to patrol. The Institute and the gendarmerie watch the lake from the three dams, from the ends of the roads and tracks that reach the water (the gazetteer's landing places), and from the water by boat.
- Fix the night's watch when you fix the run: which dams and road ends are manned, by how many, from when to when; and the patrol boat's circuit as a list of references with clock times. A motor is heard long before it is seen. A patrol that paddles is quiet and rare.
- A watcher on a dam or road end sees what the noise and light rules say can be seen from there. Check the line of sight with `terrain.py line`: a point of land between hides a boat.
- The house shore in the north-west has the most road ends and the most eyes outside the band. The south and east have almost none, and the longest carry to reach.
- Being seen on the water, leaving a boat, a buoy or a drag mark, and landing at a road end all feed Heat as section 9 has it for the wire.

**Washing.**

- Wash at the line: twenty minutes at the band line, on the land side, on the way out. Lake water is Zone water. Do not wash with it, and do not carry it out as washing water.
- A run that leaves by boat washes at the landing, after the boat is ashore and before the band line is crossed. The boat, the paddles, the lines and the floats are washed too, or left inside the band: washing the boat and gear adds twenty minutes.
- Skipping it carries something home, as the general rule says. The ledger says what.

**Trade craft, as the lake has it.** Offer these through a mentor or the bar, in their words.

1. Start from a proven landing.
2. The channel is the world.
3. One boat per channel; the second waits.
4. Sound before you buoy.
5. Thirds, for the night, the light and the floats.
6. Keep the turn time, and count the paddle home in it at the loaded, night, head-wind speed.
7. Tie the boat.
8. Lift your buoys.
9. Know the level before you trust last month's channel.
