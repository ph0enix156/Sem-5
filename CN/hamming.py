
# Hamming Code (7,4) - Error Detection and Correction

data = input("Enter 4-bit data: ")

if len(data) != 4 or any(bit not in "01" for bit in data):
    print("Please enter exactly 4 binary bits.")
else:
    # Positions are numbered from 1 to 7
    h = [0] * 8

    # Place data bits
    h[3] = int(data[0])
    h[5] = int(data[1])
    h[6] = int(data[2])
    h[7] = int(data[3])

    # Calculate even parity bits
    h[1] = h[3] ^ h[5] ^ h[7]
    h[2] = h[3] ^ h[6] ^ h[7]
    h[4] = h[5] ^ h[6] ^ h[7]

    code = ''.join(str(h[i]) for i in range(1, 8))

    print("Transmitted code:", code)

    # Introduce an error
    error = int(input("Enter error position (1-7): "))

    if error < 1 or error > 7:
        print("Invalid error position.")
    else:
        h[error] ^= 1

        received = ''.join(str(h[i]) for i in range(1, 8))
        print("Received code:", received)

        # Calculate syndrome bits
        s1 = h[1] ^ h[3] ^ h[5] ^ h[7]
        s2 = h[2] ^ h[3] ^ h[6] ^ h[7]
        s4 = h[4] ^ h[5] ^ h[6] ^ h[7]

        error_position = s4 * 4 + s2 * 2 + s1

        print("Error position:", error_position)

        # Correct the error
        if error_position != 0:
            h[error_position] ^= 1

        corrected = ''.join(str(h[i]) for i in range(1, 8))

        print("Corrected code:", corrected)

        # Extract original data
        original = ''.join(str(h[i]) for i in [3, 5, 6, 7])
        print("Original data:", original)