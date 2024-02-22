# functions
from decimal import Decimal, getcontext

getcontext()

def Operate(statement):

    temp = list(statement.replace(" ", "")) # Returns a list ex: ['2','+','3','-','4']
    ind = 0
    numberQueue = []
    opQueue = []
    numToAdd = ""
    start = 0

    if not temp[ind].isdigit(): #or not (temp[ind] != '-' and temp[ind+1].isnumeric()):
        return "Error improper statement"
    else:
        if temp[ind] == "-" and not temp[ind+1].isdigit():
            return "Error improper statement"
        else:
            if temp[ind] in valid_ops:
                return "Error improper statement"

    while ind < len(temp):
        if temp[ind] in valid_ops and not (temp[ind-1] in valid_ops):
                num = "".join(temp[start:ind])
                print(num)
                start = ind + 1
                numberQueue.append(num)
                opQueue.append(temp[ind])
        if temp[ind] in "-" and temp[ind-1] in valid_ops:
            start = ind
        ind += 1
    num = "".join(temp[start:ind])
    numberQueue.append(num)
    return numberQueue, opQueue

    # slist = rmSpace(list(statement))
    # if not slist[0].isnumeric(): return "Error"
    # nums = []
    # ops = []
    # prev = 0
    # print(slist)
    # for i in range(len(slist)): # 2+-4-5+-2 
    #     if slist[i] in valid_ops:
    #         if slist[i] == "-" and slist[i-1] in valid_ops:
    #             continue
    #         nums.append("".join(slist[prev:i]))
    #         ops.insert(0,slist[i])
    #         prev = i+1
    # # nums is the list of numbers (as strings) and ops is the queue of operations
    # num1 = None
    # num2 = None
    # ans = None
    # print(nums)
    # print(ops)
    # for i in range(len(nums)): # 2+3+4+5
    #     if num1 == None:
    #         num1 = nums[i]
    #         continue
    #     if num2 == None:
    #         num2 = nums[i]
    #         continue
    #     op = ops.pop()
    #     if ans == None:
    #         ans = valid_ops[op](num1,num2)
    #     val = nums[i]
    #     ans = valid_ops[op](str(ans),val)
    # return ans
        
         
    



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