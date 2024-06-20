#Local Variable
#def add (x):
#    y=10
#    sum=x+y
#    print(sum)
#    print(y)
#
#Global Variable
#y=10
#def add (x):
#    sum=x+y
#    print(sum)
#add(10)

#cross variable
#y=20
#def add (x):
#    y=10
#    sum=x+y
#    print(sum)
#add(10)

#Calling Global variable in local
#y=30
#def add (x):
#    y=10
#    sum=x+globals()['y']
#    print(sum)
#add(10)
#print(y)

#calling local variable to global
#def add (x):
#    global y
#    y=10
#    sum=x+ y
#    print(sum)
#add(10)
#print(y)

#
y=20
def add (x):
    global y
    y=10
    sum =x+y
    print(sum)
y=30
add(10)
print(y)
