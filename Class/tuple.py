my_tuple=(10,20,30,40,50,60)
#print(len(my_tuple))
#print(max(my_tuple))
#print(min(my_tuple))
#print(sum(my_tuple))
#print(id(my_tuple))
#print(type(my_tuple))

#---INDEXINGG----

#print(my_tuple.index(50))
#print(my_tuple[0])
#print(my_tuple[1])

#---Negative INDEXINGG----
#print(my_tuple[-1])

#---Slicing---
#print(my_tuple[1:3])

#---Count----
#print(my_tuple.count(10))

#converting tuple to list then list to tuple
x= list(my_tuple)
print(type(x))
x[0]=20

#then list to tuple
y=tuple(x)
print(type(y))
print(y)