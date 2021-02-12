from decoder import Decoder
from encoder import Encoder, EncodedText


class DecodingError(Exception):
    pass


class WeirdText:
    template = """
    -weird-
    {result}
    -weird-
    {original_words}"""

    def __init__(self, encoder: Encoder, decoder: Decoder) -> None:
        self.encoder = encoder
        self.decoder = decoder

    def encode(self, text: str) -> str:
        return self.encoder.encode(text).to_full_str()

    def decode(self, text: str):
        words = text.split("\n-weird-\n")

        if len(words) != 3:
            raise DecodingError("Can not decode given text!")

        sentence_to_decode = words[1]
        original_words = words[2].split()

        return self.decoder.decode(EncodedText(sentence_to_decode, original_words))
