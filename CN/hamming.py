"""
================================================================================
HAMMING (7, 4) ERROR DETECTION AND CORRECTION CODE
================================================================================

CONCEPT:
- Hamming (7,4) is a linear error-correcting code that encodes 4 bits of data
  into 7 bits by adding 3 parity (redundant) check bits.
- It can detect and correct any single-bit error (Single Error Correction - SEC).
- Bit Position Assignment:
    * Parity bits occupy powers of 2 positions:
        Position 1 (2^0) -> Parity P1
        Position 2 (2^1) -> Parity P2
        Position 4 (2^2) -> Parity P4
    * Data bits occupy the remaining positions:
        Position 3 -> Data D1 (data[0])
        Position 5 -> Data D2 (data[1])
        Position 6 -> Data D3 (data[2])
        Position 7 -> Data D4 (data[3])
- Even Parity Coverage (Bit Index in Binary):
    * P1 covers bits whose position binary has 1 in 1st bit (LSB): {1, 3, 5, 7}
        P1 = D1 ^ D2 ^ D4  (i.e., h[3] ^ h[5] ^ h[7])
    * P2 covers bits whose position binary has 1 in 2nd bit: {2, 3, 6, 7}
        P2 = D1 ^ D3 ^ D4  (i.e., h[3] ^ h[6] ^ h[7])
    * P4 covers bits whose position binary has 1 in 3rd bit: {4, 5, 6, 7}
        P4 = D2 ^ D3 ^ D4  (i.e., h[5] ^ h[6] ^ h[7])
- Syndrome Calculation (Receiver Side):
    * S1 = h[1] ^ h[3] ^ h[5] ^ h[7]
    * S2 = h[2] ^ h[3] ^ h[6] ^ h[7]
    * S4 = h[4] ^ h[5] ^ h[6] ^ h[7]
    * Error Position = S4*4 + S2*2 + S1*1 (Syndrome decimal value).
    * If syndrome == 0 -> No error.
    * If syndrome != 0 -> Syndrome directly gives 1-based index of corrupted bit!

PREREQUISITES:
- Python 3.x installed.
- No external libraries required.

HOW TO RUN:
  Open terminal in this directory and execute:
      python hamming.py
================================================================================
"""

# ==============================================================================
# SECTION 1: INPUT DATA VALIDATION
# ==============================================================================
# Prompt user for 4-bit data word (e.g., 1011)
data = input("Enter 4-bit data (e.g., 1011): ").strip()

# Validate that input is exactly 4 characters and only contains '0' and '1'
if len(data) != 4 or any(bit not in "01" for bit in data):
    print("Error: Please enter exactly 4 binary bits (e.g., 1011).")
else:
    # ==========================================================================
    # SECTION 2: CONSTRUCT 7-BIT CODEWORD (1-BASED INDEXING)
    # ==========================================================================
    # We use an 8-element list so indices 1..7 map directly to bit positions.
    # Index 0 is unused dummy padding.
    h = [0] * 8

    # Place user's 4 data bits into positions 3, 5, 6, 7
    h[3] = int(data[0])  # Data bit 1 (D1)
    h[5] = int(data[1])  # Data bit 2 (D2)
    h[6] = int(data[2])  # Data bit 3 (D3)
    h[7] = int(data[3])  # Data bit 4 (D4)

    # Compute Even Parity Bits using bitwise XOR (^)
    # An even number of 1s yields 0; an odd number of 1s yields 1.
    h[1] = h[3] ^ h[5] ^ h[7]  # P1 covers positions 1, 3, 5, 7
    h[2] = h[3] ^ h[6] ^ h[7]  # P2 covers positions 2, 3, 6, 7
    h[4] = h[5] ^ h[6] ^ h[7]  # P4 covers positions 4, 5, 6, 7

    # Assemble the final 7-bit transmitted codeword string
    code = ''.join(str(h[i]) for i in range(1, 8))
    print("\n----------------------------------------")
    print("Transmitted 7-bit Codeword:", code)
    print("----------------------------------------")

    # ==========================================================================
    # SECTION 3: SIMULATE CHANNEL ERROR (BIT FLIP)
    # ==========================================================================
    # Ask user to pick a bit position (1 to 7) to inject an error
    error = int(input("Enter error bit position to corrupt (1-7): "))

    if error < 1 or error > 7:
        print("Invalid error position! Must be between 1 and 7.")
    else:
        # Flip the selected bit using XOR with 1: (0 ^ 1 = 1, 1 ^ 1 = 0)
        h[error] ^= 1

        # Form received corrupt codeword
        received = ''.join(str(h[i]) for i in range(1, 8))
        print("Received (corrupted) Codeword:", received)

        # ======================================================================
        # SECTION 4: SYNDROME CALCULATION (ERROR DETECTION)
        # ======================================================================
        # Recompute parity checks across received bits
        s1 = h[1] ^ h[3] ^ h[5] ^ h[7]  # Parity check 1
        s2 = h[2] ^ h[3] ^ h[6] ^ h[7]  # Parity check 2
        s4 = h[4] ^ h[5] ^ h[6] ^ h[7]  # Parity check 4

        # Convert binary syndrome (S4 S2 S1) into decimal integer
        # This decimal value points exactly to the corrupted bit index!
        error_position = s4 * 4 + s2 * 2 + s1 * 1

        print("\n----------------------------------------")
        print(f"Calculated Syndrome: S4={s4}, S2={s2}, S1={s1}")
        print("Detected Error Position:", error_position)

        # ======================================================================
        # SECTION 5: ERROR CORRECTION & DATA RECOVERY
        # ======================================================================
        # If error_position > 0, flip that bit back to its original value
        if error_position != 0:
            h[error_position] ^= 1
            print(f"Corrected bit at position {error_position} via bit-flip.")
        else:
            print("No transmission error detected.")

        # Reconstructed 7-bit codeword
        corrected = ''.join(str(h[i]) for i in range(1, 8))
        print("Corrected Codeword:", corrected)

        # Extract the original 4 data bits from positions [3, 5, 6, 7]
        original = ''.join(str(h[i]) for i in [3, 5, 6, 7])
        print("Original Recovered 4-bit Data:", original)
        print("----------------------------------------")
