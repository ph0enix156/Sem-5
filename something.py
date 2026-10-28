
WaterJug Problem
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







Cannible And Missionary

visited = set()

TOTAL_M = 0
TOTAL_C = 0


def isValid(ml, cl, mr, cr):
    if ml < 0 or cl < 0 or mr < 0 or cr < 0:
        return False

    if ml > TOTAL_M or cl > TOTAL_C or mr > TOTAL_M or cr > TOTAL_C:
        return False

    if ml > 0 and cl > ml:
        return False

    if mr > 0 and cr > mr:
        return False

    return True


def missionaryCannibalDFS(ml, cl, boat):

    mr = TOTAL_M - ml
    cr = TOTAL_C - cl

    if (ml, cl, boat) in visited:
        return False

    visited.add((ml, cl, boat))

    side = "Left" if boat == 0 else "Right"
    print(f"Left({ml}M,{cl}C)  Right({mr}M,{cr}C)  Boat:{side}")

    if ml == 0 and cl == 0 and boat == 1:
        print("\nGoal Reached!")
        return True

    moves = [
        (1, 0),
        (2, 0),
        (0, 1),
        (0, 2),
        (1, 1)
    ]

    for m, c in moves:

        if boat == 0:
            newML = ml - m
            newCL = cl - c
            newBoat = 1
        else:
            newML = ml + m
            newCL = cl + c
            newBoat = 0

        newMR = TOTAL_M - newML
        newCR = TOTAL_C - newCL

        if isValid(newML, newCL, newMR, newCR):
            if missionaryCannibalDFS(newML, newCL, newBoat):
                return True

    return False


TOTAL_M = int(input("Enter number of Missionaries: "))
TOTAL_C = int(input("Enter number of Cannibals: "))

print("\nMissionaries and Cannibals Problem (DFS)\n")

if not missionaryCannibalDFS(TOTAL_M, TOTAL_C, 0):
    print("\nNo Solution Exists.")





TOWER OF HANOI

def towerOfHanoi(n, source, auxiliary, destination):

    if n == 1:
        print(f"Move Disk 1 from {source} to {destination}")
        return

    towerOfHanoi(n - 1, source, destination, auxiliary)

    print(f"Move Disk {n} from {source} to {destination}")

    towerOfHanoi(n - 1, auxiliary, source, destination)


n = int(input("Enter the number of disks: "))

print("\nSteps to solve Tower of Hanoi:\n")

towerOfHanoi(n, 'A', 'B', 'C')