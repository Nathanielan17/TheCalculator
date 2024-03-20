# testing functions in funcs.py

from funcs import *

def test_get_list():
    test_string = "5.3 + .23"
    result = get_list(test_string)
    correctResult = ['5.3','+','.23']
    print(result)
    assert result == correctResult
    return result

def test_operate():
    test_list = test_get_list()
    result = newOperate(test_list)
    print(result)
    correctResult = '5.53'
    assert result == correctResult    
    