from enum import Enum

class Mode(Enum):
    """Enum for encoding mode"""
    NUMERIC = "NUMERIC"
    ALPHANUMERIC = "ALPHANUMERIC"
    BYTE = "BYTE"
    KANJI = "KANJI"
    
class Level(Enum):
    L = 'L'
    M = 'M'
    Q = 'Q'
    H = 'H'

class ErrorCorrectionLevel(Enum):
    L = {'Numeric': 187, 'Alpha Numeric': 114, 'Byte': 78, 'Kanji': 48}
    M = {'Numeric': 149, 'Alpha Numeric': 90, 'Byte': 62, 'Kanji': 38}
    Q = {'Numeric': 111, 'Alpha Numeric': 67, 'Byte': 46, 'Kanji': 28}
    H = {'Numeric': 82, 'Alpha Numeric': 50, 'Byte': 34, 'Kanji': 21}

class NumberOfBits(Enum):
    NUMERIC = 10
    ALPHANUMERIC = 9
    BYTE = 8
    KANJI = 8
