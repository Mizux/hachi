#!/usr/bin/env python3
from ortools.sat.python import cp_model

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
type_to_int = {t: i for i, t in enumerate(types)}

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
assert(len(types) == len(colors))

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
assert(len(types) == len(strengths))


def find_pokemon_type_cycles():
    """
    Finds all 3-type cycles where type1 is strong against type2,
    type2 is strong against type3, and type3 is strong against type1.
    """
    model = cp_model.CpModel()

    # Create variables for the three types in the cycle
    type1 = model.NewIntVar(0, len(types) - 1, "type1")
    type2 = model.NewIntVar(0, len(types) - 1, "type2")
    type3 = model.NewIntVar(0, len(types) - 1, "type3")

    # Ensure the three types are different
    model.AddAllDifferent([type1, type2, type3])

    # Generate a list of all valid "strong against" pairs as integer tuples
    allowed_assignments = []
    for attacker, defenders in strengths.items():
        for defender in defenders:
            allowed_assignments.append(
                (type_to_int[attacker], type_to_int[defender])
            )

    # Constraints: The pairs (t1, t2), (t2, t3), and (t3, t1) must exist
    # in our list of super-effective matchups.
    model.AddAllowedAssignments((type1, type2), allowed_assignments)
    model.AddAllowedAssignments((type2, type3), allowed_assignments)
    model.AddAllowedAssignments((type3, type1), allowed_assignments)

    # break symetry making type1 the lowest id of the chain
    model.Add(type1 < type2)
    model.Add(type1 < type3)

    # --- Solver and Solution Printer ---
    solver = cp_model.CpSolver()

    class SolutionCollector(cp_model.CpSolverSolutionCallback):
        def __init__(self, variables):
            cp_model.CpSolverSolutionCallback.__init__(self)
            self.__variables = variables
            self.solutions = []
            self.solution_ids = []

        def on_solution_callback(self):
            self.solutions.append(
                tuple(f"{types[self.Value(v)]}" for v in self.__variables)
            )
            self.solution_ids.append(
                tuple(self.Value(v) for v in self.__variables)
            )

    solution_collector = SolutionCollector([type1, type2, type3])
    status = solver.SearchForAllSolutions(model, solution_collector)

    print(f"Status: {solver.StatusName(status)}")
    print(f"Found {len(solution_collector.solutions)} 3-types cycles.")
    return solution_collector.solution_ids, solution_collector.solutions 


def get_dot():
    a = r"""@startdot
digraph TypeChart {
  //rankdir=BT;
  rankdir=TD;
"""
    a += """  node [shape=cylinder, style="rounded,filled", color=black, fillcolor=royalblue];\n"""
    for t, c in zip(types, colors):
        a += f"  {t} [label=\"{t}\", fillcolor=\"{c}\"];\n"
    a += "\n  edge [color=red];\n"
    for t1, c in zip(types, colors):
        for t2 in strengths[t1]:
            a += f"  {t1} -> {t2} [label=\">\", color=\"{c}\"];\n"
    a += r"""}
@enddot
"""
    return a


def get_table():
    ret = "| A \\ D  "
    for t in types:
      ret += f"| {t:^6} "
    ret += "|\n"
    ret += "| ------ " * (len(types)+1) + "|\n"

    for atk in types:
        ret += f"| {atk:^6} "
        for defenser in types:
            ret += f"| {'X' if defenser in strengths[atk] else '.':^6} "
        ret += "|\n"
    return ret


def get_weak_strength():
    ret = ""
    for i in types:
        ret += f"{[j for j in types if i in strengths[j]]}" + f" > **{i}** > {strengths[i]}\n"
    return ret


if __name__ == "__main__":
    print(get_weak_strength())

    cycle_ids, cycles = find_pokemon_type_cycles()
    for cycle in sorted(zip(cycle_ids,cycles)):
        print(cycle[1])

    print("Stats:")
    stats = dict.fromkeys(types, 0)
    for ids in cycles:
        for id in ids:
          stats[id] += 1
    print(stats)

    #print(get_dot())
    with open('pkm.dot', 'w') as f:
        f.write(get_dot())

    #print(get_table())
    with open('pkm.md', 'w') as f:
        f.write(get_table())
