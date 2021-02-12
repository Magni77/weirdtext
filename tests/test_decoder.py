from encoder import EncodedText


def test_should_decode_encoded_text(decoder):
    text_to_decode = "Tihs is a lnog tset sntceene,\n wtih smoe big (biiiiig) !"
    original_words = "This biiiiig long sentence some test with".split()

    result = decoder.decode(EncodedText(text_to_decode, original_words))

    assert result == "This is a long test sentence,\n with some big (biiiiig) !"


def test_should_decode_full_encoded_text_str(weird_text):
    text_to_decode = "\n-weird-\nTihs is a lnog loonog tset sntceene,\n wtih smoe big (biiiiig) wdros!\n-weird-\nlong looong sentence some test This with words"

    result = weird_text.decode(text_to_decode)

    assert (
        result
        == "This is a long looong test sentence,\n with some big (biiiiig) words!"
    )


def test_decoder_can_decode_encoded_text(encoder, decoder):
    # given
    original_text = (
        "This is a long looong test sentence,\n with some big (biiiiig) words!"
    )
    # and
    encoded_text = encoder.encode(original_text)

    # when
    decoded_text = decoder.decode(encoded_text)

    # then
    assert decoded_text == original_text
