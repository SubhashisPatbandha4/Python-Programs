'''
Assignment 3.1
==============
PROGRAM   :To print all perfect numbers between m and n where m,n are runtime input
FILE NAME :perfectnumlist.py
CREATED BY:Subhashis Patbandha
DATED     :30/09/2020
'''
n=int(input("\nplease enter lower limit :"))
m=int(input("\nplease enter upper limit :"))
print("\nAll perfect numbers between ",n," and ",m," are =",end="")

for i in range(n,m+1):
    s=0
    temp=n
    for j in range(1,i):
        if(i%j==0):
            s=s+j
    if(s==i):
        print(i,end=" ")
    
