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