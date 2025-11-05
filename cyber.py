#!/usr/bin/env python3
import tools as t

types = [
    "Mil",
    "Bio",
    "Tel",
    "Nano",
    "Chem",
    "Blk",
    "Wht",
    "AI",
    "Street",
]

colors = [
    "#E00000",  # Mil
    "#00E000",  # Bio
    "#0060E0",  # Tel
    "#C0E000",  # Nano
    "#8000E0",  # Chem
    "#101010",  # Blk
    "#DDDDDD",  # Wht
    "#808080",  # AI
    "#806030",  # Street
]
assert len(types) == len(colors)

strengths = {
    "Mil": ["Bio", "AI", "Street"],
    "Bio": ["Tel", "Blk", "Wht", "Street"],
    "Tel": ["Mil", "Nano", "AI", "Street"],
    "Nano": ["Mil", "Bio", "Nano", "Street"],
    "Chem": ["Mil", "Bio"],
    "Blk": ["Tel", "Nano", "Wht", "Mil"],
    "Wht": ["Tel", "Nano", "Blk", "Mil"],
    "AI": ["Nano", "Blk", "Wht"],
    "Street": ["Chem", "Blk", "Wht", "AI"],
}
assert len(types) == len(strengths)


if __name__ == "__main__":
    print(t.get_weak_strength(types, strengths))

    cycle_ids, cycles = t.find_all_type_cycles(types, strengths)
    for cycle in sorted(zip(cycle_ids, cycles)):
        print(cycle[1])

    print("Stats:")
    stats = dict.fromkeys(types, 0)
    for ids in cycles:
        for id in ids:
            stats[id] += 1
    print(stats)

    # print(get_dot(types, strengths, colors))
    with open("types.dot", "w") as f:
        f.write(t.get_dot(types, strengths, colors))

    # print(get_table(types, strengths))
    with open("types.md", "w") as f:
        f.write(t.get_table(types, strengths))
