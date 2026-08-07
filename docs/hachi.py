#!/usr/bin/env python3
import tools as t

colors = {
    "Mil": "#E00000",
    "Bio": "#00E000",
    "Tel": "#0060E0",
    "Nano": "#C0E000",
    "Chem": "#8000E0",
    "Blk": "#101010",
    "Wht": "#DDDDDD",
    "AI": "#808080",
    "Street": "#806030",
}
types = list(colors.keys())

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

    with open("hachi.md", "w") as f:
        f.write("## Types Chart\n\n")
        f.write(t.get_table(types, strengths))
        f.write("\n")
        f.write(t.get_mermaid(types, strengths, colors))
        f.write("\n")
        f.write(t.get_type_cycles_markdown(types, strengths))
