import pytest

from library import convert_kilometers, get_plural

def convert_kilometers_positive():
    assert convert_kilometers(10) == 16.0934


def convert_kilometers_zero():
    assert convert_kilometers(0) == 0


def convert_kilometers_negative():
    with pytest.raises(ValueError):
        convert_kilometers(-5)


def convert_kilometers_float():
    assert convert_kilometers(3.5) == 5.63269


def convert_kilometers_large_value():
    assert convert_kilometers(100000) == 160934

# Тести для другої функції get_plural:

def test_get_plural_list():
    assert get_plural([3, 2, 1, 2, 3, 4]) == (1, 2, 3, 4)


def test_get_plural_set():
    assert get_plural({3, 2, 1, 2, 3, 4}) == (1, 2, 3, 4)


def test_get_plural_string():
    assert get_plural("hello") == ('e', 'h', 'l', 'o')


def test_get_plural_dict():
    assert get_plural({'a': 1, 'b': 2, 'c': 3}) == ('a', 'b', 'c')


def test_get_plural_empty():
    assert get_plural([]) == ()
