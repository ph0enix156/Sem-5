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