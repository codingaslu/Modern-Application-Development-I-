""" 
the below code is using marker method

import pytest 

@pytest.mark.marker1
def test_1():
    x = "this"
    assert "h" in x

@pytest.mark.method2    
def test_2():
    y = "hello"
    assert "a" in y
    
    """