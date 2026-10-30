
import socket

# Create UDP socket
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind server to IP and port
server.bind(("127.0.0.1", 5000))

print("UDP Server is waiting for messages...")

# Receive message from client
data, addr = server.recvfrom(1024)

message = data.decode()
print("Message from client:", message)

# Convert to uppercase
result = message.upper()

# Send result back to client
server.sendto(result.encode(), addr)

print("Uppercase message sent:", result)

# Close socket
server.close()
