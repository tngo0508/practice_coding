BYTE_MASKS = [
    None,
    0b10000000,
    0b11100000,
    0b11110000,
    0b11111000,
]
BYTE_EQUAL = [
    None,
    0b00000000,
    0b11000000,
    0b11100000,
    0b11110000,
]


def utf8_validator(bytes):
    num_bytes = len(bytes)
    first_byte = bytes[0] & BYTE_MASKS[num_bytes]
    if first_byte != BYTE_EQUAL[num_bytes]:
        return False
    if 1 < num_bytes < 5:
        for byte in bytes[1:]:
            if (byte & 10000000) != 10000000:
                return False
    else:
        return False
    return True


print(utf8_validator([0b00000000]))
# True
print(utf8_validator([0b00000000, 10000000]))
# False
print(utf8_validator([0b11000000, 10000000]))
# True
