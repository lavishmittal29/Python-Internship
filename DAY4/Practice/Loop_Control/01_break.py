

#program 
passwords = ("python123")

while True:
    entered_passwords=input("Enter your passwords: ")
    if passwords == entered_passwords:
        print("Access Granted")
        break
    else:
        print("wrong")    
