from State import State
class Number2(State):
    def __init__(self,calculator):
        self.calculator = calculator
    def enternum(self,a):
        self.calculator.n2 += a
        print(self.calculator.n2)
    def enteroperation(self,operation):
        self.calculator.count()
        self.calculator.n1 = self.calculator.result
        self.calculator.result = ''
        self.calculator.setstate(self.calculator.operationstate)
        self.calculator.enteroperation(operation)
    def entereq(self):
        self.calculator.setstate(self.calculator.resultstate)
        self.calculator.entereq()