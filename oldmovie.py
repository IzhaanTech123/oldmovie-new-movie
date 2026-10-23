member = input("Are you a member? (yes/no): ").lower()
movie = input("Enter movie type (old/new): ").lower()
days = int(input("Enter number of days: "))

if member == "yes":
    if movie == "old":
        bill = days * 10
    elif movie == "new":
        bill = days * 20
    else:
        bill = -1
elif member == "no":
    if movie == "old":
        bill = days * 20
    elif movie == "new":
        bill = days * 30
    else:
        bill = -1
else:
    bill = -1

if bill >= 0 and days > 0:
    print("Total video library bill = ₹", bill)
else:
    print("Invalid input")