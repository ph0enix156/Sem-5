
# Distance Vector Routing Algorithm

INF = float('inf')

# Input number of routers
n = int(input("Enter number of routers: "))

# Input cost matrix
print("Enter cost matrix (-1 for no direct connection):")

cost = []

for i in range(n):
    row = list(map(int, input().split()))

    for j in range(n):
        if row[j] == -1:
            row[j] = INF

    cost.append(row)

# Initialize distance and next-hop tables
dist = [row[:] for row in cost]

next_hop = []

for i in range(n):
    row = []
    for j in range(n):
        if i != j and cost[i][j] != INF:
            row.append(j)
        else:
            row.append(None)
    next_hop.append(row)

# Distance Vector algorithm
while True:
    old_dist = [row[:] for row in dist]
    updated = [row[:] for row in dist]
    changed = False

    for i in range(n):
        for j in range(n):
            for v in range(n):

                if i != v and cost[i][v] != INF:
                    new_cost = cost[i][v] + old_dist[v][j]

                    if new_cost < updated[i][j]:
                        updated[i][j] = new_cost
                        next_hop[i][j] = v
                        changed = True

    dist = updated

    if not changed:
        break

# Display final routing table
print("\nFinal Routing Tables:")

for i in range(n):
    print("\nRouter", chr(65 + i))
    print("Destination  Cost  Next Hop")

    for j in range(n):
        if dist[i][j] == INF:
            print(chr(65+j), "         INF   -")
        elif i == j:
            print(chr(65+j), "         0     -")
        else:
            print(chr(65+j), "        ", int(dist[i][j]),
                  "   ", chr(65 + next_hop[i][j]))

# Find shortest path
src = int(input("\nEnter source router (0=A, 1=B, 2=C): "))
dest = int(input("Enter destination router: "))

if dist[src][dest] == INF:
    print("No path exists")

else:
    path = [src]
    current = src

    while current != dest:
        current = next_hop[current][dest]
        path.append(current)

    print("Shortest Path:",
          " -> ".join(chr(65 + x) for x in path))

    print("Total Cost:", int(dist[src][dest]))