import socket

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 8080
BUFFER_SIZE = 1024

def start_client():
    # 1. Create a UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2. Send a datagram to the server (no connect!)
    message = "Hello from client"
    client_socket.sendto(message.encode('utf-8'), (SERVER_HOST, SERVER_PORT))
    print(f"Sent to server: {message}")

    # 3. Wait for reply. recvfrom() gives back (data, server_address)
    data, server_addr = client_socket.recvfrom(BUFFER_SIZE)
    print(f"Server ({server_addr}) replied: {data.decode('utf-8')}")

    # 4. Cleanup
    client_socket.close()
    print("Client closed")

if __name__ == "__main__":
    start_client()
