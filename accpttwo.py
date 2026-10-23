def calculate(choice):
    a=float(input("Enter first number: "))
    b=float(input("Enter second number: "))
    if choice == 1:
        print("addition",a+b)
    elif choice == 2:
        print("subtraction",a-b)
    elif choice == 3:
        print("multiplication",a*b)
    elif choice == 4:
        if b!=0:
            print("Division",a/b)
        else:
          print("division by zero is not possible.")
    else:
        print("invalid input!")

print("***MENU***")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

ch=int(input("enter the choice:"))
calculate(ch)
