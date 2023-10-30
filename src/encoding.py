from src.encoding_mode import get_encoding_mode
from src.models import Mode, Level, NumberOfBits

def get_mode_indicator(mode: Mode) -> str:
    return {
        Mode.NUMERIC: '0001',
        Mode.ALPHANUMERIC: '0010',
        Mode.BYTE: '0100',
        Mode.KANJI: '1000',
    }[mode]

# Number of codewords for version 4
def get_number_of_codewords() -> int:
    return {
        Level.L: 80,
        Level.M: 64,
        Level.Q: 48,
        Level.H: 36,
    }

# Get the character count indicator
def get_character_indicator(data: str, mode: Mode) -> str:
    """Returns the character count indicator"""
    if mode == Mode.NUMERIC:
        return bin(len(data))[2:].zfill(10)
    elif mode == Mode.ALPHANUMERIC:
        return bin(len(data))[2:].zfill(9)
    elif mode == Mode.BYTE:
        return bin(len(data))[2:].zfill(8)
    elif mode == Mode.KANJI:
        return bin(len(data) // 2)[2:].zfill(8)


def get_encoded_numeric_payload(data: str) -> str:
    """Returns the encoded payload for numeric mode"""
    payload = ""
    # Break the data into groups of 3
    for i in range(0, len(data), 3):
        # Get the current group
        group = data[i:i+3]
        if int(group) > 99:
            payload += bin(int(group))[2:].zfill(10)
        elif int(group) > 9:
            payload += bin(int(group))[2:].zfill(7)
        else:
            payload += bin(int(group))[2:].zfill(4)
    return payload

def get_alphanumeric_number_representation(character: str) -> int:
    mapping = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 18, 'J': 19,
        'K': 20, 'L': 21, 'M': 22, 'N': 23, 'O': 24, 'P': 25, 'Q': 26, 'R': 27, 'S': 28, 'T': 29,
        'U': 30, 'V': 31, 'W': 32, 'X': 33, 'Y': 34, 'Z': 35, ' ': 36, '$': 37, '%': 38, '*': 39,
        '+': 40, '-': 41, '.': 42, '/': 43, ':': 44
    }
    return mapping.get(character, None)

def get_encoded_alphanumeric_payload(data: str) -> str:
    """Returns the encoded payload for alphanumeric mode"""
    payload = ""
    # Break the data into groups of 2
    for i in range(0, len(data), 2):
        # Get the current group
        group = data[i:i+2]
        if len(group) == 2:
            payload += bin(
                get_alphanumeric_number_representation(group[0]) * 45 +
                get_alphanumeric_number_representation(group[1])
            )[2:].zfill(11)
        else:
            payload += bin(get_alphanumeric_number_representation(group[0]))[2:].zfill(11)
    return payload

def get_encoded_byte_payload(data: str) -> str:
    """Returns the encoded payload for byte mode"""
    payload = ""
    for character in data:
        payload += bin(ord(character))[2:].zfill(8)
    return payload

def get_encoded_kanji_payload(data: str) -> str:
    """Returns the encoded payload for kanji mode"""
    payload = ""
    for character in data:
        byte = character.encode('shift-jis').hex()
        # Check if the character is between 0x8140 and 0x9FFC, 
        # subtract 0x8140; otherwise, subtract 0xC140.
        updated_byte = int(byte, 16) - (0x8140 if 0x8140 <= int(byte, 16) <= 0x9FFC else 0xC140)
        # Split the byte into two parts
        first_part = updated_byte >> 8
        second_part = updated_byte & 0xFF
        # Multiply the most significant byte by 0xC0, 
        # add the least significant byte to the result, 
        # and convert the result into a 13 bit binary string.
        payload += bin((first_part * 0xC0) + second_part)[2:].zfill(13)
    return payload
