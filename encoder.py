import random
import re
from copy import deepcopy

tokenize_re = re.compile(r"(\w+)", re.U)

template = """
-weird-
{result}
-weird
{original_words}"""


def encode(sentence: str) -> str:
    words = tokenize_re.findall(sentence)
    for word in words:
        randomized_word = shuffle(word)
        sentence = sentence.replace(word, randomized_word)

    original_words = " ".join(sorted([word for word in words if len(word) >= 4]))

    return template.format(result=sentence, original_words=original_words)


def shuffle(word: str) -> str:
    """
    Accepts single word and try to randomize it inside.
    """
    letters_to_shuffle = [letter for letter in word[1:-1]]
    shuffled_letters = deepcopy(letters_to_shuffle)

    if len(word) < 4:
        return word

    if len(set(letters_to_shuffle)) == 1:
        return word

    while letters_to_shuffle == shuffled_letters:
        random.shuffle(shuffled_letters)

    return f"{word[0]}{''.join(shuffled_letters)}{word[-1]}"
