import socket
import threading


def reverse_string(data):
    return data[::-1]


def handle_client(client_socket, addr):
    print(f"Connected to {addr}")

    while True:
        data = client_socket.recv(1024).decode()
        if not data:
            break
        result = reverse_string(data)
        print(f"From  {addr}::      Received: {data}    Sent: {result}")
        client_socket.send(result.encode())
    client_socket.close()
    print(f"Connection with {addr} closed")


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 5555))
    # IP Address is to distinguish between devices in a Computer Network
    # Port number is to distinguish between application programs in a Single Device
    server_socket.listen(5)
    print("Server waiting for Clients...")

    while True:
        client_socket, addr = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        client_thread.start()


if __name__ == "__main__":
    start_server()