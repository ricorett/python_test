import pytest
from main import concatenation


@pytest.mark.parametrize("str1, str2, expected", [
    ("Hello", "World", "HelloWorld"),
    ("", "", ""),
    ("", "For the Horde!", "For the Horde!"),

])
def test_param(str1, str2, expected):
    assert concatenation(str1, str2) == expected


def test_sum_1():
    assert concatenation("Hello", "World") == "HelloWorld"


def test_sum_2():
    assert concatenation('', '') == ''


def test_sum_3():
    assert concatenation("", "For the Horde!") == "For the Horde!"


def test_error():
    with pytest.raises(TypeError, match="Both arguments must be strings"):
        concatenation(1, "Hello")


def test_not_eq():
    assert concatenation("Hello", "World") != "Hello World"

@pytest.mark.xfail(reason='Намеренный провал')
def test_fail():
    assert False


@pytest.mark.skip(reason='Намеренный пропуск')
def test_skip():
    assert False