#!/usr/bin/env python3
from ortools.sat.python import cp_model


def find_all_type_cycles(types, strengths):
    """
    Finds all 3-type cycles where type1 is strong against type2,
    type2 is strong against type3, and type3 is strong against type1.
    """
    assert len(types) == len(strengths)
    type_to_int = {type: idx for idx, type in enumerate(types)}

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
            allowed_assignments.append((type_to_int[attacker], type_to_int[defender]))

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
            self.solution_ids.append(tuple(self.Value(v) for v in self.__variables))

    solution_collector = SolutionCollector([type1, type2, type3])
    status = solver.SearchForAllSolutions(model, solution_collector)

    print(f"Status: {solver.StatusName(status)}")
    print(f"Found {len(solution_collector.solutions)} 3-types cycles.")
    return solution_collector.solution_ids, solution_collector.solutions


def get_type_chart_markdown(types, strengths, colors=None):
    """
    Generates a Mermaid flowchart in Markdown representing the type strengths graph,
    with optional node fill colors.
    """
    assert len(types) == len(strengths)
    if colors:
        assert len(types) == len(colors)
    ret = "```mermaid\nflowchart TD\n"
    for t in types:
        ret += f"    {t}[{t}]\n"
    for t1 in types:
        for t2 in strengths[t1]:
            ret += f"    {t1} --> {t2}\n"
    if colors:
        if isinstance(colors, dict):
            for t in types:
                if t in colors:
                    ret += f"    style {t} color:{colors[t][0]},fill:{colors[t][1]}\n"
        else:
            for t, c in zip(types, colors):
                ret += f"    style {t} fill:{c}\n"
    ret += "```\n"
    return ret


def get_type_table_markdown(types, strengths):
    """
    Generates a 2D Markdown table matrix showing super-effective matchups ('X')
    between attacker (row) and defender (column) types.
    """
    assert len(types) == len(strengths)
    ret = "| A \\ D  "
    for t in types:
        ret += f"| {t:^6} "
    ret += "|\n"
    ret += "| ------ " * (len(types) + 1) + "|\n"

    for atk in types:
        ret += f"| {atk:^6} "
        for defenser in types:
            ret += f"| {'X' if defenser in strengths[atk] else '.':^6} "
        ret += "|\n"
    return ret


def get_type_weak_strength_markdown(types, strengths):
    """
    Generates a summary string listing for each type the list of types it is
    weak to (incoming) and strong against (outgoing).
    """
    assert len(types) == len(strengths)
    ret = ""
    for i in types:
        ret += (
            f"{[j for j in types if i in strengths[j]]}"
            + f" > **{i}** > {strengths[i]}\n"
        )
    return ret


def get_stats_markdown(types, strengths):
    """
    Generates a Markdown table summarizing each type's incoming weaknesses,
    outgoing strengths, and number of 3-type cycles it participates in.
    """
    assert len(types) == len(strengths)
    _, cycles = find_all_type_cycles(types, strengths)
    stats = dict.fromkeys(types, 0)
    for cycle in cycles:
        for t in cycle:
            stats[t] += 1

    ret = "## Type Stats\n\n"
    ret += "| Type | Weak To (Incoming) | Strong Against (Outgoing) | 3-Type Cycles |\n"
    ret += "| :--- | :--- | :--- | :---: |\n"
    for t in types:
        weak_to = [j for j in types if t in strengths[j]]
        strong_vs = strengths[t]
        weak_str = (
            f"{', '.join(f'`{x}`' for x in weak_to)} ({len(weak_to)})"
            if weak_to
            else "*(None)* (0)"
        )
        strong_str = (
            f"{', '.join(f'`{x}`' for x in strong_vs)} ({len(strong_vs)})"
            if strong_vs
            else "*(None)* (0)"
        )
        ret += f"| **`{t}`** | {weak_str} | {strong_str} | **{stats[t]}** |\n"
    return ret


def get_type_cycles_markdown(types, strengths):
    """
    Generates a Markdown section listing all 3-type cycles found in the
    type strengths graph.
    """
    cycle_ids, cycles = find_all_type_cycles(types, strengths)
    ret = f"## Type Cycles\n\nFound {len(cycles)} 3-type cycles:\n\n"
    for _, cycle in sorted(zip(cycle_ids, cycles)):
        ret += f"- {' -> '.join(cycle)} -> {cycle[0]}\n"
    return ret
