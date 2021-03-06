import pytest

from weird_text.encoder import EncodedText


@pytest.mark.parametrize(
    "input_word,expected",
    [
        ("long", "lnog"),
        ("some", "smoe"),
        ("with", "wtih"),
    ],
)
def test_should_shuffle_letters_inside_four_letters_word(input_word, expected, encoder):
    assert encoder.shuffle(input_word) == expected


@pytest.mark.parametrize(
    "input_word,expected",
    [
        ("and", "and"),
        ("a", "a"),
        ("the", "the"),
    ],
)
def test_should_return_word_shorter_than_3_characters(input_word, expected, encoder):
    assert encoder.shuffle(input_word) == expected


@pytest.mark.parametrize("input_word", ["sentence", "awesome"])
def test_should_shuffle_long_words(input_word, encoder):
    assert encoder.shuffle(input_word) != input_word


@pytest.mark.parametrize(
    "input_word,expected", [("Biiiiiig", "Biiiiiig"), ("yeeeeeees", "yeeeeeees")]
)
def test_should_return_words_with_only_the_same_letters_in_the_middle(
    input_word, expected, encoder
):
    assert encoder.shuffle(input_word) == expected


def test_should_encode_whole_sentence_with_expected_words(encoder):
    text_to_encode = "This is a long test,\n with some big (biiiiig) !"

    results = encoder.encode(text_to_encode)

    assert results == EncodedText(
        "Tihs is a lnog tset,\n wtih smoe big (biiiiig) !",
        "This biiiiig long some test with".split(),
    )
