
b = [" "] * 9

def display():
    for i in range(0, 9, 3):
        print(b[i], "|", b[i+1], "|", b[i+2])
        if i < 6:
            print("---------")


def win(p):
    lines = [(0,1,2), (3,4,5), (6,7,8),
             (0,3,6), (1,4,7), (2,5,8),
             (0,4,8), (2,4,6)]

    for a, c, d in lines:
        if b[a] == b[c] == b[d] == p:
            return True
    return False


def minimax(p):
    if win("O"): return 1
    if win("X"): return -1
    if " " not in b: return 0

    best = -2 if p == "O" else 2

    for i in range(9):
        if b[i] == " ":
            b[i] = p

            next_p = "X" if p == "O" else "O"
            score = minimax(next_p)

            b[i] = " "

            if p == "O":
                best = max(best, score)
            else:
                best = min(best, score)

    return best


while True:
    display()
    m = int(input("Your move (1-9): ")) - 1
    b[m] = "X"

    if win("X"):
        display()
        print("You win!")
        break

    if " " not in b:
        display()
        print("Draw!")
        break

    best, move = -2, -1

    for i in range(9):
        if b[i] == " ":
            b[i] = "O"
            score = minimax("X")
            b[i] = " "

            if score > best:
                best, move = score, i

    b[move] = "O"

    if win("O"):
        display()
        print("Computer wins!")
        break

    if " " not in b:
        display()
        print("Draw!")
        break
