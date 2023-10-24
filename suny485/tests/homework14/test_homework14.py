'''
So we need to test two 2 functions:c ompute_complexity & evaluate_strength but

We have already tested the compute complexity in homework12 so lets focus on:

Testing evaluate strength function
    1. Testing strong passwords (complexity > 50)
    2. Test weak passwords (complexity < 50)
    3. Test a password with a complexity of 50
    4. Test a non string (should raise type error)
'''

import pytest
from suny485.projects.homework14.password_utilities import evaluate_strength


#  Test for strong passwords
@pytest.mark.parametrize("strong_password, expected_result", [
    ("0$$1@a%&%", True),
    ("O4$#o###E*%&", True),
    ("#w$@f###a&%h", True),
])
def test_strong(strong_password, expected_result):
    assert evaluate_strength(strong_password) == expected_result


#  Test for weak passwords
@pytest.mark.parametrize("weak_password, expected_result", [
    ("password123", False),
    ("thisIsaWeakpassowrd!", False),
    ("wowimgoingtogeth@cke!d", False),
])
def test_weak(weak_password, expected_result):
    assert evaluate_strength(weak_password) == expected_result


#  Testing for complexity of 50
def test_50():
    password = 'A$2#'
    fifty = evaluate_strength(password)
    assert fifty is False


# Testing for non string input
def test_non_string():
    non_string_input = 123  # Non-string input
    with pytest.raises(TypeError):
        evaluate_strength(non_string_input)
