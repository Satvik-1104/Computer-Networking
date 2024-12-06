"""
    Another Routing Table
    ('C4.5E.2.0/23', 'A'),
    ('C4.5E.4.0/22', 'B'),
    ('C4.5E.C0.0/19', 'C'),
    ('C4.5E.40.0/18', 'D'),
    ('C4.4C.0.0/14', 'E'),
    ('C0.0.0.0/2', 'F'),
    ('80.0.0.0/1', 'G')

    ('C4.4B.00.00/16', 'F'),
    ('C4.5E.00.00/16', 'B'),
    ('C4.4D.00.00/16', 'E'),
    ('C4.5E.03.00/24', 'A'),
    ('C4.5E.7F.00/24', 'D'),
    ('C4.5E.D1.00/24', 'C')

    Another Test Case
    'C4.5E.2.1',
    'C4.5E.3.255',
    'C4.5E.4.1',
    'C4.5E.CF.255',
    'C4.5E.40.1',
    'C4.4C.255.255',
    'C4.5E.2.0',
    'C4.5E.4.0',
    'C4.5E.C0.0',
    'C4.5E.40.0',
    'C4.4C.0.0',
    'C0.0.0.1',
    '79.255.255.255',
    '80.0.0.1',
    'C4.5E.5.0',
    'C4.5E.C1.0',
    'C4.4D.0.0'

    'C4.4B.31.2E',
    'C4.5E.05.09',
    'C4.4D.31.2E',
    'C4.5E.03.87',
    'C4.5E.7F.12',
    'C4.5E.D1.02'
"""

# Routing table
routing_table = [
    ('C4.5E.2.0/23', 'A'),
    ('C4.5E.4.0/22', 'B'),
    ('C4.5E.C0.0/19', 'C'),
    ('C4.5E.40.0/18', 'D'),
    ('C4.4C.0.0/14', 'E'),
    ('C0.0.0.0/2', 'F'),
    ('80.0.0.0/1', 'G')
]


def convert_ip_to_binary(ip):
    # Conversion of IP addresses to Binary Strings
    parts = ip.split('.')
    binary_parts = []

    for part in parts:
        if len(part) == 2 and part.isalnum():  # Assumes hex part (e.g., C0, 5E)
            try:
                binary_parts.append(format(int(part, 16), '08b'))
            except ValueError:
                raise ValueError(f"Unsupported hexadecimal part: {part}")
        else:
            try:
                binary_parts.append(format(int(part), '08b'))
            except ValueError:
                raise ValueError(f"Unsupported decimal part: {part}")

    return ''.join(binary_parts)


def longest_prefix_match(dest_ip, routing_table):
    # Checking for the best match from the routing table
    try:
        dest_ip_bin = convert_ip_to_binary(dest_ip)
    except ValueError as e:
        print(e)
        return None  # Return None if there is an unsupported format

    longest_prefix_len = -1
    best_line = None

    for entry in routing_table:
        network, line = entry
        network_ip, prefix_len = network.split('/')
        prefix_len = int(prefix_len)

        # Convert network IP to binary
        try:
            network_ip_bin = convert_ip_to_binary(network_ip)
        except ValueError as e:
            print(e)
            continue  # Skip if the format is unsupported

        # Compare prefixes
        if dest_ip_bin[:prefix_len] == network_ip_bin[:prefix_len]:
            if prefix_len > longest_prefix_len:
                longest_prefix_len = prefix_len
                best_line = line

    return best_line


# Test cases
test_cases = [
    'C4.5E.2.1',
    'C4.5E.3.255',
    'C4.5E.4.1',
    'C4.5E.CF.255',
    'C4.5E.40.1',
    'C4.4C.255.255',
    'C4.5E.2.0',
    'C4.5E.4.0',
    'C4.5E.C0.0',
    'C4.5E.40.0',
    'C4.4C.0.0',
    'C0.0.0.1',
    '79.255.255.255',
    '80.0.0.1',
    'C4.5E.5.0',
    'C4.5E.C1.0',
    'C4.4D.0.0'
]

for ip in test_cases:
    result = longest_prefix_match(ip, routing_table)
    if result is not None:
        print(f"Packet to {ip}: Forward to {result}")
    else:
        print(f"Packet to {ip}: No valid forwarding line found.")
