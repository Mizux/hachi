#!/usr/bin/env python3
import tools as t

colors = {
    # name: (FG, BG)
    "Mech": ("#111","#E22"),
    "Bio": ("#741","#2A4"),
    "Tel": ("#EE0","#08E"),
    
    "Nano": ("#111","#CE0"),
    "Chem": ("#111","#80E"),
    
    "Hack": ("#0D0","#111"),
    "AI": ("#08E","#111"),
    
    "Corp": ("#D00","#EEE"),
    "Street": ("#111","#863"),
    "Gov": ("#DDD","#039"),
}
types = list(colors.keys())

strengths = {
    "Mech": ["Bio", "Chem"],
    "Bio": ["Tel", "Hack"],
    "Tel": ["Mech", "Nano", "AI"],
    
    "Nano": ["Nano", "Mech", "Bio", "Hack"],
    "Chem": ["Nano", "Bio", "AI", "Hack"],
    
    "Hack": ["Tel", "Mech", "Corp", "Gov"],
    "AI": ["Hack", "Mech", "Nano", "Gov"],
    
    "Corp": ["Corp", "Street", "AI"],
    "Street": ["Gov", "Chem", "Hack"],
    "Gov": ["Corp", "Nano"],
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
