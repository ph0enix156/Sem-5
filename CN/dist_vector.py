"""
================================================================================
DISTANCE VECTOR ROUTING ALGORITHM (BELLMAN-FORD EQUATION)
================================================================================

CONCEPT:
- Distance Vector Routing is a dynamic, decentralized routing algorithm used in
  network protocols like RIP (Routing Information Protocol).
- Each router maintains a routing table containing:
    1. Destination: The target network / router.
    2. Cost (Metric): The current shortest distance to the destination.
    3. Next Hop: The adjacent neighbor to forward packets to.
- Bellman-Ford Equation:
    D_x(y) = min_v { c(x, v) + D_v(y) }
    Where:
      * D_x(y) = Shortest estimated cost from router x to destination y
      * c(x, v) = Direct link cost from router x to neighbor v
      * D_v(y) = Neighbor v's distance vector estimate to reach y
- Iterative Convergence:
    Routers exchange distance vectors with immediate neighbors.
    Updates continue in rounds until no router finds a shorter path (stable state).

PREREQUISITES:
- Python 3.x installed.
- No third-party packages required (pure Python standard library).

HOW TO RUN:
  Open terminal in this directory and execute:
      python dist_vector.py

SAMPLE INPUT (3 Routers):
  Enter number of routers: 3
  Enter cost matrix (-1 for no direct connection):
  0 2 7
  2 0 1
  7 1 0
================================================================================
"""

# ==============================================================================
# SECTION 1: GLOBAL CONSTANTS & MATRIX INPUT
# ==============================================================================
# Infinity representation for pairs of routers that do not have a direct link.
INF = float('inf')

# Number of routers in the autonomous network topology
n = int(input("Enter number of routers: "))

print("Enter cost matrix (-1 for no direct connection):")
cost = []

# Read direct link cost matrix row-by-row
for i in range(n):
    # Read space-separated integer costs for router i to all routers j
    row = list(map(int, input().split()))

    # Replace -1 with infinity (INF) to represent no direct edge/link
    for j in range(n):
        if row[j] == -1:
            row[j] = INF

    cost.append(row)


# ==============================================================================
# SECTION 2: INITIALIZE DISTANCE VECTOR & NEXT-HOP TABLES
# ==============================================================================
# Deep-copy direct link costs into the working distance vector table 'dist'
dist = [row[:] for row in cost]

# Initialize next_hop matrix:
# next_hop[i][j] stores the immediate neighbor router to forward packets from i to reach j
next_hop = []

for i in range(n):
    row = []
    for j in range(n):
        # If router i directly connects to router j (and i != j), initial next-hop is j itself
        if i != j and cost[i][j] != INF:
            row.append(j)
        else:
            row.append(None)  # None if same node or no direct route initially
    next_hop.append(row)


# ==============================================================================
# SECTION 3: DISTANCE VECTOR ITERATIVE RELAXATION (BELLMAN-FORD)
# ==============================================================================
# Repeat rounds of distance vector updates until convergence (no values change)
while True:
    # Snapshot distance table before this iteration round
    old_dist = [row[:] for row in dist]
    updated = [row[:] for row in dist]
    changed = False  # Flag to track if any route was relaxed/improved

    # Triply-nested relaxation loop:
    # i = source router
    # j = destination router
    # v = intermediate neighbor of i
    for i in range(n):
        for j in range(n):
            for v in range(n):
                # Ensure router v is a valid, reachable direct neighbor of router i
                if i != v and cost[i][v] != INF:
                    # Bellman-Ford: Cost from i to v + Neighbor v's distance to j
                    new_cost = cost[i][v] + old_dist[v][j]

                    # If routing via neighbor v yields a strictly shorter total distance
                    if new_cost < updated[i][j]:
                        updated[i][j] = new_cost  # Update minimum distance
                        next_hop[i][j] = v         # Set neighbor v as next-hop
                        changed = True            # Mark that routing table changed

    dist = updated

    # If an entire round completes without any route changes, convergence is reached
    if not changed:
        break


# ==============================================================================
# SECTION 4: DISPLAY FINAL ROUTING TABLES
# ==============================================================================
print("\n========================================")
print("          FINAL ROUTING TABLES          ")
print("========================================")

# Routers are named alphabetically: 0 -> 'A', 1 -> 'B', 2 -> 'C', etc. (chr(65 + i))
for i in range(n):
    print(f"\nRouter {chr(65 + i)}:")
    print("Destination  Cost  Next Hop")
    print("----------------------------")

    for j in range(n):
        if dist[i][j] == INF:
            print(f"{chr(65 + j):<11}  INF   -")
        elif i == j:
            print(f"{chr(65 + j):<11}  0     -")
        else:
            print(f"{chr(65 + j):<11}  {int(dist[i][j]):<4}  {chr(65 + next_hop[i][j])}")


# ==============================================================================
# SECTION 5: SHORTEST PATH TRACING & QUERY
# ==============================================================================
print("\n========================================")
print("         SHORTEST PATH QUERY            ")
print("========================================")

src = int(input(f"Enter source router index (0 to {n - 1}): "))
dest = int(input(f"Enter destination router index (0 to {n - 1}): "))

# Check if destination is unreachable
if dist[src][dest] == INF:
    print(f"\nNo route exists between Router {chr(65 + src)} and Router {chr(65 + dest)}.")
else:
    # Reconstruct the hop-by-hop forwarding path using next_hop table
    path = [src]
    current = src

    while current != dest:
        current = next_hop[current][dest]
        path.append(current)

    # Format path nicely with arrows: e.g., "A -> B -> C"
    path_str = " -> ".join(chr(65 + x) for x in path)
    print("\nShortest Path:", path_str)
    print("Total Cost   :", int(dist[src][dest]))
