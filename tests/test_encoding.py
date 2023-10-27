from src.models import Mode
from src.encoding import get_mode_indicator

def test_is_encoding_mode_indicator_numerical():
    assert get_mode_indicator(Mode.NUMERIC) == '0001'

def test_is_encoding_mode_indicator_alphanumeric():
    assert get_mode_indicator(Mode.ALPHANUMERIC) == '0010'

def test_is_encoding_mode_indicator_byte():
    assert get_mode_indicator(Mode.BYTE) == '0100'

def test_is_encoding_mode_indicator_kanji():
    assert get_mode_indicator(Mode.KANJI) == '1000'
