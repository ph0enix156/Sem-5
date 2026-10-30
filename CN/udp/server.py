"""
================================================================================
UDP UPPERCASE CONVERTER SERVER (SOCKET PROGRAMMING)
================================================================================

CONCEPT:
- UDP (User Datagram Protocol) is a connectionless, message-oriented transport
  layer protocol.
- Differences from TCP:
    * No connection setup: No 3-way handshake, no `listen()`, and no `accept()`.
    * Datagram based: Messages are sent in self-contained packets (datagrams).
    * Lightweight & Fast: Minimal protocol overhead (8-byte header vs 20-byte TCP).
    * Unreliable: Does not guarantee packet order, delivery, or flow control.
- UDP Server Workflow:
    1. Create a socket with type `socket.SOCK_DGRAM`.
    2. Bind to an IP address and Port so clients know where to send packets.
    3. Call `recvfrom(buffer_size)` which returns both data bytes AND sender address.
    4. Process data (convert string to uppercase).
    5. Call `sendto(response, client_addr)` to send reply datagram back directly.
    6. Close the socket.

PREREQUISITES:
- Python 3.x installed.
- No external libraries required (`socket` is built-in).

HOW TO RUN:
  1. Start UDP server:
       python server.py
  2. In another terminal, run:
       python client.py
================================================================================
"""

# ==============================================================================
# SECTION 1: IMPORT MODULE
# ==============================================================================
# Built-in socket library for low-level network communication.
import socket

# ==============================================================================
# SECTION 2: CREATE & CONFIGURE UDP SERVER SOCKET
# ==============================================================================
# AF_INET specifies IPv4 address family.
# SOCK_DGRAM specifies Datagram socket type (UDP protocol).
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to IP (127.0.0.1) and port (5000).
# In UDP, binding is required so incoming datagrams addressing port 5000 reach this socket.
server.bind(("127.0.0.1", 5000))

print("UDP Server is running and listening on 127.0.0.1:5000...")
print("Waiting for incoming UDP datagrams...")

# ==============================================================================
# SECTION 3: RECEIVE DATAGRAM FROM CLIENT
# ==============================================================================
# recvfrom(1024) waits for a single UDP datagram up to 1024 bytes.
# Unlike TCP's recv(), recvfrom() returns a tuple:
#   data: raw bytes of payload.
#   addr: tuple (client_ip, client_port) identifying sender so we can reply back.
data, addr = server.recvfrom(1024)

# Decode raw bytes into string using UTF-8
message = data.decode()
print(f"Received from client {addr}: '{message}'")

# ==============================================================================
# SECTION 4: PROCESS DATA (CONVERT TO UPPERCASE)
# ==============================================================================
# Convert the incoming message to uppercase letters.
result = message.upper()

# ==============================================================================
# SECTION 5: SEND REPLY DATAGRAM BACK TO CLIENT
# ==============================================================================
# sendto() takes two arguments:
#   1. Encoded byte stream payload.
#   2. Destination address tuple (client_ip, client_port) obtained earlier.
# Notice that no active connection exists; the packet is sent directly to 'addr'.
server.sendto(result.encode(), addr)
print(f"Sent uppercase reply '{result}' back to {addr}")

# ==============================================================================
# SECTION 6: CLOSE SOCKET
# ==============================================================================
# Release socket resource
server.close()
print("UDP server socket closed.")
