from State import State
class Number1(State):
    def __init__(self,calculator):
        self.calculator = calculator
    def enternum(self,a):
        self.calculator.n1 += a
        print(self.calculator.n1)
    def enteroperation(self,operation):
        self.calculator.setstate(self.calculator.operationstate)
        self.calculator.enteroperation(operation)
    def entereq(self):
        self.calculator.setstate(self.calculator.resultstate)
        if self.calculator.n1 == '':
            self.calculator.result = '0'
        else:
            self.calculator.result = self.calculator.n1
        print(self.calculator.result)

        
        
        

    
   
