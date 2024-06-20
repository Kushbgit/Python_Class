#to create 'X'
# f = open("newt2.txt", 'x')
# print("file created")
# print(f.mode)
# print(f.closed)
# f.closed()
# print(f.closed)
# --------------------------
#to wrtie 'w'
# f = open("newt2.txt", 'w')
# f= open("newt2.txt", 'a')
# f.write("there is nothing more than MUSIC\n")
# data = ('My name is kushagra bule\n', 'I live in Bhopal\n','I am 3d Animator\n')
# f.writelines(data)
# print(f.writable())
# --------------------------
#to read 'r'
# f= open('newt2.txt', 'r')
# print(f.mode)
# #data=f.read(10)
# #data= f.readline()
# data= f.readlines()
# print(data)
# f.close()
# --------------------------
#to append 'a'
# f= open('newt2.txt', 'a')
# print(f.mode)
# f.write("This is python class")

#f= open('newt2.txt', 'r')
# data= f.readlines()
# print(data)
#---------------------------------
# using tell() to know the operation 
#f= open('newt2.txt', 'r')
#print(f.tell())
#print(f.read(3))
#print(f.tell())
#print(f.readline())
#print(f.tell())
#print(f.read())
#print(f.tell())
#print(f.read(5))
#-----------------------------------
#using seek() for the position of cursor
# f= open('newt2.txt', 'r')
# print(f.tell())
# print(f.read(3))
# print(f.seek(0))
# print(f.read(10))
# print(f.tell())
# print(f.seek(15))
# print(f.tell())
#-------------------------------
#converting in binary using 'b'
# f= open('newt2.txt', 'rb')
# print(f.tell())
# # print(f.seek(-10,2))
# # print(f.tell())
# # print(f.read(10))       
# print(f.seek(10,0))
# print(f.tell())
# print(f.read(10))
#--------------------------------
#to close(incase you forget to close file)
with open('newt2.txt', 'rb') as f:
    print(f.read(10))
    print(f.tell())
    print(f.seek(10,1))
    print(f.tell())
    print(f.closed)
print(f.closed)