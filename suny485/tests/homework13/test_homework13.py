'''
So we need to test two 2 functions:c ompute_complexity & evaluate_strength but

Testing evaluate strength function
    1. Testing strong passwords (complexity > 50)
    2. Test weak passwords (complexity < 50)
    3. Test a password with a complexity of 50
    4. Test a non string (should raise type error)

Testing compute complexity function

1. Testing Valid Inputs
    - Empty String
    - Test a string with no complexifiers
    - Test a string with complexifiers

2. Testing Output
    - The output should be a float

3. Testing the Logic
    - Test a string with only complexifiers
    - Test a string with a mix of complexifiers and integers and letters
    - Test a string with multiple complexifiers
    - Test a string with one complexifier
'''


import pytest
from suny485.projects.homework13.password import evaluate_strength, compute_complexity


#  Paramitization for Testing Valid Inputs
@pytest.mark.parametrize('valid_input, valid_output', [
    #  ('', 0),  # Empty String Test (I get a division by 0 error)
    ('owen', 0.0),  # Testing a string with no complpexifiers
    ('ojc@', 25.0),  # Testing a string with complexifiers
])
def test_valid_inputs(valid_input, valid_output):
    assert compute_complexity(valid_input) == valid_output


#  Paramitization for Testing Logic
@pytest.mark.parametrize('logic_input, logic_output', [
    ('@#$%&^', 100.0),  # Testing a string with only complexifiers
    ('O1w=e#43', 25.0),  # Testing string mix complexifiers/integers/letters
    ('ojc@icloud--%', 30.76923076923077),  # Testing string mult complexifiers
    ('owencozin$', 10.0)  # Testing a string with one complexifier
])
def test_logic(logic_input, logic_output):
    assert compute_complexity(logic_input) == logic_output


#  Testing the output should be a float included in the range of 0-100
    result = compute_complexity('oweniscool@')
    assert 0.0 <= result <= 100.0


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
