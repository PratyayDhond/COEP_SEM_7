import socket
import time

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 9999))  # Connect to the server on localhost

    try:
        while True:
            # Send a message to the server
            message = "Hello Server!"
            client.send(message.encode('utf-8'))
            response = client.recv(4096)
            print(f"[RECEIVED] {response.decode('utf-8')}")
            time.sleep(1)  # Wait before sending the next message
    except KeyboardInterrupt:
        print("Client shutting down.")
    finally:
        client.close()

if __name__ == "__main__":
    start_client()
