
import math

# Input
prefix = int(input("Enter original prefix (e.g. 24): "))
subnets = int(input("Enter required number of subnets: "))

# Calculate borrowed bits
borrowed_bits = math.ceil(math.log2(subnets))

# Calculate new prefix
new_prefix = prefix + borrowed_bits

if prefix < 0 or prefix > 30 or subnets < 1 or new_prefix > 30:
    print("Invalid network prefix or subnet requirement.")

else:
    # Calculate host bits
    host_bits = 32 - new_prefix

    # Calculate usable hosts
    usable_hosts = (2 ** host_bits) - 2

    # Calculate subnet mask
    mask_bits = "1" * new_prefix + "0" * host_bits

    octets = [
        int(mask_bits[i:i+8], 2)
        for i in range(0, 32, 8)
    ]

    subnet_mask = ".".join(map(str, octets))

    # Display results
    print("\n--- Subnetting Results ---")
    print("Original Prefix: /", prefix)
    print("Required Subnets:", subnets)
    print("Borrowed Bits:", borrowed_bits)
    print("New Prefix: /", new_prefix)
    print("Subnet Mask:", subnet_mask)
    print("Usable Hosts per Subnet:", usable_hosts)
