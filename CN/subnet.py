"""
================================================================================
IP SUBNETTING CALCULATOR (FLSM - FIXED LENGTH SUBNET MASKING)
================================================================================

CONCEPT:
- Subnetting is the practice of dividing a single large physical IP network
  into multiple smaller, logical sub-networks (subnets).
- Key Terminology & Math:
    1. IPv4 Address Length: Fixed at 32 bits divided into 4 octets (8 bits each).
    2. CIDR Prefix (/N): The number of consecutive leading 1s representing
       the network identifier portion.
    3. Borrowed Bits (s): To create 'k' subnets, we must borrow 's' bits from
       the host portion such that:
           2^s >= k  ==>  s = ceil(log2(k))
    4. New Subnet Prefix:
           New Prefix = Original Prefix + Borrowed Bits
    5. Host Bits (h):
           Host Bits = 32 - New Prefix
    6. Usable Hosts per Subnet:
           Total IPs = 2^h
           Usable Hosts = 2^h - 2
           (We subtract 2 because the 1st address is reserved as the Network ID,
            and the last address is reserved as the Directed Broadcast Address).
    7. Subnet Mask (Dotted-Decimal):
           Convert the 32-bit binary string (New_Prefix 1s followed by Host_Bits 0s)
           into four 8-bit integers (e.g., 255.255.255.192).

PREREQUISITES:
- Python 3.x installed.
- Uses built-in `math` module (no third-party packages needed).

HOW TO RUN:
  Open terminal in this directory and execute:
      python subnet.py
================================================================================
"""

# ==============================================================================
# SECTION 1: IMPORT REQUIRED MODULES
# ==============================================================================
# 'math' is needed for ceil() and log2() calculations.
import math

# ==============================================================================
# SECTION 2: USER INPUTS
# ==============================================================================
# Prompt for current CIDR prefix length (e.g., 24 for a Class C network like 192.168.1.0/24)
prefix = int(input("Enter original prefix length (e.g., 24 for /24): "))

# Prompt for the number of smaller subnets needed
subnets = int(input("Enter required number of subnets: "))

# ==============================================================================
# SECTION 3: BORROWED BITS & NEW PREFIX CALCULATION
# ==============================================================================
# To create 'subnets' number of subnets, we need: 2^s >= subnets
# Using logarithms: s = ceil(log2(subnets))
borrowed_bits = math.ceil(math.log2(subnets))

# The new network mask length after borrowing host bits
new_prefix = prefix + borrowed_bits

# ==============================================================================
# SECTION 4: INPUT VALIDATION & CONSTRAINTS CHECK
# ==============================================================================
# Valid prefix range is 0 to 30.
# A prefix > 30 leaves <= 1 host bit (2^1 - 2 = 0 usable hosts).
if prefix < 0 or prefix > 30 or subnets < 1 or new_prefix > 30:
    print("\nError: Invalid network prefix or subnet requirement.")
    print("Ensure 0 <= prefix <= 30 and (prefix + borrowed_bits) <= 30.")

else:
    # ==========================================================================
    # SECTION 5: HOST CAPACITY & SUBNET MASK CALCULATION
    # ==========================================================================
    # Remaining bits available for addressing host devices in each subnet
    host_bits = 32 - new_prefix

    # Calculate usable host IP addresses (excluding Network ID and Broadcast ID)
    usable_hosts = (2 ** host_bits) - 2

    # Construct the 32-bit binary representation of the subnet mask:
    # 'new_prefix' ones followed by 'host_bits' zeros.
    mask_bits = "1" * new_prefix + "0" * host_bits

    # Split the 32-bit string into four 8-bit slices (octets) and parse as base-2 integers
    octets = [
        int(mask_bits[i:i + 8], 2)
        for i in range(0, 32, 8)
    ]

    # Join the 4 octet integers with dots to produce standard dotted-decimal notation
    subnet_mask = ".".join(map(str, octets))

    # ==========================================================================
    # SECTION 6: DISPLAY DETAILED RESULTS
    # ==========================================================================
    print("\n==========================================")
    print("           SUBNETTING RESULTS             ")
    print("==========================================")
    print(f"Original Network Prefix : /{prefix}")
    print(f"Required Subnets        : {subnets}")
    print(f"Bits Borrowed from Host : {borrowed_bits} bits")
    print(f"New Subnet Prefix (CIDR): /{new_prefix}")
    print(f"Subnet Mask (Decimal)   : {subnet_mask}")
    print(f"Binary Mask             : {' '.join(mask_bits[i:i+8] for i in range(0, 32, 8))}")
    print(f"Host Bits per Subnet    : {host_bits} bits")
    print(f"Total IPs per Subnet    : {2 ** host_bits}")
    print(f"Usable Hosts per Subnet : {usable_hosts}")
    print("==========================================")
