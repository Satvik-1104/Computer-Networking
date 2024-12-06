import socket


def start_client(server_ip, server_port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    try:
        while True:
            user_input = input("Enter a String: ")
            if user_input.lower() == 'exit' or user_input.lower() == '':
                break
            client_socket.send(user_input.encode())
            result = client_socket.recv(1024).decode()
            print("Sent: " + user_input + "    Received: " + result)
    except KeyboardInterrupt:
        print("Client Connection Cancelled")
    finally:
        client_socket.close()


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python assignment_1_client.py <server_ip> <server_port>")
        sys.exit(0)

    server_ip = sys.argv[1]
    server_port = int(sys.argv[2])
    start_client(server_ip, server_port)
