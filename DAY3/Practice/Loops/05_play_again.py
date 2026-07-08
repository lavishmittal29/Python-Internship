# Program to ask the user whether they want to continue or not.

response = input("Do you want to continue? (yes/no): ")

while response == "yes":
    print("Continuing...")
    response = input("Do you want to continue? (yes/no): ")

print("Goodbye!")