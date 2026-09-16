from plates import is_valid

def test_start_with_two_letters():
    assert is_valid("CS") == True
    assert is_valid("12") == False


def test_contains_special_char():
    assert is_valid("CS,-") == False

    for char in ["/", ",", "-", ".", "_"]:
        assert is_valid(char) == False

def test_plate_length():
    assert is_valid("CS50123") == False

def test_plate_layout():
    assert is_valid("CS0500") == False
    assert is_valid("CS50DD") == False