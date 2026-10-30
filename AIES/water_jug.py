"""
================================================================================
WATER JUG PROBLEM USING DEPTH-FIRST SEARCH (DFS)
================================================================================

PREREQUISITES:
- Python 3.x is required.
- External Libraries: NONE!
  Standard Python built-ins (recursion, sets, tuples).
  No `pip install` commands are needed.

HOW TO RUN:
  Open terminal in this directory and execute:
      python water_jug.py

PROBLEM FORMULATION:
  - Given two jugs with capacities `jug1` and `jug2` liters.
  - Neither jug has measuring markings. An infinite water supply is available.
  - Goal: Measure exactly `target` liters of water into Jug 1.
  
POSSIBLE STATE TRANSITIONS (PRODUCTION RULES):
  1. Fill Jug 1 completely: (jug1, j2)
  2. Fill Jug 2 completely: (j1, jug2)
  3. Empty Jug 1 completely: (0, j2)
  4. Empty Jug 2 completely: (j1, 0)
  5. Pour Jug 1 into Jug 2 until Jug 2 is full or Jug 1 is empty.
  6. Pour Jug 2 into Jug 1 until Jug 1 is full or Jug 2 is empty.

MATHEMATICAL SOLVABILITY:
  A solution exists if and only if target <= jug1 and target is a multiple 
  of gcd(jug1, jug2).
================================================================================
"""

# ==============================================================================
# SECTION 1: GLOBAL STATE TRACKING
# ==============================================================================
# Set storing tuples (j1, j2) of previously visited jug volumes to prevent infinite loops
visited = set()


# ==============================================================================
# SECTION 2: DEPTH-FIRST SEARCH (DFS) SOLVER
# ==============================================================================
def waterJugDFS(j1, j2, jug1, jug2, target):
    """
    Recursively searches for a state sequence where Jug 1 contains `target` liters.
    
    Parameters:
      j1 (int): Current amount of water in Jug 1.
      j2 (int): Current amount of water in Jug 2.
      jug1 (int): Maximum capacity of Jug 1.
      jug2 (int): Maximum capacity of Jug 2.
      target (int): Desired amount of water in Jug 1.
      
    Returns:
      bool: True if target amount is reached, False otherwise.
    """
    # CYCLE DETECTION: If state has already been visited, prune this branch
    if (j1, j2) in visited:
        return False

    # Mark current state (j1, j2) as visited
    visited.add((j1, j2))

    # Print the current state
    print(f"Current State: Jug 1 = {j1}L, Jug 2 = {j2}L")

    # GOAL TEST: Check if Jug 1 has achieved target volume
    if j1 == target:
        print(f"\nTarget of {target}L reached in Jug 1!")
        return True

    # GENERATE ALL POSSIBLE TRANSITIONS:
    # -------------------------------------------------------------
    # Calculate amount to pour from Jug 1 into Jug 2 without overflowing Jug 2
    pour_j1_to_j2 = min(j1, jug2 - j2)

    # Calculate amount to pour from Jug 2 into Jug 1 without overflowing Jug 1
    pour_j2_to_j1 = min(j2, jug1 - j1)

    states = [
        (jug1, j2),                            # Rule 1: Fill Jug 1
        (j1, jug2),                            # Rule 2: Fill Jug 2
        (0, j2),                               # Rule 3: Empty Jug 1
        (j1, 0),                               # Rule 4: Empty Jug 2
        (j1 - pour_j1_to_j2, j2 + pour_j1_to_j2), # Rule 5: Pour Jug 1 -> Jug 2
        (j1 + pour_j2_to_j1, j2 - pour_j2_to_j1)  # Rule 6: Pour Jug 2 -> Jug 1
    ]

    # EXPLORE NEIGHBOR STATES RECURSIVELY (DFS)
    for next_j1, next_j2 in states:
        if waterJugDFS(next_j1, next_j2, jug1, jug2, target):
            return True

    return False


# ==============================================================================
# SECTION 3: DRIVER CODE / USER INPUT
# ==============================================================================
if __name__ == "__main__":
    jug1 = int(input("Enter capacity of Jug 1: "))
    jug2 = int(input("Enter capacity of Jug 2: "))
    target = int(input("Enter target amount for Jug 1: "))

    print("\n--- State Space Traversal (DFS) ---")

    # Start search from initial state: both jugs empty (0, 0)
    if not waterJugDFS(0, 0, jug1, jug2, target):
        print("\nNo Solution Exists for the given jug capacities and target.")
