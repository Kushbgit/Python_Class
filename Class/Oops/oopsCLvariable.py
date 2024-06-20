#Varialbes 
#Intance Variable ,Local Variable, Static Variable
class Student:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def detail(self):
        print(self.name)
        print(self.age)   

obj1=Student("Kush",24)
obj1.detail()
# print(obj1.__doc__)
# print(obj1.__dict__)

obj2=Student("Vedant",24)
obj2.detail()
# print(obj2.__doc__)
# print(obj2.__dict__)