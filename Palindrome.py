num=int(input("enter the number"))
temp = num
rev = 0

while temp > 0:
    digit = temp %10
    rev =rev*10+digit
    temp=temp // 10

if num == rev:
    print("palindrome number")
else:
    print("not a palindrome")
