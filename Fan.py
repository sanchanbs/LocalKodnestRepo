
class Fan:
 def __init__(self):
      self.brand="Usha"
      self.color="Red"
      self.price=5000
 def Start(self):
     print("Fan Started rotating")
 def Stop(self):
     print("Fan Stopped rotating")
f1=Fan()
print(f1.brand)
print(f1.color)
print(f1.price)
f1.Start()
f1.Stop()

print("===================================")

class Employee:
 def __init__(self):
        self.name="Sanchan"
        self.id=23
        self.salary=35000
 def work(self):
     print("Employee is working")
 def eat(self):
     print("Employee is eating")
e1=Employee()
print(e1.name)
print(e1.id)
print(e1.salary)
e1.work()
e1.eat()


print("===================================")


class Employee:
 def __init__(self,name,id1,salary):
     self.name=name
     self.id1=id1
     self.salary=salary
 def work(self):
     print(self.name+" is working")
 def eat(self):
     print(self.name+" is eating")
e1=Employee("Akash",22,26000)
e2=Employee("Prabhas",23,45000)
e1.work()#Aksah is working
e2.work()#Prabhas is working
print(e1.name)#Akash
print(e2.name)#Prabhas
print(e1.id1)
print(e1.salary)
print(e2.id1)
print(e2.salary)

     
        



         

