        #Inheritence
#There are three type of Inheritence
#Single Level :- {Parents->Child}
#Multi Level :-{GrandFather->Father->son}
#Multiple:- {Father/Mother ->Son} 

#single Level---Multiple Level
class A:
    name="Kushagra"
    def m1(self):
        return"This is Inheritence"
class B(A):
    age='14'
    def m2(self):
        print("Name: ", A.name)

class C(B):
    
    def m3(self):
        self.m2()
        print("Age:",B.age)
        print("M1:", self.m1())
        
obj=C()
obj.m3()                