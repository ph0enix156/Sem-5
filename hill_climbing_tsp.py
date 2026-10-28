
def cost(path, graph):
    total = 0
    n = len(path)

    for i in range(n):
        total += graph[path[i]][path[(i + 1) % n]]

    return total


def hill_climbing(graph):
    n = len(graph)
    path = list(range(n))

    while True:
        best = path[:]

        for i in range(1, n):
            for j in range(i + 1, n):
                new = path[:]
                new[i], new[j] = new[j], new[i]

                if cost(new, graph) < cost(best, graph):
                    best = new

        if best == path:
            break

        path = best

    print("Best Path:", path + [path[0]])
    print("Minimum Cost:", cost(path, graph))


n = int(input("Enter number of cities: "))
graph = []
print("Enter Cost Matrix:")
for i in range(n):
    graph.append(list(map(int, input().split())))

hill_climbing(graph)