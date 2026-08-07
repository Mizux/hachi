#!/usr/bin/env python3
import tools as t

colors = {
    "Normal": "#C06040",
    "Fire": "#E00000",
    "Grass": "#00E000",
    "Water": "#0000E0",
    "Electric": "#F0F000",
    "Ice": "#40F0F0",
    "Fighting": "#806030",
    "Poison": "#8000E0",
    "Ground": "#806030",
    "Flying": "#C08060",
    "Psychic": "#FF8000",
    "Bug": "#008040",
    "Rock": "#404040",
    "Ghost": "#D0D0D0",
    "Dragon": "#C0E000",
    "Dark": "#202020",
    "Steel": "#808080",
    "Fairy": "#E050C0",
}
types = list(colors.keys())

# Based on the official Pokemon type chart
strengths = {
    "Normal": [],
    "Fire": ["Grass", "Ice", "Bug", "Steel"],
    "Grass": ["Water", "Ground", "Rock"],
    "Water": ["Fire", "Ground", "Rock"],
    "Electric": ["Water", "Flying"],
    "Ice": ["Grass", "Ground", "Flying", "Dragon"],
    "Fighting": ["Normal", "Ice", "Rock", "Dark", "Steel"],
    "Poison": ["Grass", "Fairy"],
    "Ground": ["Fire", "Electric", "Poison", "Rock", "Steel"],
    "Flying": ["Grass", "Fighting", "Bug"],
    "Psychic": ["Fighting", "Poison"],
    "Bug": ["Grass", "Psychic", "Dark"],
    "Rock": ["Fire", "Ice", "Flying", "Bug"],
    "Ghost": ["Psychic", "Ghost"],
    "Dragon": ["Dragon"],
    "Dark": ["Psychic", "Ghost"],
    "Steel": ["Ice", "Rock", "Fairy"],
    "Fairy": ["Fighting", "Dragon", "Dark"],
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

    with open("pkm.md", "w") as f:
        f.write("## Types Chart\n\n")
        f.write(t.get_table(types, strengths))
        f.write("\n")
        f.write(t.get_mermaid(types, strengths, colors))
        f.write("\n")
        f.write(t.get_type_cycles_markdown(types, strengths))
