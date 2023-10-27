from src.models import Mode

def get_encoding_mode(data: str) -> Mode:
    """Get the encoding mode for the given data"""
    return Mode.NUMERIC
