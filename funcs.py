# functions
from decimal import Decimal, getcontext

getcontext()

def Operate(statement):

    temp = list(statement.replace(" ", "")) # Returns a list ex: ['2','+','3','-','4']
    ind = 0
    numberQueue = []
    opQueue = []
    start = 0
    invalidArgs = "Error improper statement"

    if not temp[ind].isdigit(): #or not (temp[ind] != '-' and temp[ind+1].isnumeric()):
        if temp[ind] == "-":
            if not temp[ind+1].isdigit():
                return invalidArgs
        else:
            return invalidArgs
        

    while ind < len(temp):
        if temp[ind] in valid_ops and not (temp[ind-1] in valid_ops): # checks if current is a op and previous is not an op
            if ind != 0:
                num = "".join(temp[start:ind]) # gets number before this current op
                print(num)
                start = ind + 1 # sets new start index at the index after this current op
                numberQueue.append(num) # adds previous number into queue
                opQueue.append(temp[ind]) # adds this current operation into queue
        if temp[ind] in "-" and (temp[ind-1] in valid_ops or ind==0):
            start = ind
        ind += 1
    num = "".join(temp[start:ind])
    numberQueue.append(num)
    return numberQueue, opQueue

    # So now numberQueue is a list of numbers that are within the inputted statement. opQueue is also a list
    # with the operations in the statement. Both lists are Queues in where the first number/operation is first.
    # FIFO
    # This will added with creating a stack to follow PEMDAS.

    



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