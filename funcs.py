# functions
from decimal import Decimal, getcontext

getcontext() # understand what this does


# Change Operate function to loop repeatedly the statement while following PEMDAS
# Goal is to compute this example: 2*(20-(12/4 - 3 + 1))^2 - 3

def get_list(statement):

    slist = list(statement.replace(" ", ""))
    ind = 0
    while ind < len(slist):
        if slist[ind] == '-':
            if ind == 0 or slist[ind-1] in valid_ops:
                slist[ind] = slist[ind] + slist[ind+1]
                slist.pop(ind+1)
        if slist[ind].lstrip('-').isdecimal() and slist[ind+1].isdecimal():
            slist[ind] = slist[ind] + slist[ind+1]
            slist.pop(ind+1)
        ind += 1
    return slist
    
# Lets try a recursive function
# newOperate(list) will recursively call on the list where list will represent the statemen where all the order
# of operations do not matter for example: if the statement has only add/sub or multi/div
# Base Case:
#   Run through the two list elements and return the result
                
# statement will look like this : ['24','+','-5','^','(','4','^','2',')'] = 24 + -5 * (4^2)
                

def newOperate(statement: list):

    # Base Case
    if len(statement) <= 3: # makes sure the subset is only two numbers and three elements
        val_1 = statement[0]
        operation = statement[1]
        val_2 = statement[2]
        return valid_ops[operation](val_1,val_2) # Returns the result of singular operation
    
    # Not Base Case
    for operator in precedence:
        start = -1
        end = -1
        ind = 0
        while(ind < len(statement)):
            # special case: parameters
            if operator == '()':
                if statement[ind] == '(':
                    start = ind
                if statement[ind] == ')':
                    end = ind
                    result = newOperate(statement[start + 1:end]) # returns completed operation for that substatement
                    statement[ind] = result
                    # remove elements until end
                    statement = statement[:start] + statement[ind:]
                    ind = end - start
                ind += 1
            else:
                if statement[ind] == operator:
                    start = ind - 1
                    end = ind + 1
                    statement[ind] = newOperate(statement[start:end+1])
                    print(statement[ind])
                    # Original length of statement is for example 9 and op is at ind 4 then 0:3 + ind...0 1 2 3 4 6 8
                    statement = statement[:start] + statement[ind:ind+1] + statement[end+1:] # what happens if start = 0
                    ind-=1 # readjusts index so that ind is at result new location
                ind += 1
    return statement
    
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

precedence = [
    '()',
    '^',
    '%',
    '*',
    '/',
    '+',
    '-'
]

def calculate(equation: str):

    listOfElems = get_list(equation)
    Result = newOperate(listOfElems) 
    return Result[0]

    # use the rules of pemdas to get the proper code
