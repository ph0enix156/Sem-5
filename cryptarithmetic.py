
w1 = input("First word: ").upper()
w2 = input("Second word: ").upper()
w3 = input("Result word: ").upper()

letters = list(set(w1 + w2 + w3))
d = {}

def num(w):
    return int("".join(str(d[c]) for c in w))

def solve(i):
    if i == len(letters):
        return num(w1) + num(w2) == num(w3)
    for digit in range(10):
        if digit in d.values():
            continue
        if digit == 0 and letters[i] in (w1[0], w2[0], w3[0]):
            continue
        d[letters[i]] = digit
        if solve(i + 1):
            return True
        del d[letters[i]]
    return False

if len(letters) <= 10 and solve(0):
    print(num(w1), "+", num(w2), "=", num(w3))
else:
    print("No solution")
