import pytest
from fuel import convert, gauge


def test_convert():
    assert convert("3/4") == 75

def test_convert_valueError():

    with pytest.raises(ValueError):
        convert("cat/cat")

    with pytest.raises(ValueError):
        convert("-2/4")

    with pytest.raises(ValueError):
        convert("3/2")

def test_convert_zeroDivisionError():

    with pytest.raises(ZeroDivisionError):
        convert("3/0")
    

def test_gauge():
    assert gauge(75) == "75%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"