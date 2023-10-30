from src.models import Level, Mode
from src.encoding import get_encoded_alphanumeric_payload, get_encoded_kanji_payload, get_encoded_numeric_payload, get_encoded_byte_payload, get_mode_indicator, get_encoded_data

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

def test_is_valid_encoded_alphanumeric_payload():
    assert get_encoded_alphanumeric_payload("HELLO CC WORLD") == '01100001011011110001101000101110001000101000110011101001000101001101110111110'

def test_is_valid_encoded_byte_payload():
    assert get_encoded_byte_payload("Hello") == "0100100001100101011011000110110001101111"

def test_is_valid_encoded_kanji_payload():
    assert get_encoded_kanji_payload("覚") == "0011011101111"

def test_is_valid_encoded_payload():
    assert get_encoded_data("Hello World", Level.M) == "01000000101101001000011001010110110001101100011011110010000001010111011011110111001001101100011001000000111011000001000111101100000100011110110000010001111011000001000111101100000100011110110000010001111011000001000111101100000100011110110000010001111011000001000111101100000100011110110000010001111011000001000111101100000100011110110000010001111011000001000111101100000100011110110000010001111011000001000111101100000100011110110000010001111011000001000111101100000100011110110000010001111011000001000111101100"
