import socket

HOST = '127.0.0.1'   # localhost — same machine
PORT = 5000
BUFFER_SIZE = 1024

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    server_socket.bind((HOST, PORT))
    
    server_socket.listen(5)
    print(f"Server started on {HOST}:{PORT}")
    print("Waiting for a client...")
    
    conn, addr = server_socket.accept()
    print(f"Client accepted from {addr}")
    
    while True:
        data = conn.recv(BUFFER_SIZE)
        if not data:
            break
        
        message = data.decode('utf-8')
        print(f"Received: {message}")
        
        if message.strip() == "Over":
            print("Client sent 'Over' — closing connection")
            break
        
        conn.sendall(data)
    
    conn.close()
    server_socket.close()
    print("Server closed")

if __name__ == "__main__":
    start_server()
