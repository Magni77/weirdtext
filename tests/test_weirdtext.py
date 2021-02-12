def test_should_encode_whole_text_sentence_with_expected_words(weird_text):
    text_to_encode = "This is a long test,\n with some big (biiiiig) !"

    results = weird_text.encode(text_to_encode)

    assert (
        results
        == "\n-weird-\nTihs is a lnog tset,\n wtih smoe big (biiiiig) !\n-weird-\nThis biiiiig long some test with"
    )
