#Method Resolution Method-> Depth first {Left to right}

# class Parent1:
#     def m1(self):
#         print("Parent1 Method called")
# class Parent2:
#     def m2(self):
#         print("Parent2 Method called")
# class child(Parent1, Parent2):
#     def m3(self):
#         self.m1()
#         self.m2()
# obj=child()
# obj.m3 ()       

class A:
    def m1(self):
        print("M1 called from A")
class B(A):
    def m1(self):
        print("M1 called from B")
        super().m1()  #to use access parent class we use super() method
obj=B()
obj.m1()                