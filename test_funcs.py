# testing functions in funcs.py

from funcs import *

def test_get_list():
    test_string = "(100-20)*10-35+10"
    result = get_list(test_string)
    correctResult = ['(','100','-','20',')','*','10','-','35','+','10']
    assert result == correctResult
    return result

def test_operate():
    test_list = test_get_list()
    result = newOperate(test_list)
    print(result)
    correctResult = '775'
    assert result == correctResult    
    