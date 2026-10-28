
from queue import PriorityQueue

def read():
    return [list(map(int, input().split())) for i in range(3)]


def h(s, goal):
    count = 0
    for i in range(3):
        for j in range(3):
            if s[i][j] != 0 and s[i][j] != goal[i][j]:
                count += 1
    return count


def astar(start, goal):
    pq = PriorityQueue()
    pq.put((h(start, goal), 0, start))
    visited = []

    while not pq.empty():
        f, g, s = pq.get()

        if s in visited:
            continue
        visited.append(s)

        print("Visited State:")
        for row in s:
            print(row)
        print("f =", f, "g =", g, "h =", h(s, goal))
        print()

        if s == goal:
            print("Goal Reached!")
            return

        x, y = 0, 0
        for i in range(3):
            for j in range(3):
                if s[i][j] == 0:
                    x, y = i, j

        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dx, dy in moves:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < 3 and 0 <= ny < 3:
                new = [row[:] for row in s]

                new[x][y], new[nx][ny] = new[nx][ny], new[x][y]

                if new not in visited:
                    ng = g + 1
                    nh = h(new, goal)
                    pq.put((ng + nh, ng, new))

    print("No Solution Found")


print("Enter Initial State (0 = Blank):")
start = read()

print("Enter Goal State:")
goal = read()

astar(start, goal)