
class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
        print("Bank Account Created")

    def show_details(self):
        print("Name:",self.name)
        print("Balance:",self.balance)

    def deposit(self,amount):
        self.balance=self.balance+amount
        print("Amount Credited Successfully.")

    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance=self.balance-amount
            print("Withdrawal Successful..")
        else :
            print("Insufficient Balance")

    def check_balance(self):
        print("Current Balance:",self.balance)
        
            
    
account1=BankAccount("Lavish",10000)
account2=BankAccount("Rahul",5000)
account3=BankAccount("Jayesh",7000)


account1.show_details()
account1.deposit(5000)
account1.check_balance()
account1.withdraw(6000)
account1.check_balance()