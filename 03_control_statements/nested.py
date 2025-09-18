# nested conditionals : Conditionals inside conditionals
# Dynamic Voting app
age = int(input("Enter the Age "))

if age >= 18:
    has_id = input("Do you have id (yes/no): ")
    if has_id == "yes":
        print("You can vote")
    else:
        print("You need an ID to vote")
else: 
    print("You are too young to vote")