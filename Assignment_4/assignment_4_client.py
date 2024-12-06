import socket
import argparse
import time
import signal
import sys


def start_client(output_filename, simulate_lost_ack=False):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("localhost", 12345))
    counter = 0
    with open(output_filename, 'wb') as file:
        expected_sequence_number = 0
        while True:
            data = client_socket.recv(256 + 4)  # Read frame size + 4 bytes for sequence number
            if not data:
                break

            sequence_number = int(data[:4].decode())
            frame_data = data[4:]

            print(f"Received Frame {sequence_number:04d}")
            if sequence_number == expected_sequence_number:
                file.write(frame_data)
                expected_sequence_number += 1
                ack = sequence_number
            else:
                ack = expected_sequence_number - 1

            # Simulate lost ACK
            if simulate_lost_ack and sequence_number == 0 and counter == 0:  # Modify this condition as needed
                counter += 1
                print("Simulating lost ACK for Frame 0000")
                time.sleep(1)  # Delay to simulate processing time
                continue  # Skip sending the ACK

            print(f"Sending ACK {ack:04d}")
            client_socket.sendall(f"{ack:04d}".encode())

    client_socket.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Start the client for the Stop-and-Wait ARQ protocol.")
    parser.add_argument("--simulate_lost_ack", type=bool, default=False,
                        help="Simulate lost acknowledgment (ACK) frame.")
    args = parser.parse_args()

    # Register signal handler for Ctrl+C
    signal.signal(signal.SIGINT, lambda s, e: sys.exit(0))
    start_client('output.txt', simulate_lost_ack=args.simulate_lost_ack)
