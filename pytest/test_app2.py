#fixtures are simply functions which is used to feed some sort of input data into the test.

import pytest

@pytest.fixture
def input_val(): #this is our fixture function
    input=20
    return input

def test_div(input_val): #fixture name is passing as an input parameter
    assert input_val % 3 == 0
    
def test_div2(input_val):
    assert input_val % 2 == 0
 
    
# pytest -k div -v 

    
    