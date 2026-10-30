"""
================================================================================
TRAVELING SALESPERSON PROBLEM (TSP) USING HILL CLIMBING
================================================================================

PREREQUISITES:
- Python 3.x is required.
- External Libraries: NONE!
  Standard Python built-ins (lists, loops) are used.
  No `pip install` commands are needed.

HOW TO RUN:
  Open terminal in this directory and execute:
      python hill_climbing_tsp.py

HOW TO ENTER INPUT:
  1. Enter the total number of cities (n).
  2. Enter the n x n cost adjacency matrix row-by-row (space-separated integers).
  
  Example Input (4 cities):
      Enter number of cities: 4
      Enter Cost Matrix:
      0 10 15 20
      10 0 35 25
      15 35 0 30
      20 25 30 0

ALGORITHM OVERVIEW (HILL CLIMBING):
  - Local search heuristic that iteratively moves towards better solutions.
  - Generates neighbors by swapping two city positions in the current tour.
  - Greedily selects the neighbor with the lowest total travel cost.
  - Terminates when no neighboring swap yields a lower cost (local minimum reached).
================================================================================
"""

# ==============================================================================
# SECTION 1: OBJECTIVE / COST EVALUATION FUNCTION
# ==============================================================================
def cost(path, graph):
    """
    Computes the total tour cost of visiting all cities and returning to the start.
    
    Parameters:
      path (list[int]): Order of city indices visited, e.g., [0, 2, 1, 3].
      graph (list[list[int]]): 2D cost matrix where graph[u][v] is travel cost between u and v.
      
    Returns:
      int: Sum of weights of edges along the cycle.
    """
    total = 0
    n = len(path)

    # Sum costs between consecutive cities: path[i] -> path[i+1]
    # (i + 1) % n ensures the final hop returns from path[n-1] back to path[0]
    for i in range(n):
        u = path[i]
        v = path[(i + 1) % n]
        total += graph[u][v]

    return total


# ==============================================================================
# SECTION 2: HILL CLIMBING SEARCH ALGORITHM
# ==============================================================================
def hill_climbing(graph):
    """
    Executes Steepest-Ascent (Greedy) Hill Climbing to find a minimum-cost tour.
    
    Parameters:
      graph (list[list[int]]): Adjacency matrix of edge costs between cities.
    """
    n = len(graph)
    # Start with an initial tour: visiting cities in default order [0, 1, 2, ..., n-1]
    path = list(range(n))

    iteration = 0
    while True:
        iteration += 1
        best = path[:]  # Holds the best candidate tour found in current neighborhood

        # Generate all 2-city swap neighbors (fixing city 0 as fixed start/base)
        for i in range(1, n):
            for j in range(i + 1, n):
                # Create a neighbor by swapping city at index i with city at index j
                new = path[:]
                new[i], new[j] = new[j], new[i]

                # Check if this neighbor gives a strictly lower tour cost
                if cost(new, graph) < cost(best, graph):
                    best = new

        # Termination condition: If no neighbor improves upon the current path,
        # we have reached a local minimum (peak in hill climbing terms).
        if best == path:
            break

        # Move to the better neighbor
        path = best

    # Construct complete closed loop by appending starting city to end
    complete_tour = path + [path[0]]
    min_cost = cost(path, graph)

    print("\n--- Hill Climbing Result ---")
    print("Best Path (Tour):", " -> ".join(map(str, complete_tour)))
    print("Minimum Cost:", min_cost)


# ==============================================================================
# SECTION 3: DRIVER CODE / USER INPUT
# ==============================================================================
if __name__ == "__main__":
    n = int(input("Enter number of cities: "))
    graph = []
    print(f"Enter Cost Matrix ({n} rows, {n} space-separated values per row):")
    for i in range(n):
        graph.append(list(map(int, input().split())))

    hill_climbing(graph)
