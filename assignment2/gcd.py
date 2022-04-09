# PROGRAM: To find the GCD of any two integer and print the result slong with input value
# FILE: gcd.py
# CREATED BY: Subhashis Patbandha
# DATED: 23-09-20

a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number : "))
temp1=a
temp2=b

while(a!=b):
    if a>=b:
        a=a-b
    else:
        b=b-a
    

print("The GCD of ",temp1," and ",temp2," = ",a)