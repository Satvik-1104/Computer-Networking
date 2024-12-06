FLAG = b'11111'  # Flag byte sequence
ESC = b'000000'  # Escape byte sequence


def byte_stuff(data):
    stuffed_data = FLAG
    for byte in data:
        if bytes([byte]) == FLAG:
            stuffed_data += ESC + b'F'
        elif bytes([byte]) == ESC:
            stuffed_data += ESC + b'E'
        else:
            stuffed_data += bytes([byte])
    stuffed_data += FLAG
    return stuffed_data


def byte_unstuff(stuffed_data):
    unstuffed_data = b''
    i = len(FLAG)
    while i < len(stuffed_data) - len(FLAG):
        if stuffed_data[i:i + len(ESC)] == ESC:
            if stuffed_data[i + len(ESC):i + len(ESC) + 1] == b'F':
                unstuffed_data += FLAG
            elif stuffed_data[i + len(ESC):i + len(ESC) + 1] == b'E':
                unstuffed_data += ESC
            i += len(ESC) + 1
        else:
            unstuffed_data += stuffed_data[i:i + 1]
            i += 1
    return unstuffed_data


data = b'This is a test message with FLAG and ESC sequences.'
stuffed = byte_stuff(data)
print(f"Stuffed Data: {stuffed}")
unstuffed = byte_unstuff(stuffed)
print(f"Unstuffed Data: {unstuffed}")

assert data == unstuffed, "Data unstuffed incorrectly!"
