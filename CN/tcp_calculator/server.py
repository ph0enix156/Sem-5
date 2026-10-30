
import socket

# Create TCP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind IP address and port
server.bind(("127.0.0.1", 5000))

# Listen for client
server.listen(1)
print("Server is waiting for connection...")

# Accept client connection
conn, addr = server.accept()
print("Connected to:", addr)

# Receive data from client
data = conn.recv(1024).decode()

# Split received data
num1, num2, operator = data.split(",")

num1 = float(num1)
num2 = float(num2)

# Perform calculation
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Cannot divide by zero"
else:
    result = "Invalid operator"

print("Result:", result)

# Send result back to client
conn.send(str(result).encode())

# Close connection
conn.close()
server.close()
