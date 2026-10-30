"""
================================================================================
TCP CALCULATOR CLIENT (SOCKET PROGRAMMING)
================================================================================

CONCEPT:
- The TCP Client establishes an active connection to a known server IP and port.
- Client Lifecycle:
    1. Create an endpoint socket (`AF_INET`, `SOCK_STREAM`).
    2. Initiate a 3-way handshake to the server via `connect((ip, port))`.
    3. Gather user input (two numbers and one arithmetic operator).
    4. Format and encode the message into bytes (`message.encode()`).
    5. Transmit the payload to the server with `client.send()`.
    6. Wait and read the server's reply using `client.recv()`.
    7. Close the socket to tear down the TCP connection.

PREREQUISITES:
- Python 3.x installed.
- No external libraries required (`socket` is built-in).

HOW TO RUN:
  1. Make sure server.py is already running.
  2. Run client in another terminal:
       python client.py
================================================================================
"""

# ==============================================================================
# SECTION 1: IMPORT MODULE
# ==============================================================================
import socket

# ==============================================================================
# SECTION 2: CREATE TCP CLIENT SOCKET
# ==============================================================================
# socket.AF_INET specifies IPv4 addressing.
# socket.SOCK_STREAM specifies TCP stream protocol.
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# ==============================================================================
# SECTION 3: CONNECT TO THE SERVER
# ==============================================================================
# connect() initiates the TCP 3-way handshake with the server at 127.0.0.1:5000.
# If the server is not running or listening, this raises ConnectionRefusedError.
client.connect(("127.0.0.1", 5000))
print("Successfully connected to TCP Calculator Server on 127.0.0.1:5000")

# ==============================================================================
# SECTION 4: USER INPUT COLLECTION
# ==============================================================================
# Prompt user for operand 1, operand 2, and the math operation symbol.
num1 = input("Enter first number: ").strip()
num2 = input("Enter second number: ").strip()
operator = input("Enter operator (+, -, *, /): ").strip()

# ==============================================================================
# SECTION 5: PAYLOAD FORMATTING & TRANSMISSION
# ==============================================================================
# Package parameters into a CSV format string: "num1,num2,operator"
message = num1 + "," + num2 + "," + operator

# encode() serializes string into raw bytes (default UTF-8) before network transmission.
client.send(message.encode())
print("Sent request to server:", message)

# ==============================================================================
# SECTION 6: RECEIVE RESULT & CLEANUP
# ==============================================================================
# recv(1024) blocks until server sends back the calculated answer.
# decode() turns received byte stream back into a readable string.
result = client.recv(1024).decode()

print("----------------------------------------")
print("Result from server:", result)
print("----------------------------------------")

# Close client socket to release OS resources and terminate TCP connection (FIN handshake).
client.close()
