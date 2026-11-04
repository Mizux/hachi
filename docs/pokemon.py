#!/usr/bin/env python3
import tools as t

colors = {
    "Normal": ("#111","#C06040"),
    "Fire": ("#111","#E02020"),
    "Grass": ("#111","#20A040"),
    "Water": ("#DDD","#0080E0"),
    "Electric": ("#111","#F0F000"),
    "Ice": ("#111","#40F0F0"),
    "Fighting": ("#111","#806030"),
    "Poison": ("#080","#8000E0"),
    "Ground": ("#111","#806030"),
    "Flying": ("#111","#C08060"),
    "Psychic": ("#111","#F050A0"),
    "Bug": ("#111","#008040"),
    "Rock": ("#111","#404040"),
    "Ghost": ("#111","#D0D0D0"),
    "Dragon": ("#111","#C0E000"),
    "Dark": ("#FF0","#202020"),
    "Steel": ("#111","#808080"),
    "Fairy": ("#111","#E050C0"),
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

    with open("pkm.md", "w") as f:
        f.write("## Types Chart\n\n")
        f.write(t.get_type_table_markdown(types, strengths))
        f.write("\n")
        f.write(t.get_type_chart_markdown(types, strengths, colors))
        f.write("\n")
        f.write(t.get_stats_markdown(types, strengths))
        f.write("\n")
        f.write(t.get_type_cycles_markdown(types, strengths))
