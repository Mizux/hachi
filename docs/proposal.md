# Hachi Type Extension Proposals

This document tracks proposed cyberpunk-themed types to extend the original 9-type chart in [hachi.md](hachi.md).

## Current 9 Types Overview

The baseline chart covers three core pillars:
- **Physical / Hardware:** `Mil` (`#E00000`), `Nano` (`#C0E000`), `Street` (`#806030`)
- **Organic / Biochemical:** `Bio` (`#00E000`), `Chem` (`#8000E0`)
- **Digital / Network:** `Tel` (`#0060E0`), `Blk` (`#101010`), `Wht` (`#DDDDDD`), `AI` (`#808080`)

### Current Balance Observations
- **`Chem`** only hits 2 types (`Mil`, `Bio`) and is only weak to 1 type (`Street`), appearing in only 2 of the 20 3-type cycles.
- **`AI`** and **`Mil`** only hit 3 types each, whereas `Bio`, `Tel`, `Nano`, `Blk`, `Wht`, and `Street` hit 4 types.
- Several classic elemental/RPG archetypes and colors from [pokemon.py](pokemon.py) (`#F0F000` Yellow, `#40F0F0` Cyan, `#FF8000` Orange, `#E050C0` Neon Pink, `#404040` Charcoal, `#C08060` Sky/Slate) are currently unused.

---

## Candidate New Types

### 1. Energy & Environment Pillars

| Type | Color | Concept & Flavor | Strong Against (`->`) | Weak To (`<-`) |
| :--- | :--- | :--- | :--- | :--- |
| **`Volt`** (or `Grid`) | `#F0F000` (Yellow) | **High-Voltage / EMP / Plasma / Power Grid.** Capacitor discharges, arc-welders, EMP bursts, fusion cells, grid leeches. | `Tel` (EMP jams/fries comms)<br>`AI` (power surge / hardware short)<br>`Nano` (de-energizes swarms)<br>`Aero` / `Mech` (conducts current) | `Street` (grounded/insulated junk)<br>`Mil` (EMP-hardened shielding)<br>`Chem` (corrodes batteries/conductors) |
| **`Cryo`** (or `Therm`) | `#40F0F0` (Cyan) | **Cryogenics / Server Coolant / Stasis.** Liquid nitrogen coolant leaks, supercooled server farms, cryo-pods, thermal shock. | `Bio` (freezes organic tissue)<br>`Chem` (halts chemical reactions)<br>`AI` (throttles/freezes cores)<br>`Nano` (immobilizes micro-actuators) | `Mil` (explosives/thermite shatter ice)<br>`Volt` (resistive heating)<br>`Mech` (crushes brittle ice) |
| **`Rad`** (or `Nuke`) | `#40FF80` (Neon Green) | **Radiation / Isotope / Fallout.** Old-war reactor leaks, depleted uranium, gamma emitters, wasteland fallout. | `Bio` (DNA destruction)<br>`AI` / `Blk` (ionizing bit-flips)<br>`Street` (unshielded exposure) | `Nano` (rad-absorbent/self-repairing)<br>`Mil` (NBC-sealed armor)<br>`Chem` (chelating/scrubbing agents) |

### 2. Cognitive, Sensory & High-Tech Pillars

| Type | Color | Concept & Flavor | Strong Against (`->`) | Weak To (`<-`) |
| :--- | :--- | :--- | :--- | :--- |
| **`Psy`** (or `Neuro`) | `#FF8000` (Orange) | **Neural / Braindance / Memetic / Cyberpsychosis.** BCI hacks, sensory overload, hallucinations, cognitive viruses, BDs. | `Bio` (hijacks nervous system)<br>`Street` (panic/sensory manipulation)<br>`Chem` (overrides pain/chemical receptors)<br>`Corp` (social/cognitive engineering) | `AI` (no organic brain to trick)<br>`Blk` (direct neural malware/frying)<br>`Wht` (cognitive ICE/firewalls) |
| **`Holo`** (or `Opt`) | `#E050C0` (Neon Pink) | **Holographics / Optics / Lasers / Mirage.** Hard-light projections, active optical camo, blinding lasers, AR decoys, Idol glamour. | `Mil` (spoofs targeting optics)<br>`Street` (flash/dazzle/distraction)<br>`Blk` (visual air-gap / decoy)<br>`Psy` (sensory overstimulation) | `Tel` (radar/telemetry sees through light)<br>`AI` (pattern recognition filters illusions)<br>`Chem` (smog/fumes diffuse lasers) |
| **`Qnt`** | `#9040FF` (Violet) | **Quantum / Entanglement / Phasing.** Quantum computers, superposition anomalies, probabilistic phasing, deep-lab physics. | `Blk` & `Wht` (breaks classical encryption)<br>`AI` (out-computes classical logic)<br>`Holo` (wavefunction collapse) | `Bio` & `Street` (macroscopic noise ruins coherence)<br>`Mil` (fragile lab hardware) |

