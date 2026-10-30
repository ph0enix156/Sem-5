
import socket

# Create UDP socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Take input from user
message = input("Enter a lowercase string: ")

# Send message to server
client.sendto(message.encode(), ("127.0.0.1", 5000))

# Receive response from server
data, addr = client.recvfrom(1024)

print("Uppercase message from server:", data.decode())

# Close socket
client.close()
