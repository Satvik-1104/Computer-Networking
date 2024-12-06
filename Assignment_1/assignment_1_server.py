import socket


def reverse_string(data):
    return data[::-1]


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 5555))
    server_socket.listen(1)
    print("Server waiting on port 5555...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Client {addr} connected to Server")
        while True:
            received = client_socket.recv(1024).decode()
            if not received:
                break
            send = reverse_string(received)
            print("Received: " + received + "    Sent: " + send)
            client_socket.send(send.encode())

        client_socket.close()
        print(f"Connection to {addr} closed")


if __name__ == "__main__":
    start_server()
