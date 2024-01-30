import socket
import os

# Define server address and port
SERVER_ADDRESS = "localhost"  # Replace with server IP address
SERVER_PORT = 8000

# Open the file to send
filename = "large_file.mp4"
file_size = os.path.getsize(filename)

# Create a TCP socket
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
clientsocket.connect(('localhost', 8000))

# Send file data in chunks
with open(filename, "rb") as f:
    while True:
        data = f.read(1024)
        if not data:
            break
        clientsocket.sendall(data)

# Close the connection
clientsocket.close()

print(f"Sent file: {filename} ({file_size} bytes) to server at {SERVER_ADDRESS}:{SERVER_PORT}")
