visited = set()

def waterJugDFS(j1, j2, jug1, jug2, target):

    if (j1, j2) in visited:
        return False

    visited.add((j1, j2))

    print("(", j1, ",", j2, ")")

    if j1 == target:
        print("\nTarget Achieved!")
        return True

    states = [
        (jug1, j2),
        (j1, jug2),
        (0, j2),
        (j1, 0),
        (j1 - min(j1, jug2 - j2),
         j2 + min(j1, jug2 - j2)),
        (j1 + min(j2, jug1 - j1),
         j2 - min(j2, jug1 - j1))
    ]

    for state in states:
        if waterJugDFS(state[0], state[1], jug1, jug2, target):
            return True

    return False


jug1 = int(input("Enter capacity of Jug1: "))
jug2 = int(input("Enter capacity of Jug2: "))
target = int(input("Enter target amount for Jug1: "))

print("\nState Space Traversal:\n")

if not waterJugDFS(0, 0, jug1, jug2, target):
    print("\nNo Solution Exists.")