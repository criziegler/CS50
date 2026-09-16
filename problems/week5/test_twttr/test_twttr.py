from twttr import shorten

vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

def test_shorten():
    assert shorten("Twitter") == "Twttr"
    assert shorten("Twitter1") == "Twttr1"
    assert shorten("Tweet, Tweet") == "Twt, Twt"

    for word in vowels:
        assert word != shorten(word)