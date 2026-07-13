# program for calculator using function

def add(a,b):
    return (a+b)
def substract(a,b):
    return (a-b)
def multiply(a,b):
    return(a*b)
def divide(a,b):
    return(a/b)

num1=float(input("Enter the number 1: "))
num2=float(input("Enter the number 2: "))

print("Available Operations:")
print("+ Addition")
print("- Subtraction")
print("* Multiplication")
print("/ Division")

operation=input("Enter the Operation: ")

if operation =="+":
    result=add(num1,num2)
    print("Addition=",result)
elif operation=="-":
    result=substract(num1,num2)
    print("Substraction=",result)  
elif operation=="*":
    result=multiply(num1,num2)
    print("Multiplication=", result)
elif operation=="/":
    result=divide(num1,num2)
    print("Division=", result)
else:
    print("Invalid Operator")
    print("TRY AGAIN")

print("THANK YOU, Visit Again!")