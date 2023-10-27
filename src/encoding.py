from enum import Enum
from src.models import Mode

class Level(Enum):
    L = 'L'
    M = 'M'
    Q = 'Q'
    H = 'H'

def get_mode_indicator(mode: Mode) -> str:
    return {
        Mode.NUMERIC: '0001',
        Mode.ALPHANUMERIC: '0010',
        Mode.BYTE: '0100',
        Mode.KANJI: '1000',
    }[mode]

# def get_encoded_data(data: str, level: Level = Level.L) -> str:
