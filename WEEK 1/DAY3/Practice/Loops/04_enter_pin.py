# Program to repeatedly ask the user to enter the correct PIN.
correct_pin=1591
enter_pin=int(input("Enter your Pin: "))
while enter_pin != correct_pin:
    print("wrong pin , Please enter Valid Pin")
    enter_pin=int(input(" Enter Pin: "))
    
print("Welcome")
   