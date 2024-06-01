def compute_gcd(X,Y):
   if X > Y:
     smaller= Y
     print(f"The smaller number is :{smaller}")
   else:
       smaller= X
       print(f"The smaller number is:{smaller}")


   for i in range(1, smaller+1):
         
         if (X% i==0) and (Y% i==0):
             gcd =i
             print(f"The current GCD candidate is: {gcd}")    

   return gcd

num1 = int(input("Enter The first number: "))
num2 = int(input("Enter The second number:"))

result = compute_gcd(num1,num2)
print(f"The GCD of {num1}and {num2}is {result}")
