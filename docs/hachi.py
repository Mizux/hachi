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
    "Corp": "#E050C0",
    "Mech": "#404040",
}
types = list(colors.keys())

strengths = {
    "Mil": ["Bio", "AI", "Street", "Mech"],
    "Bio": ["Tel", "Blk", "Wht", "Street"],
    "Tel": ["Mil", "Nano", "AI", "Street", "Corp"],
    "Nano": ["Mil", "Bio", "Nano", "Chem", "Street", "Mech"],
    "Chem": ["Mil", "Bio", "Corp", "Mech"],
    "Blk": ["Tel", "Nano", "Wht", "Mil", "Corp"],
    "Wht": ["Tel", "Nano", "Blk", "Mil"],
    "AI": ["Nano", "Blk", "Wht", "Corp", "Mech"],
    "Street": ["Chem", "Blk", "Wht", "AI"],
    "Corp": ["Mil", "Wht", "Street", "Mech"],
    "Mech": ["Bio", "Tel"],
}
assert len(types) == len(strengths)


if __name__ == "__main__":
    print(t.get_type_weak_strength_markdown(types, strengths))

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
        f.write(t.get_type_table_markdown(types, strengths))
        f.write("\n")
        f.write(t.get_type_chart_markdown(types, strengths, colors))
        f.write("\n")
        f.write(t.get_stats_markdown(types, strengths))
        f.write("\n")
        f.write(t.get_type_cycles_markdown(types, strengths))
