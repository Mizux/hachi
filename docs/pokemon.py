#!/usr/bin/env python3
import tools as t

types = [
    "Normal",
    "Fire",
    "Grass",
    "Water",
    "Electric",
    "Ice",
    "Fighting",
    "Poison",
    "Ground",
    "Flying",
    "Psychic",
    "Bug",
    "Rock",
    "Ghost",
    "Dragon",
    "Dark",
    "Steel",
    "Fairy",
]

colors = [
   '#C06040', # Normal
   '#E00000', # Fire
   '#00E000', # Grass
   '#0000E0', # Water
   '#F0F000', # Electric
   '#40F0F0', # Ice
   '#806030', # Fighting
   '#8000E0', # Poison
   '#806030', # Ground
   '#C08060', # Flying
   '#FF8000', # Psychic
   '#008040', # Bug
   '#404040', # Rock
   '#D0D0D0', # Ghost
   '#C0E000', # Dragon
   '#202020', # Dark
   '#808080', # Steel
   '#E050C0', # Fairy
]
assert len(types) == len(colors)

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

    # print(get_dot(types, strengths, colors))
    with open("pkm.dot", "w") as f:
        f.write(t.get_dot(types, strengths, colors))

    # print(get_table(types, strengths))
    with open("pkm.md", "w") as f:
        f.write(t.get_table(types, strengths))
