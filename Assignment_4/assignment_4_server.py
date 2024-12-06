import socket
import threading
import select
import time
import signal
import sys


def start_timer(timeout, timeout_callback):
    def timer_thread():
        time.sleep(timeout)
        timeout_callback()

    thread = threading.Thread(target=timer_thread, daemon=True)
    thread.start()
    return thread


def timeout_callback():
    print("Timer expired, resending the frame...")
    global resend_frame_flag
    resend_frame_flag = True


def start_server(filename):
    global resend_frame_flag
    resend_frame_flag = False
    timeout = 5  # seconds

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 12345))
    server_socket.listen(1)
    print("Server started, waiting for clients...")

    try:
        client_socket, _ = server_socket.accept()
        print("Client connected.")

        with open(filename, 'rb') as file:
            sequence_number = 0
            while True:
                frame = file.read(256)  # Adjust frame size as needed
                if not frame:
                    break

                data_to_send = f"{sequence_number:04d}".encode() + frame
                client_socket.sendall(data_to_send)
                print(f"Sent Frame {sequence_number:04d}")

                # Start the timer for this frame
                timer_thread = start_timer(timeout, timeout_callback)

                # Wait for acknowledgment
                while True:
                    ready = select.select([client_socket], [], [], timeout)
                    if ready[0]:
                        ack = client_socket.recv(1024).decode()
                        print(f"Received ACK {ack}")
                        if int(ack) == sequence_number:
                            sequence_number += 1
                            resend_frame_flag = False
                            break  # Break out of the loop to send the next frame

                    if resend_frame_flag:
                        client_socket.sendall(data_to_send)
                        print(f"Resent Frame {sequence_number:04d}")
                        resend_frame_flag = False
                        # Restart the timer for the resent frame
                        timer_thread = start_timer(timeout, timeout_callback)

    except KeyboardInterrupt:
        print("\nServer shutting down...")
    finally:
        client_socket.close()
        server_socket.close()


if __name__ == "__main__":
    # Register signal handler for Ctrl+C
    signal.signal(signal.SIGINT, lambda s, e: sys.exit(0))
    start_server('data.txt')
