num=int(input("Enter an number:"))
sum=0
temp=num
while temp > 0:
    digit=temp%10
    sum+=digit**3
    temp//=10
if num==sum:
      print(num,"It is an armstrong number!")
else:
      print(num,"It is not an armstrong number")
        
        
        OUTPUT:
       1.   Enter an number:153
            153 It is an armstrong number!
            
            
       2.   Enter an number:120
            120 It is not an armstrong number

