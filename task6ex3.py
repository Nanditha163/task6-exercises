def fibon(n):
    if n<=1:
        return n
    else:
        return(fibon(n-1)+fibon(n-2))
value=int(input("Enter the no.of terms:"))
if(value>0):
    print("Fibonacci sequence is:")
    for i in range(value):
        print(fibon(i))
else:
    print("Enter a positive value,Thank you!")

    OUTPUT:
        Enter the no.of terms:8
        Fibonacci sequence is:
        0
        1
        1
        2
        3
        5
        8
        13
