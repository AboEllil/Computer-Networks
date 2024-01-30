import socket
import os

# Define server address and port
SERVER_ADDRESS = "localhost"  # Bind to all interfaces
SERVER_PORT = 8000

# Create a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind socket to address and port
sock.bind(('localhost', 8000))

# Listen for incoming connections
sock.listen(1)

print(f"Server listening on {SERVER_ADDRESS}:{SERVER_PORT}")

# Accept connections and receive data
while True:
    # Wait for a connection
    conn, addr = sock.accept()

    # Receive file data in chunks
    data = b""
    while True:
        chunk = conn.recv(1024)
        if not chunk:
            break
        data += chunk

    # Save the received data as a file
    filename = f"received_file_{addr[0]}_{addr[1]}.mp4"
    with open(filename, "wb") as f:
        f.write(data)

    print(f"Received file: {filename} from {addr}")

    # Close current connection
    conn.close()

# Close the server socket
sock.close()

print("Server stopped")
