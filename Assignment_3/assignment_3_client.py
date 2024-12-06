import socket
import threading


def listen_for_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                sender_node, msg = message.split(":", 1)
                msg_content, dest_label = msg.rsplit("to Node ", 1)
                dest_node = dest_label.strip()

                if dest_node == str(client_node):
                    print(f"Received message from node {sender_node}: {msg_content.strip()}")
        except ConnectionResetError:
            print("Server closed the connection.")
            break

    client_socket.close()


def start_client():
    global client_node
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12346))

    client_node = int(input("Enter your node number: "))

    threading.Thread(target=listen_for_messages, args=(client_socket,)).start()

    while True:
        message = input(f"Node {client_node} > ")
        if message.lower() == "exit":
            client_socket.send(f"{client_node}: exit to Node {client_node}".encode('utf-8'))
            print("Exiting...")
            break

        destination_node = input("Enter destination node number: ")
        full_message = f"{client_node}: {message} to Node {destination_node}"
        client_socket.send(full_message.encode('utf-8'))

    client_socket.close()


if __name__ == "__main__":
    start_client()
