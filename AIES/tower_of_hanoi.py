"""
================================================================================
TOWER OF HANOI PUZZLE USING RECURSION (DIVIDE AND CONQUER)
================================================================================

PREREQUISITES:
- Python 3.x is required.
- External Libraries: NONE!
  Standard Python recursion is used.
  No `pip install` commands are needed.

HOW TO RUN:
  Open terminal in this directory and execute:
      python tower_of_hanoi.py

PROBLEM FORMULATION & RULES:
  - Consists of three rods (pegs): Source ('A'), Auxiliary ('B'), Destination ('C').
  - 'n' disks of distinct diameters initially stacked on Source in decreasing size.
  - Objective: Move the entire stack of 'n' disks from Source to Destination.
  - Constraints:
      1. Only one disk can be moved at a time.
      2. Each move consists of taking the upper disk from one stack and placing
         it on top of another stack.
      3. No disk may be placed on top of a smaller disk.
  - Mathematical Properties:
      Total moves required for n disks = 2^n - 1.
================================================================================
"""

# ==============================================================================
# SECTION 1: RECURSIVE SOLVER FUNCTION
# ==============================================================================
def towerOfHanoi(n, source, auxiliary, destination):
    """
    Solves Tower of Hanoi for `n` disks using Divide and Conquer recursion.
    
    Parameters:
      n (int): Number of disks to move.
      source (str): Label of rod where disks currently reside (e.g., 'A').
      auxiliary (str): Label of intermediate helper rod (e.g., 'B').
      destination (str): Label of target destination rod (e.g., 'C').
    """
    # BASE CASE: Only 1 disk remaining
    # Move disk 1 directly from source rod to destination rod
    if n == 1:
        print(f"Move Disk 1 from Rod {source} -> Rod {destination}")
        return

    # STEP 1: Move top (n - 1) disks from Source to Auxiliary rod
    # (using Destination rod as temporary helper)
    towerOfHanoi(n - 1, source, destination, auxiliary)

    # STEP 2: Move the remaining largest disk (Disk n) directly from Source to Destination
    print(f"Move Disk {n} from Rod {source} -> Rod {destination}")

    # STEP 3: Move the (n - 1) disks from Auxiliary rod to Destination rod
    # (using Source rod as temporary helper)
    towerOfHanoi(n - 1, auxiliary, source, destination)


# ==============================================================================
# SECTION 2: DRIVER CODE / USER INPUT
# ==============================================================================
if __name__ == "__main__":
    n = int(input("Enter the number of disks: "))

    print(f"\n--- Minimum Moves Required: {2**n - 1} ---")
    print(f"Sequence of moves to transfer {n} disks from Peg A to Peg C:\n")

    # Peg A = Source, Peg B = Auxiliary (Helper), Peg C = Destination
    towerOfHanoi(n, 'A', 'B', 'C')
