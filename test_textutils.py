from textutils import first_word

def test_first_word_basic():
    assert first_word("hello world") == "hello"

def test_first_word_empty_returns_empty():
    # bu test su an FAIL ediyor (IndexError) -> reproduce hedefi
    assert first_word("") == ""
