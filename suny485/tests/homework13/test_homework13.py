'''
1. Test strong passwords (complexity > 50)
2. Test weak passwords (complexity < 50)
3. Test a password with a complexity of 50
4. Test a non string (should raise type error)
'''

import pytest
from suny485.projects.homework13.password import evaluate_strength


#  Test for strong passwords
@pytest.mark.parametrize("strong_password, expected_result", [
    ("0w3n$Co&%n@", True),
    ("O4$#oE*%&", True),
    ("Kw$@fa&%h", True),
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
    password = 'A@2b#3C'
    fifty = evaluate_strength(password)
    assert fifty is True


# Testing for non string input
def test_non_string():
    non_string_input = 123  # Non-string input
    with pytest.raises(TypeError):
        evaluate_strength(non_string_input)
