# testing functions in funcs.py
import pytest
from funcs import *

def test_get_list():
    test_string = "1 - 7^2 + 40 "
    result = get_list(test_string)
    correctResult = ['1','-','7','^','2','+','40']
    assert result == correctResult
    return result

def test_operate():
    test_list = test_get_list()
    result = newOperate(test_list)
    print(result)
    correctResult = '-8'
    assert result == correctResult    
    