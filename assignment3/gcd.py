'''
Assignment 3.7
==============
PROGRAM   :To find gcd of two numbers using user defind functon findGCD
FILE NAME :gcd.py
CREATED BY:Subhashis Patbandha
DATED     :30/09/2020
'''
def findGCD(num1,num2):

    while(num1!=num2):
        if(num1>num2):
            num1-=num2
        else:
            num2-=num1
    return num1      

n1=int(input("Enter 1st number : "))
n2=int(input("Enetr 2nd number : "))
temp1=n1
temp2=n2
gcd=findGCD(n1,n2)
print("GCD of ",n1," and",n2," = ",gcd)

