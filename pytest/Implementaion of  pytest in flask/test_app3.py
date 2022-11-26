import requests

response = requests.get('http://127.0.0.1:5000/abc')

def test_t1():
    assert response.text == "Hello,World!"
    
def test_t2():
    assert response.status_code == 404
    
def test_t3():
    assert response.status_code == 404
    
def test_t4():
    assert response.status_code == 404    
    
def test_t5():
    assert response.status_code == 404