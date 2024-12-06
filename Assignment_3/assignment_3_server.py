import socket
import threading

clients = {}
node_counter = 1


def handle_client(client_socket, node_number):
    global node_counter
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break

            print(f"Received message from node {node_number}: {message}")
            broadcast(message, node_number)

        except ConnectionResetError:
            break

    print(f"Node {node_number} disconnected")
    clients.pop(node_number, None)
    client_socket.close()


def broadcast(message, sender_node):
    try:
        sender, msg = message.split(":", 1)
        msg_content, dest_label = msg.rsplit("to Node ", 1)
        dest_node = int(dest_label.strip())

        for node, client in clients.items():
            if node != sender_node:
                if node == dest_node:
                    try:
                        client.send(message.encode('utf-8'))
                    except Exception as e:
                        print(f"Error sending message to node {node}: {e}")
                else:
                    print(f"Node {node} discarded the message from node {sender_node} meant for node {dest_node}")
    except ValueError:
        print("Failed to parse the destination node from the message.")


def start_server():
    global node_counter
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12346))
    server_socket.listen(5)
    print("Server started, waiting for clients...")

    try:
        while True:
            client_socket, _ = server_socket.accept()
            node_number = node_counter
            node_counter += 1
            print(f"Node {node_number} connected")
            clients[node_number] = client_socket

            client_thread = threading.Thread(target=handle_client, args=(client_socket, node_number))
            client_thread.start()

    except KeyboardInterrupt:
        print("Server shutting down...")
    finally:
        server_socket.close()
        for client in clients.values():
            client.close()


if __name__ == "__main__":
    start_server()
