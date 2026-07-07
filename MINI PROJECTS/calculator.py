# Program which act like a calculator and perform basic operations like addition, subtraction, multiplication, division, exponentiation and modulus.
print("-------------------------")
print("    Python Calculator    ")
print("-------------------------")
#USER INPUT
number1=float(input('Enter the First number :'))
number2=float(input('Enter the Second number :'))
#OPERATION CHOICE
print("Available Operations:")
print("+ Addition")
print("- Subtraction")
print("* Multiplication")
print("/ Division")
print("** Exponentiation")
print("% Modulus")
# OPERATION SELECTION
choice= input('Enter the operation: ')
#ADITION
if (choice=='+'):
    print("Addition Selected")
    result=number1+number2
    print("-------------------------")
    print(   f"Result = {result}"    )
    print("-------------------------")
#Subtraction
elif (choice=='-'):
    print("Subtraction Selected")
    result=number1-number2
    print("-------------------------")
    print(   f"Result = {result}"    )
    print("-------------------------")
#MULTIPLICATION
elif(choice=='*'):
    print("Multiplication Selected")
    result=number1*number2
    print("-------------------------")
    print(   f"Result = {result}"    )
    print("-------------------------")
#DIVISION
elif(choice=='/'):
    print("Division Selected")
    result=number1/number2
    print("-------------------------")
    print(   f"Result = {result}"    )
    print("-------------------------")
#EXPONENTIATION
elif(choice=='**'):
    print("Exponentiation Selected")
    result=number1**number2
    print("-------------------------")
    print(   f"Result = {result}"    )
    print("-------------------------")
#MODULUS
elif(choice=='%'):
    print("Modulus Selected")
    result=number1%number2
    print("-------------------------")
    print(   f"Result = {result}"    )
    print("-------------------------")
#INVALID CHOICE
else:
    print("Invalid choice. Please enter valid operation.")
