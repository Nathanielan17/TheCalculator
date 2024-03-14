# testing functions in funcs.py
import pytest
from funcs import *

def test_get_list():
    test_string = "-25 * 5 - (4 ^ -2)"
    result = get_list(test_string)
    correctResult = ['-25','*','5','-','(','4','^','-2',')']
    assert result == correctResult
    return result

def test_operate():
    test_list = test_get_list()
    result = newOperate(test_list)
    print(result)
    correctResult = ['-125.0625']
    assert result == correctResult    
    