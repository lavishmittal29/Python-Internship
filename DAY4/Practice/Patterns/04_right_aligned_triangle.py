#program to print right aligned triangle with star.
for i in range(5):
    for j in range(4-i):
        print(" ",end=" ")
    for j in range(i+1):
        print("* ",end="")    
    print()    