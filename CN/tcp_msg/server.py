
import socket

# Create TCP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind server to IP and port
server.bind(("127.0.0.1", 5000))

# Listen for client connections
server.listen(1)
print("Server is waiting for a connection...")

# Accept client connection
conn, addr = server.accept()
print("Connected to:", addr)

# Receive message from client
message = conn.recv(1024).decode()
print("Message from client:", message)

# Close connection
conn.close()
server.close()
