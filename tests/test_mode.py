from src.models import Mode
from src.encoding_mode import get_encoding_mode

def test_is_mode_numeric():
    data = "123"
    mode = get_encoding_mode(data)
    assert mode == Mode.NUMERIC

def test_is_mode_alphanumeric():
    data = "ABC"
    mode = get_encoding_mode(data)
    assert mode == Mode.ALPHANUMERIC
