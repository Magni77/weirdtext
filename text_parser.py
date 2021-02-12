import re

tokenize_re = re.compile(r"(\w+)", re.U)


def get_words(sentence: str) -> list:
    return tokenize_re.findall(sentence)
