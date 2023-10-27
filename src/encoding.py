from src.models import Mode

def get_mode_indicator(mode: Mode) -> str:
    return {
        Mode.NUMERIC: '0001',
        Mode.ALPHANUMERIC: '0010',
        Mode.BYTE: '0100',
        Mode.KANJI: '1000',
    }[mode]

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
