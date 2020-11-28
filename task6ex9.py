print("Calculator")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
ch=int(input("enter your choice:"))
a=int(input("Enter value of a:"))
b=int(input("Enter value of b:"))
if ch==1:
    c=a+b
    print("sum is:",c)
elif ch==2:
    c=a-b
    print("sub is:",c)
elif ch==3:
    c=a*b
    print("mul is:",c)
elif ch==4:
    c=a//b
    print("div is:",c)
else:
    print("Invalid option")