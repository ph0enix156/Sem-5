"""
================================================================================
TCP CALCULATOR SERVER (SOCKET PROGRAMMING)
================================================================================

CONCEPT:
- TCP (Transmission Control Protocol) is a connection-oriented, reliable transport
  layer protocol that guarantees ordered and error-checked delivery of a stream
  of octets (bytes) between applications.
- Connection-Oriented: A 3-way handshake (SYN -> SYN-ACK -> ACK) is performed
  before data can be transferred.
- Client-Server Architecture:
    1. Server creates a socket, binds it to an IP address and Port, and listens.
    2. Server blocks on `accept()` waiting for incoming client connections.
    3. When client connects, a new dedicated connection socket `conn` is returned.
    4. Client sends mathematical operands and an operator (comma-separated string).
    5. Server parses data, performs arithmetic calculation, and returns the result.
    6. Both connection and server sockets are closed gracefully.

PREREQUISITES:
- Python 3.x installed.
- No external libraries required (uses Python's built-in `socket` module).

HOW TO RUN:
  1. First start the server:
       python server.py
  2. Then, in a separate terminal window, run client:
       python client.py
================================================================================
"""

# ==============================================================================
# SECTION 1: IMPORT MODULE
# ==============================================================================
# The 'socket' module provides access to the standard BSD socket interface.
import socket

# ==============================================================================
# SECTION 2: CREATE & CONFIGURE TCP SERVER SOCKET
# ==============================================================================
# socket.AF_INET specifies IPv4 addressing scheme.
# socket.SOCK_STREAM specifies TCP (reliable byte stream protocol).
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Associate the socket with local loopback IP (127.0.0.1) and port number 5000.
# Port 5000 is an unreserved port chosen for custom application communication.
server.bind(("127.0.0.1", 5000))

# Put the server socket into passive listening mode.
# The backlog argument '1' specifies the maximum number of unaccepted connections
# allowed in the system's listen queue before refusing new attempts.
server.listen(1)
print("Server is waiting for connection on 127.0.0.1:5000...")

# ==============================================================================
# SECTION 3: ACCEPT CLIENT CONNECTION
# ==============================================================================
# accept() is a blocking call: it pauses execution until a client connects.
# It returns a tuple:
#   conn: a NEW socket object usable to send and receive data on the established connection.
#   addr: the client's address (IP, ephemeral_port).
conn, addr = server.accept()
print("Connected to client at:", addr)

# ==============================================================================
# SECTION 4: RECEIVE & PARSE CLIENT REQUEST
# ==============================================================================
# recv(1024) reads up to 1024 bytes from the TCP socket buffer.
# decode() converts the received raw bytes back into a Python string (UTF-8).
data = conn.recv(1024).decode()
print("Received raw data from client:", data)

# Split comma-separated string "num1,num2,operator" into distinct components.
num1, num2, operator = data.split(",")

# Convert string inputs into floating-point numbers for calculation.
num1 = float(num1)
num2 = float(num2)

# ==============================================================================
# SECTION 5: ARITHMETIC COMPUTATION
# ==============================================================================
# Perform the requested operation based on operator symbol.
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    # Guard against division by zero runtime error
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Cannot divide by zero"
else:
    result = "Invalid operator"

print("Calculated Result:", result)

# ==============================================================================
# SECTION 6: SEND RESPONSE & CLEANUP
# ==============================================================================
# Convert result to string and encode() it into raw bytes before sending over TCP.
conn.send(str(result).encode())

# Close the dedicated client connection socket.
conn.close()

# Close the listening server socket to release port 5000.
server.close()
print("Connection closed. Server terminated.")
