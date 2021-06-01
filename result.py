from State import State
class Result(State):
    def __init__(self,calculator):
        self.calculator = calculator
    def enternum(self,a):
        self.calculator.result = ''
        self.calculator.setstate(self.calculator.n1state)
        self.calculator.enternum(a)
    def enteroperation(self,operation):
        self.calculator.n1 = self.calculator.result
        self.calculator.result = ''
        self.calculator.setstate(self.calculator.operationstate)
        self.calculator.enteroperation(operation)
    def entereq(self):
        if self.calculator.n1 == '':
            self.calculator.result = '0'
        elif self.calculator.n1 != '' and self.calculator.n2 == '':
            if self.calculator.operation == '':
                self.calculator.result = self.calculator.n1
            else:
                self.calculator.n2 = self.calculator.n1
                self.calculator.count()
        elif self.calculator.n1 != '' and self.calculator.n2 != '':
            self.calculator.count()
        print(self.calculator.result)