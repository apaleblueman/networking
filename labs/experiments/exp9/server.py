import socket

HOST = '0.0.0.0'      # Listen on all interfaces (INADDR_ANY in C)
PORT = 8080
BUFFER_SIZE = 1024

def start_server():
    # 1. Create a UDP (datagram) socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2. Bind — required on server so clients know where to send
    server_socket.bind((HOST, PORT))
    print(f"UDP server listening on {HOST}:{PORT}")
    print("Waiting for a datagram...")

    # 3. Receive one datagram. recvfrom() returns (data, client_address)
    data, client_addr = server_socket.recvfrom(BUFFER_SIZE)
    message = data.decode('utf-8')
    print(f"Client ({client_addr}) sent: {message}")

    # 4. Send reply back to the source address
    reply = "Hello from server"
    server_socket.sendto(reply.encode('utf-8'), client_addr)
    print(f"Replied to {client_addr}: {reply}")

    # 5. Cleanup
    server_socket.close()
    print("Server closed")

if __name__ == "__main__":
    start_server()
