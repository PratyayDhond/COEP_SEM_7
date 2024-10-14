import socket
import threading

MAX_CONNECTIONS = 100
connectionCount = 0
def handle_client(client_socket):
    while True:
        try:
            # Receive data from the client
            request = client_socket.recv(1024)
            if not request:
                break
            print(f"[RECEIVED] {request.decode('utf-8')}")
            message = "Hello Client!"
            # Echo the received message back to the client
            client_socket.sendall(message.encode('utf-8'))
        except ConnectionResetError:
            break
    client_socket.close()
    connectionCount-=1

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 9999))  # Bind to all interfaces on port 9999
    server.listen(5)
    connectionCount = 0
    print("[LISTENING] Server is listening on port 9999")

    while True:
        if connectionCount > MAX_CONNECTIONS:
            print("Max Connections reached! Server did not respond")
            continue
        client_socket, addr = server.accept()
        print(f"[CONNECTED] Client connected from {addr}")
        connectionCount+=1
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    start_server()
