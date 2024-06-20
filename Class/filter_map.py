#using map
# my_list=[5,10,15,20,25]
# def num(x):
#     if x%2==0:
#         return 'even'
#     else:
#         return 'odd'
# x=list(map(num,my_list))
# print(x)
#---------------------------------
#using Filter
# my_list=[10,15,20,25,30,35]
# def greater(x):
#     if x>=20:
#         return True
# x=filter(greater,my_list)
# print(list(x))
#------------------------------
my_list=[5,10,15,20,25]
def num(x):
    if x % 2 ==0:
        return 'even'
x=list(filter(num,my_list))
print(x)
