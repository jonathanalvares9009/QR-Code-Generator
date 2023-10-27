from src.models import Mode
from src.encoding_mode import get_encoding_mode

def test_is_mode_numeric():
    data = "123"
    mode = get_encoding_mode(data)
    assert mode == Mode.NUMERIC

def test_is_mode_alphanumeric():
    data = "ABC$%90"
    mode = get_encoding_mode(data)
    assert mode == Mode.ALPHANUMERIC

def test_is_not_mode_alphanumeric():
    data = "abc90"
    mode = get_encoding_mode(data)
    assert mode != Mode.ALPHANUMERIC

def test_is_mode_byte():
    data = "ÕÉē90ABC"
    mode = get_encoding_mode(data)
    assert mode == Mode.BYTE

def test_is_mode_kanji():
    data = "漢字"
    mode = get_encoding_mode(data)
    assert mode == Mode.KANJI
