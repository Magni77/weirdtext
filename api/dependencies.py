from decoder import Decoder
from encoder import Encoder
from weird_text import WeirdText


def weird_text_service():
    return WeirdText(Encoder(), Decoder())
