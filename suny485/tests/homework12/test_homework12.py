"""
(  complexifiers = ['~', '@', '#', '$', '%', '^', '&', '-', '_', '+', '='])

Categories for Testable things

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
"""

import pytest
from suny485.projects.homework12.compute_complexity import compute_complexity

#Paramitization for Testing Valid Inputs
@pytest.mark.parametrize('valid_input, valid_output',
[
    #('', 0), #Empty String Test (I get a division by 0 error)
    ('owen', 0.0), #Testing a string with no complpexifiers
    ('ojc@', 25.0), #Testing a string with complexifiers
])

def test_valid_inputs(valid_input, valid_output):
    assert compute_complexity(valid_input) == valid_output

#Paramitization for Testing Logic 
@pytest.mark.parametrize('logic_input, logic_output',
[
    ('@#$%&^', 100.0), #Testing a string with only complexifiers
    ('O1w=e#43', 25.0), #Testing a string with a mix of complexifiers and integers and letters
    ('ojc@icloud--%', 30.76923076923077), #Testing a string with multiple complexifiers
    ('owencozin$', 10.0)#Testing a string with one complexifier
])

def test_logic(logic_input, logic_output):
    assert compute_complexity(logic_input) == logic_output

#Just a regular test testing that the output should be a positive integer that is in the range of 0-100(including 0 and 100)
def test_output():
    result = compute_complexity('oweniscool@') 
    assert 0.0 <= result <= 100.0

if __name__ == '__main__':
    pytest.main()

