import random
from copy import deepcopy
from dataclasses import dataclass
from typing import List

from text_parser import get_words


@dataclass
class EncodedText:
    encoded_text: str
    original_words: List[str]
    _template: str = """\n-weird-\n{result}\n-weird-\n{original_words}"""

    def replace_word(self, original_word: str, new_word: str):
        self.encoded_text = self.encoded_text.replace(original_word, new_word)

    def to_full_str(self) -> str:
        return self._template.format(
            result=self.encoded_text, original_words=" ".join(self.original_words)
        )


class Encoder:
    def encode(self, text: str) -> EncodedText:
        words = get_words(text)

        for word in words:
            randomized_word = self.shuffle(word)
            text = text.replace(word, randomized_word)

        original_words = list(sorted([word for word in words if len(word) > 3]))

        return EncodedText(text, original_words)

    def shuffle(self, word: str) -> str:
        """
        Accepts single word and try to randomize it inside.
        """
        letters_to_shuffle = [letter for letter in word[1:-1]]
        shuffled_letters = deepcopy(letters_to_shuffle)

        if len(word) < 4 or self._consists_of_one_unique_letter(letters_to_shuffle):
            return word

        while letters_to_shuffle == shuffled_letters:
            random.shuffle(shuffled_letters)

        return word.replace(word[1:-1], "".join(shuffled_letters))

    @staticmethod
    def _consists_of_one_unique_letter(letters_to_shuffle: list) -> bool:
        return len(set(letters_to_shuffle)) == 1
