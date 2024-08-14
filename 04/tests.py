import pytest
from main import concatenation


@pytest.mark.parametrize("str1, str2, expected", [
    ("Hello", "World", "HelloWorld"),
    ("", "", ""),
    ("", "For the Horde!", "For the Horde!"),

])
def test_param(str1, str2, expected):
    assert concatenation(str1, str2) == expected


def test_error():
    with pytest.raises(TypeError, match="Both arguments must be strings"):
        concatenation(1, "Hello")


def test_not_eq():
    assert concatenation("Hello", "World") != "hello world"


def test_ngt_1():
    assert concatenation("A", "") < "a"


@pytest.mark.xfail(reason='Намеренный провал')
def test_fail():
    assert False


@pytest.mark.skip(reason='Намеренный пропуск')
def test_skip():
    assert False
