#manual way to create decorater .... 
def greet():
    print("Hello")

def wrapper(fun):
    def inner():
        print("Before")

        fun()

        print("After")
    return inner

greet = wrapper(greet)

greet()