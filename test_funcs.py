# testing functions in funcs.py
import pytest
from funcs import *

def test_Operate_numList():
    test_string = "25 + 3  -   4"
    numQ = Operate(test_string)[0]
    if numQ is str:
        print("Function is reading improper input")
    numCheck = ["25","3","4"]
    print(numQ)
    assert numQ == numCheck

def test_Operate_opList():
    test_string = "-25 + 3  -   4"
    opQ = Operate(test_string)[1]
    opCheck = ["+","-"]
    print(opQ)
    assert opQ == opCheck


    
    