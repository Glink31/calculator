from State import State
class Number1(State):
    def __init__(self,calculator):
        self.calculator = calculator
        self.operation = None
    def enternum(self,a):
        self.calculator.n1 += a
        print(self.calculator.n1)
    def enteroperation(self,operation):
        self.calculator.setstate(self.calculator.operationstate)
        self.calculator.enteroperation(operation)
    def entereq(self):
        self.calculator.setstate(self.calculator.resultstate)
        self.calculator.entereq()

        
        
        

    
   
