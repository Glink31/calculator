from calculator import Calculator
from firstnumber import Number1
from secondnumber import Number2
from operation import Operation
from result import Result
Calc = Calculator()
st1 = Number1(Calc)
st2 = Number2(Calc)
st3 = Operation(Calc)
st4 = Result(Calc)
Calc.setn1state(st1)
Calc.setn2state(st2)
Calc.setoperationstate(st3)
Calc.setresultstate(st4)
Calc.setstate(Calc.n1state)
a = input('> ')
while a in ['1','2','3','4','5','6','7','8','9','0','+','-','*','/','=']:
    if a in ['1','2','3','4','5','6','7','8','9','0']:
        Calc.enternum(a)
    elif a in ['+','-','*','/']:
        Calc.enteroperation(a)
    elif a == '=':
        Calc.entereq()
    a = input('> ')