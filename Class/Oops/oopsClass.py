#without Constructor

class Student:
    Stu_qualification="B.COM"
    def Student_detail(name, age):
         print("Student Name=", name)
         print("Student Age=",age)
         print("Student Qualification=", Student.Stu_qualification)         
obj=Student
obj.Student_detail("Kushagra",24)
#print(dir(Student))

# #with Constructor

# class Student:
#      Stu_qualification="Bcom"
#      def __init__(self):
#           print("Constructor Called")
# obj=Student() 
# print(obj)          
        