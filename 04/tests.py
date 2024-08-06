import pytest
from main import concatenation


def test_sum_1():
    assert concatenation("Hello", "World") == "HelloWorld"


def test_sum_2():
    assert concatenation('', '') == ''


def test_sum_3():
    assert concatenation("", "For the Horde!") == "For the Horde!"


@pytest.mark.xfail(reason='Намеренный провал')
def test_fail():
    assert False


@pytest.mark.skip(reason='Намеренный пропуск')
def test_skip():
    assert False