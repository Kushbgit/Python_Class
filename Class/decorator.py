#  Decorator-it is a function which takes a fucntion as an argument and also return the function is known as Decorator.
def decorator(x):
    def wrapper():
        print("Start Work")
        x()
        print("Stop Work")
    return wrapper
@decorator       #-------->Company's Format
def original_fun():
    print("This is Original Function")

# var=decorator(original_fun)
# var()
original_fun()   #-------->Company's Format