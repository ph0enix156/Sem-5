"""
================================================================================
CRYPTARITHMETIC PUZZLE SOLVER (CSP USING BACKTRACKING)
================================================================================

PREREQUISITES:
- Python 3.x is required.
- External Libraries: NONE!
  Uses only built-in Python data types (sets, dicts, lists).
  No `pip install` commands are needed.

HOW TO RUN:
  Open terminal in this directory and execute:
      python cryptarithmetic.py

HOW IT WORKS:
  - Cryptarithmetic is a Constraint Satisfaction Problem (CSP) where letters 
    represent unique decimal digits (0-9).
  - Formula: Word1 + Word2 = ResultWord (e.g., SEND + MORE = MONEY)
  - Constraints:
      1. Each letter maps to a unique digit (0-9).
      2. No two distinct letters share the same digit.
      3. Leading letters of any word cannot be zero (0).
      4. Total unique letters cannot exceed 10 (since digits are 0-9).
  - Uses Backtracking Search: assigns digits recursively, backtracks on conflict.
================================================================================
"""

# ==============================================================================
# SECTION 1: USER INPUT & INITIALIZATION
# ==============================================================================
# Read three words representing the equation: w1 + w2 = w3
w1 = input("First word: ").strip().upper()
w2 = input("Second word: ").strip().upper()
w3 = input("Result word: ").strip().upper()

# Extract all unique characters across all three words
letters = list(set(w1 + w2 + w3))

# Dictionary mapping each letter to its assigned digit: {'S': 9, 'E': 5, ...}
d = {}


# ==============================================================================
# SECTION 2: HELPER FUNCTION - WORD TO NUMBER CONVERSION
# ==============================================================================
def num(w):
    """
    Converts a word into its numerical value based on current letter assignments in dict `d`.
    Example: If w='SEND' and d={'S':9, 'E':5, 'N':6, 'D':7}, returns integer 9567.
    """
    return int("".join(str(d[c]) for c in w))


# ==============================================================================
# SECTION 3: BACKTRACKING SOLVER (CSP)
# ==============================================================================
def solve(i):
    """
    Recursively assigns digits (0-9) to letters[i] using backtracking.
    
    Parameters:
      i (int): Index of the current letter in the `letters` list to be assigned.
      
    Returns:
      bool: True if a valid assignment exists satisfying the arithmetic equation, False otherwise.
    """
    # BASE CASE: All letters have been assigned a unique digit
    if i == len(letters):
        # Verify if the arithmetic constraint holds: w1 + w2 == w3
        return num(w1) + num(w2) == num(w3)

    # RECURSIVE STEP: Try assigning every possible digit (0 to 9) to letters[i]
    for digit in range(10):
        # Constraint 1: Digit must not already be assigned to another letter (all-different constraint)
        if digit in d.values():
            continue

        # Constraint 2: Leading letters of any operand cannot be assigned 0
        if digit == 0 and letters[i] in (w1[0], w2[0], w3[0]):
            continue

        # Assign candidate digit to current letter
        d[letters[i]] = digit

        # Recurse to assign the next letter (i + 1)
        if solve(i + 1):
            return True

        # BACKTRACK: Undo assignment if it did not lead to a valid solution
        del d[letters[i]]

    return False


# ==============================================================================
# SECTION 4: DRIVER / VALIDATION & EXECUTION
# ==============================================================================
# If there are more than 10 unique letters, it's impossible to solve with base-10 digits
if len(letters) <= 10 and solve(0):
    print("\n--- Solution Found ---")
    for letter, digit in sorted(d.items()):
        print(f"{letter} = {digit}")
    print("\nVerification:")
    print(f"{num(w1)} ({w1}) + {num(w2)} ({w2}) = {num(w3)} ({w3})")
else:
    print("\nNo solution exists (either > 10 unique letters or no valid mapping).")
