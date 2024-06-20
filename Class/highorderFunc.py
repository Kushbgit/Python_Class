#to add 5 to each element
# x=my_list = [10, 20, 30, 40, 50]
# y=[]
# for i in my_list:
#     x=i+5
#     y.append(x)
# print(y) 

#to add each element by 5 using map()
# my_list = [10, 20, 30, 40, 50]
# def add(n):
#     return n+5
# x=map(add,my_list)
# print(x)
# print(list(x))

#to sqaure each element by 5 using map()
# my_list = [10, 20, 30, 40, 50]
# def add(n):
#     return n*5
# x=map(add,my_list)
# print(x)
# print(list(x))

#asking user to enter their name and return ASCII value
n=input("Enter your name :")
def add(n):
    n=ord(n)
    y=n+5
    return chr(y)
y=map(add,n)
print((n))
#---------------------------------------------

