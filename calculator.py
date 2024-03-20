from funcs import calculate, get_list, valid_ops

class Calculator:

    def __init__(self):
        self.expr = "" # Expression string
        self.Result = '' # Result of current expr
        self.log = [] # log of inputs
        self.prevResult = None  # Previous result

    # check_expression makes sure expression entered is valid before calculating
    def check_expression(self):
        s = get_list(self.expr)
        for elem in s:
            if not (elem.isdecimal() or elem in valid_ops or elem == '(' or elem == ')'):
                return False
        return True
        ...


    # clear() clears the calculator log, expr, result, prevResult 
    # and sets up the calculator for the next input
    def clear(self):
        self.log = [] # clears log 
        self.Result = ''
        self.prevResult = ''
        self.expr = ''
    
    def clear_Entry(self):
        self.expr = ''

    def get_Result(self):
        if not self.check_expression():
            return 'ERR'
        self.log.append(self.expr)
        self.Result = calculate(self.expr) # gets result based on expression
        self.prevResult = self.Result
        return self.Result

