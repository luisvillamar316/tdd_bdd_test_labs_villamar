import pytest

class Calculator:
    def __init__(self,name):
        self.name = name

    def add(self, a, b):
        return a + b
    
    def subtract(self,a,b):
        return a - b
    
    def multiply(self,a,b):
        return a * b
        
calc = Calculator("Base Calculator")        
        
@pytest.fixture
def base_calculator():
    return Calculator("Base Calculator")
    
def test_lab4_test1(base_calculator):
    print("#1 This calculator's name is " + base_calculator.name)
    
    #Changing calculator's name
    base_calculator.name = 'Changed Calculator'
    print("#1 This calculator's name is " + base_calculator.name)
    
    assert True

def test_lab4_test2(base_calculator):
    print("#2 This calculator's name is " + base_calculator.name)
    
    assert True

def test_subtract():
    assert calc.subtract(2,1)  == 1

def test_multiply():
    assert calc.multiply(2,6) == 12