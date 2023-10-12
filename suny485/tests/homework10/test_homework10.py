import pytest
import sys
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
parent_directory = os.path.abspath(os.path.join(current_directory, "..", ".."))
sys.path.append(parent_directory)

from suny485.projects.homework10.fruit_query import is_it_a_fruit

def test_1():
    assert is_it_a_fruit('apple') == True

def test_2():
    assert is_it_a_fruit('pear') == True

def test_3():
    assert is_it_a_fruit('banana') == False

def test_4():
    assert is_it_a_fruit('grape') == True

def test_5():
    assert is_it_a_fruit('pineapple') == False

def test_6():
    assert is_it_a_fruit('') == False

def test_7():
    assert is_it_a_fruit('1') == False

if __name__ == "__main__":
    pytest.main(["test_homework10.py"])