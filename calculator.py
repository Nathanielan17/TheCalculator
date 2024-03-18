from funcs import calculate

class Calculator:

    def __init__(self):
        self.expr = "" # Expression string
        self.Result = '' # Result of current expr
        self.log = [] # log of inputs
        self.prevResult = None  # Previous result

    # check_expression makes sure expression entered is valid before calculating
    def check_expression(self):
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
        self.log.append(self.expr)
        self.Result = calculate(self.expr) # gets result based on expression
        self.prevResult = self.Result
        return self.Result

