"""
================================================================================
MAP / GRAPH COLOURING PROBLEM USING CSP & BACKTRACKING
================================================================================

PREREQUISITES:
- Python 3.x is required.
- External Libraries: NONE!
  Uses standard Python dictionaries and lists.
  No `pip install` commands are needed.

HOW TO RUN:
  Open terminal in this directory and execute:
      python map_colouring.py

PROBLEM FORMULATION (CSP - CONSTRAINT SATISFACTION PROBLEM):
  - Variables (V): Regions / Nodes to be coloured -> {'A', 'B', 'C', 'D'}.
  - Domains (D): Set of available colours for each region -> {'Red', 'Green', 'Blue'}.
  - Constraints (C): No two adjacent (neighbouring) regions may share the same colour.
      Example: If A is connected to B, colour(A) != colour(B).

ALGORITHM (BACKTRACKING SEARCH):
  - A depth-first search that chooses a variable, assigns a valid domain value,
    and checks consistency.
  - If a dead-end is encountered (no valid colour left for a neighbour),
    it undoes the assignment (backtracks) and tries the next colour.
================================================================================
"""

# ==============================================================================
# SECTION 1: PROBLEM DEFINITION (GRAPH & DOMAINS)
# ==============================================================================
# Adjacency list representing connected neighbouring regions
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

# Domain: Available palette of colours
colours = ['Red', 'Green', 'Blue']

# State tracker: Stores final colour assignments {region: colour}
colour_map = {}


# ==============================================================================
# SECTION 2: CONSTRAINT CHECKING FUNCTION
# ==============================================================================
def is_valid(region, colour):
    """
    Checks if assigning `colour` to `region` violates the adjacency constraint.
    
    Parameters:
      region (str): The node being assigned a colour.
      colour (str): The candidate colour from the domain.
      
    Returns:
      bool: True if no adjacent neighbor has the same colour, False otherwise.
    """
    for neighbour in graph[region]:
        # If neighbor is already coloured and has the same candidate colour, invalid
        if colour_map.get(neighbour) == colour:
            return False
    return True


# ==============================================================================
# SECTION 3: RECURSIVE BACKTRACKING SOLVER
# ==============================================================================
def solve():
    """
    Recursively colours regions using backtracking search.
    
    Returns:
      bool: True if all regions are successfully coloured without conflicts,
            False if no valid assignment is possible.
    """
    # BASE CASE: All regions in the graph have been assigned a colour
    if len(colour_map) == len(graph):
        return True

    # VARIABLE SELECTION: Pick the first uncoloured region
    region = next(r for r in graph if r not in colour_map)

    # VALUE ASSIGNMENT: Try each colour from domain
    for colour in colours:
        # Check if candidate colour satisfies consistency constraints
        if is_valid(region, colour):
            # Assign colour to current region
            colour_map[region] = colour

            # Recursively assign colours to remaining regions
            if solve():
                return True

            # BACKTRACK: If assignment leads to a dead end, remove assignment
            del colour_map[region]

    return False


# ==============================================================================
# SECTION 4: MAIN EXECUTION / OUTPUT
# ==============================================================================
if __name__ == "__main__":
    print("Solving Map Colouring Problem for regions A, B, C, D...")
    print(f"Available Colours: {colours}\n")

    if solve():
        print("--- Map Colouring Solution Found ---")
        for region, colour in sorted(colour_map.items()):
            print(f"  Region {region} -> {colour}")
    else:
        print("No valid colouring solution exists for the given graph and colours.")
