"""
================================================================================
8-PUZZLE SOLVER USING A* SEARCH ALGORITHM
================================================================================

PREREQUISITES:
- Python 3.x is required.
- External Libraries: NONE!
  The `queue` module used here is part of Python's standard library.
  No `pip install` commands are needed.
  
HOW TO RUN:
  Open terminal in this directory and run:
      python astar.py

HOW TO ENTER INPUT:
  Enter the 3x3 grid line-by-line using numbers separated by spaces.
  Use `0` to represent the blank tile.
  Example:
      1 2 3
      4 0 5
      7 8 6
================================================================================
"""

# ==============================================================================
# SECTION 1: IMPORTS
# ==============================================================================
# PriorityQueue is part of Python's built-in standard library (no installation needed).
# It retrieves items in ascending order based on priority: (f_score, g_score, state).
from queue import PriorityQueue


# ==============================================================================
# SECTION 2: INPUT FUNCTION
# ==============================================================================
def read():
    """
    Reads a 3x3 matrix from standard console input.
    Each row expects 3 space-separated integers.
    Returns: A 2D list of integers (3x3 grid).
    """
    return [list(map(int, input().split())) for i in range(3)]


# ==============================================================================
# SECTION 3: HEURISTIC FUNCTION - Misplaced Tiles (h)
# ==============================================================================
def h(s, goal):
    """
    Calculates the heuristic value h(n) for state `s`.
    
    Heuristic used: Count of misplaced tiles compared to the goal state.
    Note: The blank tile (0) is ignored in this count according to standard rules.
    
    Parameters:
      s: The current 3x3 grid state.
      goal: The target 3x3 goal state.
      
    Returns:
      count: Number of non-zero tiles not in their target positions.
    """
    count = 0
    for i in range(3):
        for j in range(3):
            # Check if tile is not the blank space (0) and does not match the goal
            if s[i][j] != 0 and s[i][j] != goal[i][j]:
                count += 1
    return count


# ==============================================================================
# SECTION 4: A* SEARCH ALGORITHM
# ==============================================================================
def astar(start, goal):
    """
    Performs A* search to solve the 8-puzzle from `start` to `goal`.
    
    A* Formula:
        f(n) = g(n) + h(n)
        where:
          g(n) = Actual cost from start node to current node (number of moves)
          h(n) = Estimated heuristic cost from current node to goal
          f(n) = Total estimated cost through node n
    """
    # Initialize the Open List as a Priority Queue
    pq = PriorityQueue()
    
    # Push initial state into priority queue: (f_cost, g_cost, state)
    # At start: g = 0, so f = h(start, goal)
    pq.put((h(start, goal), 0, start))
    
    # Closed list: stores states that have already been explored
    visited = []

    # Loop until all reachable states are exhausted or goal is reached
    while not pq.empty():
        # Pop the state with the lowest total estimated cost f(n)
        f, g, s = pq.get()

        # Skip this state if it has already been evaluated
        if s in visited:
            continue
        visited.append(s)

        # Print current visited state and its evaluation metrics
        print("Visited State:")
        for row in s:
            print(row)
        print("f =", f, "g =", g, "h =", h(s, goal))
        print()

        # Goal Test: Check if current state matches the goal state
        if s == goal:
            print("Goal Reached!")
            return

        # Locate the coordinates (x, y) of the blank tile (0)
        x, y = 0, 0
        for i in range(3):
            for j in range(3):
                if s[i][j] == 0:
                    x, y = i, j

        # Possible directions to slide tiles into the blank spot:
        # (-1, 0) -> Up, (1, 0) -> Down, (0, -1) -> Left, (0, 1) -> Right
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Explore all 4 possible neighbor moves
        for dx, dy in moves:
            nx = x + dx
            ny = y + dy

            # Check boundary conditions: new position must remain inside the 3x3 grid
            if 0 <= nx < 3 and 0 <= ny < 3:
                # Create a deep copy of the current grid state
                new = [row[:] for row in s]

                # Swap the blank tile (0) with the adjacent tile
                new[x][y], new[nx][ny] = new[nx][ny], new[x][y]

                # If this new configuration has not been visited yet, add to open list
                if new not in visited:
                    ng = g + 1                     # Increment path cost by 1
                    nh = h(new, goal)              # Calculate heuristic for new state
                    pq.put((ng + nh, ng, new))     # Push (f = ng + nh, g = ng, state)

    print("No Solution Found")


# ==============================================================================
# SECTION 5: DRIVER CODE / MAIN EXECUTION
# ==============================================================================
if __name__ == "__main__":
    print("Enter Initial State (0 = Blank):")
    start = read()

    print("Enter Goal State:")
    goal = read()

    astar(start, goal)
