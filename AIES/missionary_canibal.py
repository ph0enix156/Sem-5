"""
================================================================================
MISSIONARIES AND CANNIBALS PROBLEM USING DEPTH-FIRST SEARCH (DFS)
================================================================================

PREREQUISITES:
- Python 3.x is required.
- External Libraries: NONE!
  Uses standard Python sets, tuples, and functions.
  No `pip install` commands are needed.

HOW TO RUN:
  Open terminal in this directory and execute:
      python missionary_canibal.py

PROBLEM FORMULATION:
  - Total Missionaries (M) and Cannibals (C) initially start on the Left Bank.
  - Objective: Transport all M and C to the Right Bank using a boat that carries
    at most 2 people (and at least 1 person to row).
  - Safety Constraint: At no point on either river bank can Cannibals outnumber
    Missionaries (if Missionaries are present), otherwise they get eaten!
      * On Left Bank:  if ml > 0, then cl <= ml
      * On Right Bank: if mr > 0, then cr <= mr

ALGORITHM (DEPTH-FIRST SEARCH):
  - Explores state transitions recursively.
  - Maintains a `visited` set to prevent infinite loops / cycles.
  - Backtracks if an unsafe state or dead end is reached.
================================================================================
"""

# ==============================================================================
# SECTION 1: GLOBAL STATE VARIABLES
# ==============================================================================
# Set to track visited states: stores tuples (ml, cl, boat)
visited = set()

# Total counts entered by the user
TOTAL_M = 0
TOTAL_C = 0


# ==============================================================================
# SECTION 2: SAFETY & VALIDITY CHECK FUNCTION
# ==============================================================================
def isValid(ml, cl, mr, cr):
    """
    Validates if a given state satisfies all safety and capacity constraints.
    
    Parameters:
      ml (int): Number of missionaries on the left bank.
      cl (int): Number of cannibals on the left bank.
      mr (int): Number of missionaries on the right bank.
      cr (int): Number of cannibals on the right bank.
      
    Returns:
      bool: True if state is valid and safe, False otherwise.
    """
    # 1. Negative count check
    if ml < 0 or cl < 0 or mr < 0 or cr < 0:
        return False

    # 2. Maximum limit check
    if ml > TOTAL_M or cl > TOTAL_C or mr > TOTAL_M or cr > TOTAL_C:
        return False

    # 3. Left bank safety: Cannibals cannot outnumber missionaries
    if ml > 0 and cl > ml:
        return False

    # 4. Right bank safety: Cannibals cannot outnumber missionaries
    if mr > 0 and cr > mr:
        return False

    return True


# ==============================================================================
# SECTION 3: DEPTH-FIRST SEARCH (DFS) TRAVERSAL
# ==============================================================================
def missionaryCannibalDFS(ml, cl, boat):
    """
    Explores the state space recursively to find a safe path to the goal.
    
    Parameters:
      ml (int): Missionaries on left bank.
      cl (int): Cannibals on left bank.
      boat (int): Boat location (0 = Left bank, 1 = Right bank).
      
    Returns:
      bool: True if goal reached along this branch, False otherwise.
    """
    # Calculate counts on right bank from conservation of people
    mr = TOTAL_M - ml
    cr = TOTAL_C - cl

    # Cycle Detection: Skip if this exact state has already been visited
    if (ml, cl, boat) in visited:
        return False

    # Mark current state as visited
    visited.add((ml, cl, boat))

    # Print the current step in the solution path
    side = "Left" if boat == 0 else "Right"
    print(f"Left: ({ml}M, {cl}C) | Right: ({mr}M, {cr}C) | Boat at: {side}")

    # GOAL TEST: All missionaries and cannibals are on right bank (ml=0, cl=0, boat=Right)
    if ml == 0 and cl == 0 and boat == 1:
        print("\nGoal Reached! All individuals safely crossed the river.")
        return True

    # Possible boat passengers: (missionaries, cannibals) - max capacity is 2, min is 1
    moves = [
        (1, 0),  # 1 Missionary crosses
        (2, 0),  # 2 Missionaries cross
        (0, 1),  # 1 Cannibal crosses
        (0, 2),  # 2 Cannibals cross
        (1, 1)   # 1 Missionary and 1 Cannibal cross
    ]

    # Try all possible transitions from current state
    for m, c in moves:
        if boat == 0:
            # Boat moves from Left to Right
            newML = ml - m
            newCL = cl - c
            newBoat = 1
        else:
            # Boat returns from Right to Left
            newML = ml + m
            newCL = cl + c
            newBoat = 0

        newMR = TOTAL_M - newML
        newCR = TOTAL_C - newCL

        # Verify whether new state is safe and within bounds
        if isValid(newML, newCL, newMR, newCR):
            # Recurse down this branch
            if missionaryCannibalDFS(newML, newCL, newBoat):
                return True

    return False


# ==============================================================================
# SECTION 4: DRIVER CODE / USER INPUT
# ==============================================================================
if __name__ == "__main__":
    TOTAL_M = int(input("Enter number of Missionaries (typically 3): "))
    TOTAL_C = int(input("Enter number of Cannibals (typically 3): "))

    print("\n--- Missionaries and Cannibals State Space Traversal (DFS) ---\n")

    # Start DFS with all M and C on Left Bank (boat = 0)
    if not missionaryCannibalDFS(TOTAL_M, TOTAL_C, 0):
        print("\nNo Solution Exists for the given numbers.")
