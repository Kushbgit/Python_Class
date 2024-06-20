# x= lambda name: print ("Hello", name)
# x=("Kushagra")
# x=lambda x,y: x+y
# print(x(10,20))
#--------------------------------------

# x= lambda name: print ("Hello", name)
# y=input("Enter Name :")
# x(y)
# x=lambda x,y: x+y
# p=int(input("Enter Number :"))
# q=int(input("Enter Number :"))
# print(x(p,q))
#---------------------------------------
# my_list=[2,4,6,8,10]
# x=list(map(lambda x:x**2, my_list))
# print(x)
#---------------------------------------
my_list=[1,2,3,4,5,6,7,8,9,10]
#x=list(filter(lambda x:x%2==0, my_list)) #even
x=list(filter(lambda x:x%2!=0, my_list))  #Odd
print(x)
