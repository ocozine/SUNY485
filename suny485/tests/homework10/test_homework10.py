import pytest


from suny485.projects.homework10.fruit_query import is_it_a_fruit


def test_1():
    assert is_it_a_fruit('apple') is True


def test_2():
    assert is_it_a_fruit('pear') is True


def test_3():
    assert is_it_a_fruit('banana') is False


def test_4():
    assert is_it_a_fruit('grape') is True


def test_5():
    assert is_it_a_fruit('pineapple') is False


def test_6():
    assert is_it_a_fruit('') is False


def test_7():
    assert is_it_a_fruit('1') is False


if __name__ == "__main__":
    pytest.main(["test_homework10.py"])
