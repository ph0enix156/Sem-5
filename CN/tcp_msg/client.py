"""
================================================================================
TCP ONE-WAY MESSAGE CLIENT (SOCKET PROGRAMMING)
================================================================================

CONCEPT:
- The TCP client connects directly to a server socket listening on an IP:Port.
- When `connect()` is executed, TCP initiates a 3-way handshake:
    1. SYN (Client -> Server)
    2. SYN-ACK (Server -> Client)
    3. ACK (Client -> Server)
- Once connected, strings must be serialized to bytes via `encode()` before
  being pushed onto the socket stream.
- When communication is complete, `close()` sends a FIN packet to terminate
  the connection reliably.

PREREQUISITES:
- Python 3.x installed.
- No external libraries required (`socket` is built-in).

HOW TO RUN:
  1. Start server.py first.
  2. In another terminal, run:
       python client.py
================================================================================
"""

# ==============================================================================
# SECTION 1: IMPORT MODULE
# ==============================================================================
import socket

# ==============================================================================
# SECTION 2: CREATE TCP SOCKET
# ==============================================================================
# AF_INET = IPv4 protocol family.
# SOCK_STREAM = Connection-oriented TCP socket.
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# ==============================================================================
# SECTION 3: CONNECT TO THE SERVER
# ==============================================================================
# Initiate 3-way handshake with server listening on loopback (127.0.0.1) at port 5000.
client.connect(("127.0.0.1", 5000))
print("Connected to server at 127.0.0.1:5000")

# ==============================================================================
# SECTION 4: GET INPUT & TRANSMIT MESSAGE
# ==============================================================================
# Prompt user for a text message to send.
message = input("Enter a message to send to server: ")

# encode() converts the string into a sequence of UTF-8 bytes.
# client.send() pushes those bytes into the socket's transmit buffer.
client.send(message.encode())
print("Message sent successfully!")

# ==============================================================================
# SECTION 5: CLOSE SOCKET
# ==============================================================================
# Close the client socket and initiate connection teardown (TCP FIN).
client.close()
print("Client connection closed.")
