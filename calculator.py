class Calculator():
    def __init__(self):
        self.state = None
        self.n1 = ''
        self.n2 = ''
        self.operation = None
        self.result = None
        self.n1state = None
        self.n2state = None
        self.operationstate = None
        self.resultstate = None
    def setn1state(self,state):
        self.n1state = state
    def setn2state(self,state):
        self.n2state = state
    def setoperationstate(self,state):
        self.operationstate = state
    def setresultstate(self,state):
        self.resultstate = state
    def setstate(self,state):
        self.state = state
    def enternum(self,a):
        self.state.enternum(a)
    def enteroperation(self,operation):
        self.state.enteroperation(operation)
    def entereq(self):
        self.state.entereq()
    def count(self):
        if self.operation == '+':
            self.result = int(self.n1) + int(self.n2)
        elif self.operation == '-':
            self.result = int(self.n1) - int(self.n2)
        elif self.operation == '*':
            self.result = int(self.n1) * int(self.n2)
        elif self.operation == '/':
            self.result = int(self.n1) // int(self.n2)