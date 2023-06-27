'''#EX-2
class Calculator:
    def calculate(self,a,b):
        print("Calculating result")
class add:    
    def calculate(self,a,b):
        print(a+b)
class sub:         
    def calculate(self,a,b):
        print(a-b)
class mul:         
    def calculate(self,a,b):
        print(a*b)
class div:         
    def calculate(self,a,b):
        print(a/b)
#class div(Calculator):
 #   pass
def result(ref,a,b):
    ref.calculate(a,b)

result(add(),20,10)#30
result(sub(),20,10)#10
result(mul(),20,10)#200
result(div(),20,10)#2.0'''


#EX-3
#SPECIAL VARIBLE __name__
class Calculator:
    def calculate(self):
        print("Calculating result")
class Add:    
    def calculate(self,a,b):
        print(a+b)
class Sub:         
    def calculate(self,a,b):
        print(a-b)
class Mul:         
    def calculate(self,a,b):
        print(a*b)
class Div:
    pass

def result(ref,a,b):
    if type(ref).__name__=="Div":
        print("Div class doesnt have calculate()")
    else:    
        ref.calculate(a,b)

result(Add(),20,10)#30
result(Sub(),20,10)#10
result(Mul(),20,10)#200
result(Div(),20,10)#2.0






