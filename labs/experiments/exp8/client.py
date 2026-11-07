import socket

HOST = '127.0.0.1'
PORT = 5000

def start_client():
    # 1. Create TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 2. Connect to server
    client_socket.connect((HOST, PORT))
    print(f"Connected to server at {HOST}:{PORT}")
    print("Type messages. Type 'Over' to quit.")
    
    while True:
        message = input("> ")
        client_socket.sendall(message.encode('utf-8'))
        
        if message.strip() == "Over":
            print("Sending 'Over' — closing connection")
            break
        
        # Receive echo
        data = client_socket.recv(1024)
        print(f"Server echoed: {data.decode('utf-8')}")
    
    # 3. Close
    client_socket.close()
    print("Client closed")

if __name__ == "__main__":
    start_client()
