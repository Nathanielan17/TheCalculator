# functions
from decimal import Decimal, getcontext

getcontext()

def Operate(statement):
    slist = list(statement)
    ans = "Error"
    for i in range(len(slist)):
        if slist[i] in valid_ops:
            num1 = "".join(slist[0:i])
            num2 = "".join(slist[i+1:len(slist)])
            try:
                ans = valid_ops[slist[i]](num1,num2)
            except ValueError:
                return "Invalid statement was made, please enter a proper statement"
            break
    return ans

def add(a,b):
    return str(Decimal(a) + Decimal(b))

def subtract(a,b):
    return str(Decimal(a) - Decimal(b))

def multiply(a,b):
    return str(Decimal(a) * Decimal(b))

def division(a,b):
    return str(Decimal(a)/Decimal(b))

def power(a,b):
    return str(Decimal(a)**Decimal(b))

def moduli(a,b):
    return str(Decimal(a) % Decimal(b))

valid_ops = {
    '+': add,
    '-': subtract,
    '/': division,
    '*': multiply,
    '^': power,
    '%': moduli
}