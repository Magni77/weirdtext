from typing import List

from encoder import EncodedText
from text_parser import get_words


class Decoder:
    def decode(self, text: EncodedText):
        words = get_words(text.encoded_text)

        for word in words:
            text.replace_word(word, self._decode_word(word, text.original_words))

        return text.encoded_text

    @classmethod
    def _decode_word(cls, word: str, original_words: List[str]) -> str:
        for pattern in original_words:
            if sorted(word) == sorted(pattern):
                return pattern

        return word
