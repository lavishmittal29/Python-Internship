# Program to check the customer is eligible for discount or not.
purchase_amount=int(input("Enter the purchase amount: "))
if purchase_amount>=5000:
    print("Discount Applied.")
else:
    print("No Discount.")