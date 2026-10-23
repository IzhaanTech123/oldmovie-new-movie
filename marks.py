m1=float(input("enter the marks of first subject:"))
m2=float(input("enter the marks of second subject:"))
m3=float(input("enter the marks of third subject:"))

total=m1+m2+m3
average=total/3
percentage=(total/300)*100

print("the total marks is:",total)
print("the average marks is :",average)
print("percentage = {:.2f}%".format(percentage))