from weird_text import WeirdText, Encoder, Decoder


def weird_text_service():
    return WeirdText(Encoder(), Decoder())
