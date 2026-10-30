"""
================================================================================
UDP UPPERCASE CONVERTER CLIENT (SOCKET PROGRAMMING)
================================================================================

CONCEPT:
- In UDP, a client does not perform a connection handshake (`connect()` is optional).
- UDP Client Workflow:
    1. Create a socket with type `socket.SOCK_DGRAM`.
    2. Prompt user for string input.
    3. Use `sendto(data, (server_ip, server_port))` to dispatch the packet.
       The OS automatically assigns an ephemeral client port.
    4. Call `recvfrom(buffer_size)` to listen for the server's response datagram.
    5. Display the received response and close socket.

PREREQUISITES:
- Python 3.x installed.
- Standard library only (`socket` is built-in).

HOW TO RUN:
  1. Start server.py first in one terminal.
  2. Run client in another terminal:
       python client.py
================================================================================
"""

# ==============================================================================
# SECTION 1: IMPORT MODULE
# ==============================================================================
import socket

# ==============================================================================
# SECTION 2: CREATE UDP CLIENT SOCKET
# ==============================================================================
# AF_INET = IPv4 addressing.
# SOCK_DGRAM = Connectionless UDP datagram socket.
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# ==============================================================================
# SECTION 3: USER INPUT & DISPATCH DATAGRAM
# ==============================================================================
# Prompt user for string text to send to server for uppercase conversion.
message = input("Enter a lowercase string: ")

# sendto() transmits data without establishing a persistent session.
# Parameters:
#   1. message.encode(): byte representation of the text.
#   2. ("127.0.0.1", 5000): destination address tuple (target_ip, target_port).
client.sendto(message.encode(), ("127.0.0.1", 5000))
print("Datagram sent to server at 127.0.0.1:5000...")

# ==============================================================================
# SECTION 4: RECEIVE RESPONSE FROM SERVER
# ==============================================================================
# recvfrom(1024) waits for a reply datagram of up to 1024 bytes.
# Returns (payload_bytes, sender_address_tuple).
data, addr = client.recvfrom(1024)

# Decode received byte stream to string
print("Uppercase message from server:", data.decode())

# ==============================================================================
# SECTION 5: CLOSE SOCKET
# ==============================================================================
# Release socket resource
client.close()
