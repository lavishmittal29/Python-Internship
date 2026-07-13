#SIMPLE INTEREST CALCULATION
Principle=float(input('Enter the principle amount: '))
rate=float(input('Enter the rate of interest: '))
time=float(input('Enter the time period: '))
SI=(Principle*rate*time)/100
print("The simple interest is:",SI)
amount=Principle+SI
print("The total amount is:",amount)