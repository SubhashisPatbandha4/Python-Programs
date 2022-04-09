def gcd(a,b):
    while(a!=b):
        if(a>b):
            a=a-b
        else:
            b=b-a
    return a

x=int(input("Enter 1st integer : "))
y=int(input("Enter 2nd integer : "))
gcd=gcd(x,y)
print("GCD OF ",x,",",y," : ",gcd)
    
