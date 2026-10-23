ch=input("enter a character:")

if len(ch)==1:
    print("please enter only one character")
elif ch.isdigit():
    print("it is digit")
elif ch.isalpha():
    if ch.lower() in "a e i o u":
        print("it is vowel")
    else:
        print("it is consonant")
else:
    print("it is special character")