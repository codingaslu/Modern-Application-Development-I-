class Testclass1: #class name should be start with TEST
    def testtest1(): #test is mandatory after that any substring
        x=3
        y=10
        assert x == y
        
    def testtest2():
        num=10
        assert 10+10==20

class Testclass2:     
    def test_test1():
        num1=10
        assert 10*10 == 90
    
    def test_method2():
    assert false