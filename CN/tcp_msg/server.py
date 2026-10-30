"""
================================================================================
TCP ONE-WAY MESSAGE SERVER (SOCKET PROGRAMMING)
================================================================================

CONCEPT:
- TCP (Transmission Control Protocol) provides reliable, ordered, and error-checked
  delivery of a stream of bytes.
- This program implements a fundamental TCP echo/listener server that:
    1. Binds to localhost (127.0.0.1) on port 5000.
    2. Listens passively for a client connection request.
    3. Accepts the connection when a client establishes the 3-way handshake.
    4. Receives a textual message sent by the client.
    5. Displays the received message along with the client's socket address.
    6. Closes the socket connection.

PREREQUISITES:
- Python 3.x installed.
- Standard library only (`socket` is built-in).

HOW TO RUN:
  1. Start server first:
       python server.py
  2. In a separate terminal, run:
       python client.py
================================================================================
"""

# ==============================================================================
# SECTION 1: IMPORT MODULE
# ==============================================================================
# socket module provides standard network communication interfaces.
import socket

# ==============================================================================
# SECTION 2: CREATE & CONFIGURE TCP SERVER SOCKET
# ==============================================================================
# AF_INET = Address Family for IPv4.
# SOCK_STREAM = Stream socket type indicating TCP protocol.
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the network interface IP (127.0.0.1 - Loopback) and port 5000.
# The server will only accept connections destined for this address & port.
server.bind(("127.0.0.1", 5000))

# Put the socket in listening mode.
# Backlog = 1: Allows up to 1 pending connection in the queue.
server.listen(1)
print("Server is listening on 127.0.0.1:5000...")
print("Waiting for an incoming connection...")

# ==============================================================================
# SECTION 3: ACCEPT INCOMING CLIENT CONNECTION
# ==============================================================================
# accept() blocks until an incoming TCP connection arrives.
# It returns:
#   conn: a new socket object specifically bound to this client conversation.
#   addr: a tuple (client_ip, client_ephemeral_port).
conn, addr = server.accept()
print(f"Connection accepted! Connected to client: {addr}")

# ==============================================================================
# SECTION 4: RECEIVE DATA
# ==============================================================================
# recv(1024) reads up to 1024 bytes from the TCP input buffer.
# decode() converts the raw bytes into a Python string using UTF-8 decoding.
message = conn.recv(1024).decode()
print("Message received from client:", message)

# ==============================================================================
# SECTION 5: CLOSE CONNECTION & TERMINATE
# ==============================================================================
# Close the dedicated connection socket to release port and connection state.
conn.close()

# Close the main listening server socket.
server.close()
print("Connection closed. Server finished.")
