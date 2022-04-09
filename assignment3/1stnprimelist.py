'''
Assignment 3.2
==============
PROGRAM   :To print 1st n prime numbers  where n is runtime input
FILE NAME :1stnprimelist.py
CREATED BY:Subhashis Patbandha
DATED     :30/09/2020
'''
num=int(input("\nEnter an integer value of n  : "))
a=2
ctr=0
print("\nFirst ",num," prime numbers are = \n")
while(num!=0):
    for i in range(2,a):
        if(a%i==0):
            break
    else:
        print(a,end=" ")
        num-=1
    a+=1        
    
