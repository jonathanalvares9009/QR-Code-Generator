from src.models import Mode
from src.encoding import get_encoded_numeric_payload, get_mode_indicator

def test_is_encoding_mode_indicator_numerical():
    assert get_mode_indicator(Mode.NUMERIC) == '0001'

def test_is_encoding_mode_indicator_alphanumeric():
    assert get_mode_indicator(Mode.ALPHANUMERIC) == '0010'

def test_is_encoding_mode_indicator_byte():
    assert get_mode_indicator(Mode.BYTE) == '0100'

def test_is_encoding_mode_indicator_kanji():
    assert get_mode_indicator(Mode.KANJI) == '1000'

def test_is_valid_encoded_numeric_payload():
    assert get_encoded_numeric_payload("291") == '0100100011'
    assert get_encoded_numeric_payload("76") == '1001100'
    assert get_encoded_numeric_payload("4") == '0100'
