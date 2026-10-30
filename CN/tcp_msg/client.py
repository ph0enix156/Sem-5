
import socket

# Create TCP socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client.connect(("127.0.0.1", 5000))

# Send message
message = input("Enter a message: ")
client.send(message.encode())

print("Message sent successfully!")

# Close connection
client.close()