### 3. Industrial, Aerospace & Social Pillars

| Type | Color | Concept & Flavor | Strong Against (`->`) | Weak To (`<-`) |
| :--- | :--- | :--- | :--- | :--- |
| **`Mech`** (or `Ind`) | `#404040` (Charcoal) | **Heavy Industrial / Chrome / Hydraulics.** Loader exosuits, mining drills, titanium plating, full-body chrome (brute force vs `Mil`'s tactical ordnance). | `Street` (crushes improvised gear)<br>`Bio` (heavy steel vs flesh)<br>`Cryo` (shatters frozen targets)<br>`Holo` (collateral area destruction) | `Nano` (dismantles at molecular level)<br>`Mil` (anti-materiel armor-piercing)<br>`Chem` (acid/rust melts joints)<br>`Volt` (conductive frame) |
| **`Aero`** (or `Orb`) | `#C08060` (Slate/Sky) | **Aerospace / VTOL / Orbital.** High-altitude surveillance drones, orbital kinetic strikes, smart-gliders, hover-tanks. | `Street` (out of reach / air superiority)<br>`Chem` (disperses gas clouds)<br>`Bio` (aerial predation)<br>`Mech` (top-down strikes on slow armor) | `Tel` (GPS spoofing/signal jamming)<br>`Mil` (anti-air flak / SAMs)<br>`Volt` (EMP / lightning strikes) |
| **`Corp`** (or `Lux`) | `#FFD700` (Gold) | **Megacorp / Executive / Sovereign.** DRM-locked proprietary tech, legal/financial kill-switches, gold-plated cyberware, elite trauma-team privilege. | `Street` (gentrification / private security)<br>`Wht` (owns the security protocols)<br>`Mil` (funds/controls the contracts)<br>`Mech` (owns the factories) | `Blk` (corporate espionage / zero-day leaks)<br>`Bio` (bioweapons ignore wealth)<br>`Psy` (executive blackmail/braindance) |

---

## Selected Core Expansion Set (+5 Types -> 14 Types)

Replacing `Holo` with **`Corp`** and **`Mech`** alongside **`Volt`**, **`Cryo`**, and **`Psy`** anchors the chart in grounded cyberpunk archetypes:

1. **`Volt`** (`#F0F000`) — Power / EMP / High-Voltage
2. **`Cryo`** (`#40F0F0`) — Coolant / Cryogenics / Thermal Sink
3. **`Psy`** (`#FF8000`) — Neural / Braindance / Memetic
4. **`Corp`** (`#E050C0`) — Megacorp / Executive / DRM / Sovereign
5. **`Mech`** (`#404040`) — Heavy Industrial / Hydraulics / Exo-Rigs

### Key New Type Triangles
- **`Psy` -> `Corp` -> `Mech` -> `Psy`**:
  - `Psy` beats `Corp` (executive braindance blackmail & cognitive manipulation).
  - `Corp` beats `Mech` (owns the factories, industrial patents, and DRM kill-switches).
  - `Mech` beats `Psy` (unthinking hydraulic machinery & brute physical trauma crush mind-hackers).
- **`Volt` -> `Cryo` -> `Psy` -> `Volt`**:
  - `Volt` beats `Cryo` (resistive heating & power surges).
  - `Cryo` beats `Psy` (hypothermia/cryo-stasis shuts down neural activity).
  - `Psy` beats `Volt` (neural/telekinetic redirection & sensory control).

### `Aero` (Aerial / Orbital) as a Secondary Type
Like `Flying` in Pokémon, **`Aero`** (`#C08060`) works especially well as a **secondary type** on dual-typed creatures/units rather than needing pure `Aero` monsters:
- **`Mil / Aero`**: Tactical VTOL gunships, smart-missile drones
- **`Tel / Aero`**: High-altitude signal relays, orbital comms satellites
- **`Corp / Aero`**: Luxury armored Executive AVs (Aerodynes), trauma-team transports
- **`Bio / Aero`**: Winged genetic splices, bio-engineered swarm flyers
- **`Mech / Aero`**: Heavy cargo lifters, orbital drop-loaders
- **`Street / Aero`**: Jury-rigged hoverbikes, scrap-gliders

### Solver Results (14-Type Chart in `hachi.py`)

Running the OR-Tools CP-SAT cycle finder in [tools.py](tools.py) on the 14-type chart yields **58 3-type cycles** with tight balance across all types:

| Type | Weak To (Incoming) | Strong Against (Outgoing) | 3-Type Cycles |
| :--- | :--- | :--- | :---: |
| **`Mil`** | `Tel`, `Nano`, `Chem`, `Blk`, `Wht`, `Corp` (6) | `Bio`, `AI`, `Street`, `Cryo`, `Mech` (5) | **13** |
| **`Bio`** | `Mil`, `Nano`, `Chem`, `Cryo`, `Psy`, `Mech` (6) | `Tel`, `Blk`, `Wht`, `Street`, `Volt` (5) | **11** |
| **`Tel`** | `Bio`, `Blk`, `Wht`, `Volt`, `Cryo`, `Mech` (6) | `Mil`, `Nano`, `AI`, `Street`, `Corp` (5) | **14** |
| **`Nano`** | `Tel`, `Nano`, `Blk`, `Wht`, `AI`, `Volt` (6) | `Mil`, `Bio`, `Nano`, `Chem`, `Street`, `Mech` (6) | **12** |
| **`Chem`** | `Nano`, `Street`, `Cryo`, `Psy` (4) | `Mil`, `Bio`, `Volt`, `Corp`, `Mech` (5) | **9** |
| **`Blk`** | `Bio`, `Wht`, `AI`, `Street`, `Volt` (5) | `Tel`, `Nano`, `Wht`, `Mil`, `Psy`, `Corp` (6) | **12** |
| **`Wht`** | `Bio`, `Blk`, `AI`, `Street`, `Volt`, `Corp` (6) | `Tel`, `Nano`, `Blk`, `Mil`, `Psy` (5) | **13** |
| **`AI`** | `Mil`, `Tel`, `Street`, `Volt`, `Cryo` (5) | `Nano`, `Blk`, `Wht`, `Psy`, `Corp`, `Mech` (6) | **14** |
| **`Street`** | `Mil`, `Bio`, `Tel`, `Nano`, `Psy`, `Corp` (6) | `Chem`, `Blk`, `Wht`, `AI`, `Volt` (5) | **17** |
| **`Volt`** | `Bio`, `Chem`, `Street`, `Psy`, `Mech` (5) | `Tel`, `Nano`, `Blk`, `Wht`, `AI`, `Cryo` (6) | **12** |
| **`Cryo`** | `Mil`, `Volt`, `Corp`, `Mech` (4) | `Bio`, `Tel`, `Chem`, `AI`, `Psy` (5) | **11** |
| **`Psy`** | `Blk`, `Wht`, `AI`, `Cryo`, `Mech` (5) | `Bio`, `Chem`, `Street`, `Volt`, `Corp` (5) | **13** |
| **`Corp`** | `Tel`, `Chem`, `Blk`, `AI`, `Psy` (5) | `Mil`, `Wht`, `Street`, `Cryo`, `Mech` (5) | **13** |
| **`Mech`** | `Mil`, `Nano`, `Chem`, `AI`, `Corp` (5) | `Bio`, `Tel`, `Volt`, `Cryo`, `Psy` (5) | **10** |


