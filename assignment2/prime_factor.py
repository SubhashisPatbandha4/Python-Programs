# PROGRAM: Print all the prime factors of a given number
# FILE: prime_factor.py
# CREATED BY: Subhashis Patbandha
# DATED: 23/09/20

num = int(input("\nEnter a number: "))
ctr=0
print("\nPrime factors of ",num," are = ",end="")
for i in range(2,num+1):
    ctr=0
    if(num%i==0):
      
        for j in range(1,i+1):
            if i%j==0:  
                ctr=ctr+1
    if(ctr==2):
        print(i,end=" ")
if(ctr==0):
    print(num," has no prime factors")
                