
import socket

# Create TCP socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client.connect(("127.0.0.1", 5000))

# Take input from user
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
operator = input("Enter operator (+, -, *, /): ")

# Send data to server
message = num1 + "," + num2 + "," + operator
client.send(message.encode())

# Receive result from server
result = client.recv(1024).decode()

print("Result from server:", result)

# Close connection
client.close()
