#Static Method
class Student:
    @staticmethod
    def greet():
        print("Thanks for Visiting")

    def greet1(self):
        print("Welcome to my Webpage")
#obj=Student
obj=Student() #-->c
obj.greet()
Student.greet()
# obj.Student() 
# Student.greet1() 
obj.greet1()