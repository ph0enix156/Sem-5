"""
================================================================================
UNBEATABLE TIC-TAC-TOE AI USING THE MINIMAX ALGORITHM
================================================================================

PREREQUISITES:
- Python 3.x is required.
- External Libraries: NONE!
  Uses standard Python built-ins.
  No `pip install` commands are needed.

HOW TO RUN:
  Open terminal in this directory and execute:
      python minmax_tictactoe.py

HOW TO PLAY:
  - The board is a 3x3 grid numbered 1 through 9:
        1 | 2 | 3
        ---------
        4 | 5 | 6
        ---------
        7 | 8 | 9
  - You play as 'X' (First turn).
  - Computer AI plays as 'O' (Minimax AI, provably unbeatable).
  - Enter numbers 1 to 9 to place your mark on the board.

MINIMAX ALGORITHM OVERVIEW:
  - Game theory decision rule for two-player zero-sum games.
  - Terminal Utility Scores:
      * AI ('O') wins:  +1 (Maximizer)
      * Human ('X') wins: -1 (Minimizer)
      * Draw / Tie:       0 (Neutral)
  - Maximizer seeks the move with maximum score; Minimizer seeks the lowest score.
================================================================================
"""

# ==============================================================================
# SECTION 1: GAME BOARD & DISPLAY
# ==============================================================================
# Board representation: 9 elements initialized to blank space ' '
b = [" "] * 9


def display():
    """Prints the current 3x3 Tic-Tac-Toe board to standard console output."""
    print()
    for i in range(0, 9, 3):
        print(f" {b[i]} | {b[i+1]} | {b[i+2]} ")
        if i < 6:
            print("-----------")
    print()


# ==============================================================================
# SECTION 2: WIN CONDITION CHECKER
# ==============================================================================
def win(p):
    """
    Checks if player `p` ('X' or 'O') has achieved 3 marks in a line.
    
    Parameters:
      p (str): Player mark ('X' or 'O').
      
    Returns:
      bool: True if player has won, False otherwise.
    """
    # All 8 possible winning lines: 3 rows, 3 columns, 2 diagonals
    lines = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical columns
        (0, 4, 8), (2, 4, 6)              # Diagonals
    ]

    for a, c, d in lines:
        if b[a] == b[c] == b[d] == p:
            return True
    return False


# ==============================================================================
# SECTION 3: MINIMAX ALGORITHM (RECURSIVE DECISION ENGINE)
# ==============================================================================
def minimax(p):
    """
    Recursively simulates all possible game outcomes to evaluate board positions.
    
    Parameters:
      p (str): Current player taking turn in simulation ('O' = AI, 'X' = Human).
      
    Returns:
      int: Static evaluation score (+1 for AI win, -1 for Human win, 0 for Draw).
    """
    # 1. TERMINAL STATE CHECKS
    if win("O"):
        return 1   # AI won (+1)
    if win("X"):
        return -1  # Human won (-1)
    if " " not in b:
        return 0   # Board full, game is a Draw (0)

    # 2. INITIALIZE WORST-CASE SCORE
    # Maximizer ('O') starts at -infinity (-2), Minimizer ('X') starts at +infinity (+2)
    best = -2 if p == "O" else 2

    # 3. EXPLORE ALL EMPTY CELLS
    for i in range(9):
        if b[i] == " ":
            # Try placing the mark
            b[i] = p

            # Switch turns for next recursion level
            next_p = "X" if p == "O" else "O"
            score = minimax(next_p)

            # Undo move (Backtrack)
            b[i] = " "

            # 4. OPTIMIZE SCORE BASED ON PLAYER GOAL
            if p == "O":
                best = max(best, score)  # AI maximizes score
            else:
                best = min(best, score)  # Human minimizer minimizes score

    return best


# ==============================================================================
# SECTION 4: MAIN GAME PLAY LOOP
# ==============================================================================
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print("You are 'X', Computer is 'O'.")

    while True:
        display()

        # --- USER TURN ---
        try:
            m = int(input("Enter your move (1-9): ")) - 1
            if m < 0 or m > 8 or b[m] != " ":
                print("Invalid move! Pick an empty cell between 1 and 9.")
                continue
        except ValueError:
            print("Please enter a valid integer (1-9).")
            continue

        b[m] = "X"

        # Check Human Win
        if win("X"):
            display()
            print("Congratulations! You won!")
            break

        # Check Draw after user move
        if " " not in b:
            display()
            print("It's a Draw!")
            break

        # --- COMPUTER AI TURN ---
        print("Computer is thinking...")
        best, move = -2, -1

        # Test every legal move and find the one with the maximum minimax score
        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                score = minimax("X")  # Evaluate position assuming Human plays optimally next
                b[i] = " "

                if score > best:
                    best, move = score, i

        # Execute optimal computer move
        b[move] = "O"

        # Check Computer Win
        if win("O"):
            display()
            print("Computer wins! Better luck next time.")
            break

        # Check Draw after computer move
        if " " not in b:
            display()
            print("It's a Draw!")
            break


if __name__ == "__main__":
    play_game()
