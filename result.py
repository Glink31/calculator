from State import State
class Result(State):
    def __init__(self,calculator):
        self.calculator = calculator
    def enternum(self,a):
        self.calculator.result = ''
        self.calculator.n1 = ''
        self.calculator.setstate(self.calculator.n1state)
        self.calculator.enternum(a)
    def enteroperation(self,operation):
        self.calculator.n1 = self.calculator.result
        self.calculator.result = ''
        self.calculator.setstate(self.calculator.operationstate)
        self.calculator.enteroperation(operation)
    def entereq(self):
        self.calculator.count()
        print(self.calculator.result)