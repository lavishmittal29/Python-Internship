

#program  

passwords = ("python123")
attempt=3
while True:
    entered_passwords=input("Enter your passwords: ")
    if passwords == entered_passwords:
        print("Access Granted")
        break
    else:
        attempt=attempt-1
        print("wrong password")
        print("attemp left:", attempt)
        if attempt==0:
            print("Account locked")
            break   
