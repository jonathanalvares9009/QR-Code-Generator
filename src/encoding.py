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
