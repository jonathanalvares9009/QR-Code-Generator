import re
from src.models import Mode

def get_encoding_mode(data: str) -> Mode:
    """Get the encoding mode for the given data"""
    if re.match(r'^[\u4e00-\u9faf]+$', data):
        return Mode.KANJI
    if re.match(r'^[0-9]+$', data):
        return Mode.NUMERIC
    if re.match(r'^[0-9A-Z $%*+./:-]+$', data):
        return Mode.ALPHANUMERIC
    return Mode.BYTE
