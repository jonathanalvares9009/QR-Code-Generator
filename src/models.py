from enum import Enum

class Mode(Enum):
    """Enum for encoding mode"""
    NUMERIC = "NUMERIC"
    ALPHANUMERIC = "ALPHANUMERIC"
    BYTE = "BYTE"
    KANJI = "KANJI"
    