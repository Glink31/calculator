from State import State
class Operation(State):
    def __init__(self,calculator):
        self.calculator = calculator
    def enternum(self,a):
        self.calculator.n2 = ''
        self.calculator.setstate(self.calculator.n2state)
        self.calculator.enternum(a)
    def enteroperation(self,operation):
        self.calculator.operation = operation
        print(self.calculator.n1)
    def entereq(self):
        self.calculator.n2 = ''
        self.calculator.setstate(self.calculator.resultstate)
        self.calculator.n2 = self.calculator.n1
        self.calculator.count()
        print(self.calculator.result)