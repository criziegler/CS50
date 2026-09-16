from bank import value

def test_value():

    assert value("Hello") == 0
    assert value("How are you?") == 20

    for word in ["Good to see you", "Moin", "Not now"]:
        assert value(word) == 100